<?php
require_once "config.php";
/**
 * @var SistemaSolar $sistemaSolar
 */
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <meta name="description" content="EJERCICIOS OBJETOS - EJERCICIO 1">
    <meta name="author" content="Daniel Alonso Lázaro">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title></title>
    <script src="main.js"></script>
</head>
<body>
<div>
    <h1>Introduce un planeta</h1>
    <form action="form_processing.php" method="post" id="form">
        <label for="nombre">Nombre</label>
        <input type="text" name="nombre" id="nombre" required><br>
        <label for="masa">Masa</label>
        <input type="number" name="masa" id="masa" required><br>
        <label for="diametro">Diámetro</label>
        <input type="number" name="diametro" id="diametro" required><br>
        <label for="distanciaSol">Distancia al Sol</label>
        <input type="number" name="distanciaSol" id="distanciaSol" required><br>
    </form>
    <input type="submit" value="Enviar" form="form">
    <input type="button" value="Resetear sesión" id="resetear" onclick="resetear()">
</div>
<div>
    <h1>Tabla de planetas</h1>
    <?php
    $sistemaSolar->mostrarTabla();
    ?>
</div>

</body>
</html>