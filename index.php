<!DOCTYPE html>
<html>

<head>
    <title>Greenhouse Butler</title>
    <link rel="stylesheet" href="styles.css"> 
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js"></script>
    <script type = "module" src="getChartData.js"></script>
</head>


<body>

    <div class= "container">
        <pre>
    
  /$$$$$$                                          /$$                                               /$$$$$$$              /$$     /$$                    
 /$$__  $$                                        | $$                                              | $$__  $$            | $$    | $$                    
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$ | $$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$$  /$$$$$$ | $$  \ $$ /$$   /$$ /$$$$$$  | $$  /$$$$$$   /$$$$$$ 
| $$ /$$$$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$| $$  | $$ /$$_____/ /$$__  $$| $$$$$$$ | $$  | $$|_  $$_/  | $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  \__/| $$$$$$$$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$| $$  | $$|  $$$$$$ | $$$$$$$$| $$__  $$| $$  | $$  | $$    | $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$      | $$_____/| $$_____/| $$  | $$| $$  | $$| $$  | $$| $$  | $$ \____  $$| $$_____/| $$  \ $$| $$  | $$  | $$ /$$| $$| $$_____/| $$      
|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$| $$  | $$| $$  | $$|  $$$$$$/|  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$/  |  $$$$/| $$|  $$$$$$$| $$      
 \______/ |__/       \_______/ \_______/|__/  |__/|__/  |__/ \______/  \______/ |_______/  \_______/|_______/  \______/    \___/  |__/ \_______/|__/      

        </pre>
    </div>
    
    <p>Her er sensor data fra GHB for de sidste 7 dage</p>


    <div class="base-container">
        <!-- tabs to access "home" and "Sensor variables" -->
        <div class="tabs">
            <button class="button button1" onclick="location.href='parameters.php';">
                Sensor Parameters
            </button>
        </div>

        <!-- 1st row of plot-->
        <div class="main-container">
            <div class="chart-container-1">
                <canvas id="chart-1"></canvas>
            </div>

            <div class="chart-container-2">
                <canvas id="chart-2"></canvas>
            </div>
        </div>

        <!-- 2nd row of plot-->
        <div class="main-container">
            <div class="chart-container-3">
                <canvas id="chart-3"></canvas>
            </div>

            <div class="chart-container-4">
                <canvas id="chart-4"></canvas>
            </div>
        </div>

      </div>
      
      <div class="sensorStatus">
        <div>
            <h1>Sensor Status</h1>
        </div>
        
        
              <?php 
        $txt = file_get_contents("sensorStatus.txt");
        $status = explode(' ', $txt);
        ?>    

      
    <div class="box">
        <?php echo '<div class="watchdogBox ' . ($status[0] ? 'inactiveSensor' : 'activeSensor') . '">'; ?>
            <div>
                <h1> <?php echo ($status[0] ? 'X' : 'O'); ?> </h1>
            </div>
            <div>
                <p> Luftfugt </p>
            </div>
        </div>
        

        <?php echo '<div class="watchdogBox ' . ($status[1] ? 'inactiveSensor' : 'activeSensor') . '">'; ?>
            <div>
                <h1> <?php echo ($status[1] ? 'X' : 'O'); ?> </h1>
            </div>
            <div>
                <p> Temperatur </p>
            </div>
        </div>
        
        
        <?php echo '<div class="watchdogBox ' . ($status[2] ? 'inactiveSensor' : 'activeSensor') . '">'; ?>
            <div>
                <h1> <?php echo ($status[2] ? 'X' : 'O'); ?> </h1>
            </div>
            <div>
                <p> Jordfugt </p>
            </div>
        </div>
        
        
        <?php echo '<div class="watchdogBox ' . ($status[3] ? 'inactiveSensor' : 'activeSensor') . '">'; ?>
            <div>
                <h1> <?php echo ($status[3] ? 'X' : 'O'); ?> </h1>
                
            </div>
            <div>
                <p> Sollys </p>
            </div>
        </div>
      </div>
      </div>
      </div>

</body>
</html> 
