<?php
/**
 * @var string $info
 */
include 'procesador.php';

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <link href="styles.css" rel="stylesheet">
    <title>PRÁCTICA - DANIEL ALONSO LÁZARO Y VÍCTOR HELLÍN SÁEZ</title>
    <script src="main.js"></script>
</head>
<body>
<form action="procesador.php" method="get">
    <input id="textAreaInfo" name="info" type="text" value="<?= $info ?>">
    <input id="botonSubmit" type="submit" value="Analiza">

    <h2><? echo $info ?> </h2>
</form>
</body>
</html>