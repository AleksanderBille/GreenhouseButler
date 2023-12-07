


ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate


# Åben fil med ting i
log = open(parameters.txt, 'r')
line = log.read_docstrings()
log.close()

ser.write(line)
