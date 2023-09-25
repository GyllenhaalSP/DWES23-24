<?php
include('enviar.php');
/**
 * @var $cadena string
 * @var $resultadoVisible string
 */
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <link href="styles.css" rel="stylesheet">
    <title>EJERCICIO 1 - DANIEL ALONSO LÁZARO</title>
    <script src="main.js"></script>
</head>
<body>

<form action="index.php" method="GET" id="form">
    <label for="cadena">Cadena: </label>
    <input type="text" id="cadena" name="cadena" placeholder="Introduce una cadena..." value="<?= $cadena ?>">
    <label for="resultadoVisible"></label>
    <input type="text" id="resultadoVisible" name="resultadoVisible" value="true">
    <input type="submit" value="Enviar" onclick="revelar()" id="botonEnviar">
    <div id="resultado"
         style="<?= ($resultadoVisible === "true") ? "display:block;" : "display:none;" ?>">
        <ul>
            <li>Número de vocales: <?= numVocales($cadena) ?></li>
            <li>Número de consonantes: <?= numConsonantes($cadena) ?></li>
            <li>Es palíndromo: <?= empty($cadena) ? "¿?" : (esPalindromo($cadena) ? 'Sí' : 'No') ?></li>
        </ul>
    </div>
</form>


</body>
</html>
