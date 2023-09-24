<?php
include('data.php');
/**
 * @var $fuente string
 * @var $imagen string
 * @var $haiku string
 * @var $nombre string
 * @var $fecha string
 */
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>PRÁCTICA 2 - DANIEL ALONSO LÁZARO</title>
    <link href="<?php echo "${fuente}" ?>" rel='stylesheet'>
    <link href='styles.css' rel='stylesheet'>
    <script src="main.js"></script>
</head>
<body>
<div>
    <img id="imagen" src="<?php echo "${imagen}" ?>" alt="Facepalm" onmouseover="cambiarOpacidad()"/>
</div>
<div id="haiku">
    <blockquote title="Programming Haiku">
        <p><?= $haiku ?></p>
        <footer>
            <p><?php echo "— ${nombre}" ?></p>
        </footer>
    </blockquote>
    <p class="fecha"><?php echo "${fecha}" ?></p>
</div>
</body>
</html>