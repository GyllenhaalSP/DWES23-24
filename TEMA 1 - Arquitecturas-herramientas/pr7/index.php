<!DOCTYPE html>
<html lang="es">
<head>
    <title>PRÁCTICA 7 - DANIEL ALONSO LÁZARO</title>
</head>
<body>
<?php

$a = 5;
$b = 3;

$suma = $a + $b;
$resta = $a - $b;
$multiplicacion = $a * $b;
$division = $a / $b;
$resto = $a % $b;

echo "<p>La suma de $a y $b es $suma</p>";
echo "<p>La resta de $a y $b es $resta </p>";
echo "<p>La multiplicación de $a y $b es $multiplicacion</p>";
echo "<p>La división de $a y $b es $division</p>";
echo "<p>El resto de $a y $b es $resto</p>";

echo "<p>El valor de a es $a</p>";
echo "<p>El valor de b es $b</p>";

echo "<p>Se aumentan a y b con el operador ++ y --</p>";
$a++;
$b--;

echo "<p>El valor de a es $a</p>";
echo "<p>El valor de b es $b</p>";

print_r(get_defined_vars());
?>
</body>
</html>