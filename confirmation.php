<!DOCTYPE html>
<html>

<head>
    <title>Greenhouse Butler</title>
    <link rel="stylesheet" href="styles.css"> 
</head>


<body>

    <h1>GreenhouseButler</h1>
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
    echo "$txt"; //Udskriver parametrer på skærmen
    fwrite($file, $txt);
    fclose($file);
    ?>


</body>
</html> 
