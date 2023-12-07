<!DOCTYPE html>
<html>
    
<head>
    <title>Greenhouse Butler</title>
    <link rel="stylesheet" href="styles.css"> 
</head>

<body>



    <h1>GreenhouseButler</h1>
    <p>Her kan du ændre parameterne for GHB's sensorer</p>
    
    <div class="main-container">
        <div class="tabs">
            <button class="button button1" onclick="location.href='index.php';">
                Home
            </button>
        </div>
    </div>

     
    <form action="confirmation.php" method="post">



        <?php 
        $txt = file_get_contents("parameters.txt");
        $vals = explode(' ', $txt);
    
        echo 'Jordfugt: <input type="number" name="jordfugt" min=0 max=100 value=' . $vals[0] . ' >%<br>';
        echo 'Luftfugt: <input type="number" name="luftfugt" min=0 max=100 value=' . $vals[1] . '>%<br>';
        echo 'Temperatur: <input type="number" name="temp" min=-10 max=70 value=' . $vals[2] . '>&deg;C<br>';
        echo 'Sollys: <input type="number" name="sollys" min=0 max=24 value=' . $vals[3] . '>Timer<br>';
        ?>    



        <br>
        <input type="submit">
    </form>
</body>
</html> 
