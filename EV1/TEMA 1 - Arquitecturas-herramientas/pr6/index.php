<?php
include "calculaciones.php";
/**
 * @var float $r
 * @var string $nombre
 * @var float $area
 * @var float $perimetro
 */
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>PRÁCTICA 6 - DANIEL ALONSO LÁZARO</title>
    <style>
        .contenedor {
            background-color: #cccccc;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
    </style>
</head>
<body>
<div class="contenedor">
    <?php
    echo "<h1>¡Bienvenido a mi página, $nombre!</h1>";
    printf("<p>El radio de la circunferencia es: %d</p>", $r);
    printf("<p>El area de la circunferencia es: %.2f</p>", $area);
    printf("<p>El perímetro de la circunferencia es: %.2f</p>", $perimetro);
    ?>
</div>
</body>
</html>


