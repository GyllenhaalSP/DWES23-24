<?php
include('infoCiclos.php');
/**
 * @var $ciclos array
 */
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>PRÁCTICA 3 - DANIEL ALONSO LÁZARO</title>
</head>
<body>
<div id="ciclos">
    <h1>CICLOS FORMATIVOS</h1>
    <ul>
        <?php
        foreach ($ciclos as $ciclo) {
            echo "<li>${ciclo['nombre']}: <a href='${ciclo['enlace']}'>${ciclo['desc']}</a></li>\n";
        }
        ?>
    </ul>
</div>
</body>
</html>

