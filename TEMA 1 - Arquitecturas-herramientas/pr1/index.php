<!DOCTYPE html>
<html lang="en">
<?php
if (isset($_POST["edad"])) {
    $edad = $_POST["edad"];
} else {
    $edad = 0;
}
$nombre = "Daniel Alonso Lázaro";
$texto = "Hola, me llamo $nombre y tengo $edad años";
$color = "";
if ($edad <= 18) {
    $color = "azul";
} else {
    $color = "blanco";
}
?>
<head>
    <meta charset="UTF-8">
    <title>Pruebis</title>
    <style>
        .azul {
            color: blue;
            background-color: white;
        }

        .blanco {
            color: white;
            background-color: blue;
        }
    </style>
</head>
<body class="<?php echo $color ?>">
<h1>Introduce tu edad</h1>
<form action="index.php" method="post">
    <label>
        <input type="text" name="edad">
    </label>
    <input type="submit" value="Enviar">
</form>
<p><?php echo $texto ?></p>

</body>
</html>