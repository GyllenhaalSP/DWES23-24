<!DOCTYPE html>
<html lang="es">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link href="styles.css" rel="stylesheet">
    <title>EJERCICIO 2 - DANIEL ALONSO LÁZARO</title>
    <script src="main.js"></script>
</head>
<body>
<form class="main" action="info.php" method="GET" id="form">
    <label for="nombre">Nombre: </label>
    <input type="text" id="nombre" name="nombre" placeholder="Nombre completo"><br><br>
    <label for="empresa">Empresa: </label>
    <input type="text" id="empresa" name="empresa" placeholder="Apple"><br><br>
    <label for="fecha">Fecha: </label>
    <input type="date" id="fecha" name="fecha" value="<?= date("Y-m-d") ?>">
    <input type="submit" value="Enviar">
</form>

</body>
</html>