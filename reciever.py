'''
UART communication on Raspberry Pi using Pyhton
http://www.electronicwings.com
'''
import serial
import struct
from bitarray import bitarray
from bitarray.util import ba2int
from datetime import datetime
from datetime import timedelta
from time import sleep
from enum import Enum

Sensor = Enum('Sensor', ['LuftFugt', 'Temp', 'JordFugt', 'Sollys'], start=0)

def readUART():
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    
    # Generate bitarray and load the first byte into it. We can now manipulate the first byte.
    errAkt = bitarray()
    errAkt.frombytes(received_data[0:1])
    
    # Genererer en array med floats representerende de målte sensorværdier
    [temp, luft_fugt, jord_fugt, sollys] = struct.unpack('ffff', received_data[1:17])
    
    return errAkt, temp, luft_fugt, jord_fugt, sollys
    

def logSensorStatus(errAkt):
    sensorStatusFile = open('sensorStatus.txt', 'w')
    for i in range(4):
        bitMask = bitarray('00000001') << i
        sensorStatus = '0 '
        if ba2int(errAkt & bitMask):
            sensorStatus = '1 '
            
        sensorStatusFile.write(sensorStatus)
        
    sensorStatusFile.close()

def logData(errAkt, temp, luft_fugt, jord_fugt, sollys):

    # Skriv til temp_data.txt
    logDataInFile('Temperatur.txt', temp, Sensor.Temp, errAkt)
    
    # Skriv til luftfugt_data.txt
    logDataInFile('Luftfugt.txt', luft_fugt, Sensor.LuftFugt, errAkt)
    
    # Skriv til jordfugt_data.txt
    logDataInFile('Jordfugt.txt', jord_fugt, Sensor.JordFugt, errAkt)
    
    # Skriv til sollys_data.txt
    logDataInFile('Sollys.txt', sollys, Sensor.Sollys, errAkt)
    
    # Skriv sensor status til fil
    logSensorStatus(errAkt)
    
    # Send grænseværdier som svar
    sendGrænseVærdier()
    
    
    
def sendGrænseVærdier():
    grænseværdiFil = open('parameters.txt', 'r')
    
    grænseværdier = grænseværdiFil.readline().split()
    
    jordfugtGrænse = int(grænseværdier[0])
    luftfugtGrænse = int(grænseværdier[1])
    temperaturGrænse = int(grænseværdier[2])
    sollysGrænse = int(grænseværdier[3])
    
    nightTime = 6 + sollysGrænse

    hour = datetime.now().time().hour
    
    isNight = 1 if hour > nightTime else 0
    
    print(f'sending: \n jordfugt: {jordfugtGrænse} \n luftfugt: {luftfugtGrænse} \n temp: {temperaturGrænse} \n isNight: {isNight}\n')
    
    packageToSend = struct.pack('bbbb', jordfugtGrænse, luftfugtGrænse, temperaturGrænse, isNight)
    
    ser.write(packageToSend)
    
# Returns a string representiv the current time in the format 
# day-month-year hour:minute:second
def getTime():
    now = str(datetime.now())
    time = ""
    for char in now:
        if char == ".":
            break
        time += char
    return time
    
    
def formatDate(date):
    return date[0:4] + " " + date[5:16]


# Generates a specific value from a month and year parameter
def getMonthValue(year, month):

    monthValue = 0

    if month == 1: 
            monthValue = 0
    if month == 2: 
            monthValue = 31
    if month == 3:
            monthValue = 59
    if month == 4:
            monthValue = 90
    if month == 5:
            monthValue = 120
    if month == 6:
            monthValue = 150
    if month == 7:
            monthValue = 181
    if month == 8:
            monthValue = 212
    if month == 9:
            monthValue = 242
    if month == 10:
            monthValue = 273
    if month == 11:
            monthValue = 303
    if month == 12:
            monthValue = 334

    if month != 1 and month != 2:
        if year % 4 == 0:
            monthValue += 1

    return monthValue
    

# Generates a specific value for a measurement based on the time that the measurement was taken.
def getDayNumber(date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    hour = float(date[11:13])
    minute = float(date[14:16])

    day = (year - 2023)*365 + getMonthValue(year, month) + day + hour/24.0 + minute/1440 

    return day
 

# Logs data to specified file
# Params:
#   fileToWriteTo:      String edescribing the name of the file to write to. e.g "example.txt". File must be in same folder as script
#   data:               float containing the data that is to be logged
#   sensorNumber:       a number between 1 and 4 (botgh inclusive) that specifies what sensor the data was captured from.
#                           0:  Luftfugt sensor
#                           1:  Temperature sensor
#                           2:  Jordfugt sensor
#                           3:  Sollys sensor
#   AktuatorErrorByte:  bitarray representing the first recieved byte of the transmission. Holds information on whether an aktuator was activated or not
def logDataInFile(fileToWriteTo, data, sensorEnum, AktuatorErrorByte):
    log = open(fileToWriteTo, "r" )
    timeNow = getTime()
    timeScore = getDayNumber(timeNow) # days since 31th dec. 2022
    date = formatDate(timeNow)
    
    # Generate a bitmask from the enum signifying which sensor we are logging
    # Use that bitmask to check if the actuator for the sensor was activated.
    bitMask = bitarray('00010000') << sensorEnum.value
    aktuatorStatus = 0
    if ba2int(AktuatorErrorByte & bitMask):
        aktuatorStatus = 1
        
      
    bitMask = bitarray('00000001') << sensorEnum.value
    sensorStatus = 0
    if ba2int(AktuatorErrorByte & bitMask):
        sensorStatus = 1
    
    # We loop through all data in the log. If a datapoint is older than 7 days, as seen from the score of the datapoint,
    # the datapoint is NOT put in the currentLoggedData array for relogging.
    currentLoggedData = []
    fileHasData = False

    for line in log:
        bata = line.split()
        if bata:
            fileHasData = True
            if timeScore - float(bata[-1]) < 7:
                currentLoggedData.append(line)

    if(fileHasData):
        previousTimeScore = currentLoggedData[-1].split()[-1]
        timeScoreDiff = float(timeScore) - float(previousTimeScore)
    
        if timeScoreDiff > 0.0072:
            #how many entries are missing
            missingEntriesNum = int(timeScoreDiff//0.0069)
            print("Nr of missing entries", missingEntriesNum)
        
        
            lastEntry = currentLoggedData[-1].split()
            year = lastEntry[0]
            month_day = lastEntry[1].split("-")
            hour_minute = lastEntry[2].split(":")
        
            lastKnownTime = datetime(int(year), int(month_day[0]), int(month_day[1]), int(hour_minute[0]), int(hour_minute[1]), 0)
        
            for i in range(1,missingEntriesNum):
                timeDelta = timedelta(minutes = 10)
                lastKnownTime = lastKnownTime + timeDelta
                emptyEntry = lastKnownTime.strftime("%Y %m-%d %H:%M ") + "0 " + "0 " + "0 " + str(getDayNumber(str(lastKnownTime))) + "\n"   
                # str(lastKnownTime.month) + "-" + str(lastKnownTime.day) + " " + str(lastKnownTime.hour) + ":" + str(lastKnownTime.minute)
                currentLoggedData.append(emptyEntry)
            
    # Generate a new datapoint that we then add to the currentLoggedData array        
    newEntry = date + " " + str(data) + " " + str(AktuatorStatus) + str(sensorStatus) + " " + str(timeScore) + "\n"     
    currentLoggedData.append(newEntry)       
    log.close()
    
    # Open in write mode and log the data
    log = open(fileToWriteTo, 'w')
    for line in currentLoggedData: 
        log.write(line)
    log.close()


ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate

while True: 

    errAkt, temp, luft_fugt, jord_fugt, sollys = readUART()

    
    logData(errAkt, temp, luft_fugt, jord_fugt, sollys)

    # Dummy data
    #data_AktErr         = b'\x00'
    
    #data_sensor_one     = b'\x10\x11\x12\x13'
    #data_sensor_two     = b'\x14\x15\x16\x17'
    #data_sensor_three   = b'\x18\x19\x1A\x1B'
    #data_sensor_four    = b'\x1C\x1D\x1E\x1F'

    #data_limit_one      = b'\x10'
    #data_limit_two      = b'\x11'
    #data_limit_three    = b'\x12'
    #data_limit_four     = b'\x13'

    #received_data = data_AktErr + data_sensor_one + data_sensor_two + data_sensor_three + data_sensor_four + data_limit_one + data_limit_two + data_limit_three + data_limit_four



    
    # UART DATA PROTOKOL ARDUINO -> RASPBERYY PI:
    # Vi modtager watchdog fejl og aktuator aktiverings-status som 8bit
    
    # første fire bit fra aktuatorer 1 = aktuator blev aktiveret
    # 0b00010000 - lufthydrerings-system
    # 0b00100000 - kølesystem
    # 0b01000000 - vandingssystem
    # 0b10000000 - lampe
    
    # næste fire bit fra watchdog: 1 = fejl på sensor
    # 0b00000001 - luftfugt sensor 
    # 0b00000010 - temp sensor
    # 0b00000100 - jordfugt sensor
    # 0b00001000 - lys sensor
    
    # Dernæst 4x4 byte som beskriver målinger i rækkefølgen:
    # Temp
    # Luftfugtighed
    # Jordfugtighed
    # Sollys

    # dag:måned timer:minutter sensorværdi 1/0 score
    


    # UART DATA PROTOKOL RASPBERRY PI --> ARDUINO (GRÆNSEVÆRDIER)
    # Sender 4x1 bytes som beskriver nye grænseværdier i rækkefølgen:
    # Temp
    # Luftfugtighed
    # Jordfugtighed
    # Sollys 

    
    
    

