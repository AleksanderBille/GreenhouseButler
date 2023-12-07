<!DOCTYPE html>
<html>

<head>
    <title>Greenhouse Butler</title>
    <link rel="stylesheet" href="styles.css"> 
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
    <p>Du har ændret parameterne</p>
    
    <div class="main-container">
        <div class="tabs">
            <button class="button button1" onclick="location.href='index.php';">
                Home
            </button>
            <button class="button button1" onclick="location.href='parameters.php';">
                Sensor Parameters
            </button>
            
        </div>
    </div>
    
    <?php 
    
    $file = fopen("parameters.txt", "w");
    //$txt = "Hej";
     $txt = "{$_POST['jordfugt']} {$_POST['luftfugt']} {$_POST['temp']} {$_POST['sollys']}";
    fwrite($file, $txt);
    fclose($file);
    ?>


<div class= "container">
    <pre>

~ Grænseværdi troldmand ~
                      .  
                         
                   .     
         /^\     .       
    /\   "V"             
   /__\   I      O  o    
  //..\\  I     .        
  \].`[/  I              
  /l\/j\  (]    .  O     
 /. ~~ ,\/I          .   
 \\L__j^\/I       o      
  \/--v}  I     o   .    
  |    |  I   _________  
  |    |  I c(`       ')o
  |    l  I   \.     ,/  
_/j  L l\_!  _//^---^\\_ 
    </pre>
</div>

</body>
</html> 
