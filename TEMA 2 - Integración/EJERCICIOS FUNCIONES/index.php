<?php
require('funciones.php');
/**
 * @var int $suma
 * @var int $resta
 * @var int $multiplicacion
 * @var callable $esPrimo
 */
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta http-equiv="Content-Type" content="text/html" charset=UTF-8">
    <meta name="description" content="Ejercicios de funciones">
    <meta name="author" content="Daniel Alonso Lázaro">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="styles.css" rel="stylesheet">
    <title>EJERCICIOS FUNCIONES</title>
    <script src="main.js"></script>
</head>
<body>
<div>
    <?php
    $cadena = concatenarPalabras("Hola", "que", "tal", "estas");
    echo $cadena . "<br>";
    $concatena = ", ";
    echo concatenaCon($concatena, "yo", "muy", "bien");
    echo "<br>";
    echo "3+4 es " . aplicarOperacion($suma, 3, 4) . "<br>";
    echo "3-4 es " . aplicarOperacion($resta, 3, 4) . "<br>";
    echo "3x4 es " . aplicarOperacion($multiplicacion, 3, 4) . "<br>";
    echo invertirCadena($cadena) . "&nbsp;&nbsp;&nbsp;<-- con un for" . "<br>";
    echo invertirCadena2($cadena) . "&nbsp;&nbsp;&nbsp;<-- con strrev" . "<br>";

    echo implode(", ", filtra_array($esPrimo, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17));

    
    ?>
</div>
</body>
</html>