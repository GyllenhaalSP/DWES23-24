<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>PRACTICA 4 - DANIEL ALONSO LAZARO</title>
    <style>
        body {
            margin: 0;
            padding: 0;
        }

        .line {
            height: 5px;
            background-color: green;
        }
    </style>
</head>
<body>
    <?php
    for ($i = 0; $i <= 255; $i += 2) {
        $greenValue = $i;
        $blueValue = 255 - $i;
        $color = "rgb(0, $greenValue, $blueValue);";
        echo "<div class='line' style='background-color: $color'></div>";
    }
    ?>
</body>
</html>