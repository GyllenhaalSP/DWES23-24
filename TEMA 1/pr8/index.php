<!DOCTYPE html>
<html lang="es">
<head>
    <title>PRÁCTICA 8 - DANIEL ALONSO LÁZARO</title>
</head>
<body>
<?php
$min = 1;
$max = 10;
$n = rand($min, $max);

function imprimirPiramide($altura): void
{
    for ($i = 1; $i <= $altura; $i++) {
        echo str_repeat("&nbsp;&nbsp;", $altura - $i);
        echo str_repeat("*", 2 * $i - 1);
        echo "<br>";
    }
}

imprimirPiramide($n);
?>
</body>
</html>