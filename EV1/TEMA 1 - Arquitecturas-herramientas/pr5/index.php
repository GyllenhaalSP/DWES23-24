<!DOCTYPE html>
<html lang="es">
<head>
    <meta http-equiv="refresh" content="0.25">
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: row;
            height: 100vh;
        }

        .techno-div {
            flex: 1;
        }
    </style>
    <title>PRACTICA 5 - DANIEL ALONSO LÁZARO</title>
</head>
<body>

<?php
$veces = 10;
$offset = 0;
$length = 6;
$colores = [];

for ($i = 0; $i < $veces; $i++) {
    $colores[] = '#' . substr(md5(rand()), $offset, $length);
}

foreach ($colores as $color) {
    echo "<div class='techno-div' style='background-color: $color;'></div>";
}
?>

</body>
</html>

