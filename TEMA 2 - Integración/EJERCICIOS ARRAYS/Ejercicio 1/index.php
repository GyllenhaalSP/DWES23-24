<?php
include("logicaEj1.php");
/**
 * @var array $frutas
 */
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta http-equiv="Content-Type" content="text/html" charset=UTF-8">
    <meta name="description" content="Ejercicio 1 de Arrays">
    <meta name="author" content="Daniel Alonso Lázaro">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="styles.css" rel="stylesheet">
    <title>EJERCICIOS ARRAYS - Ejercicio 1</title>
    <script src="main.js"></script>
    <style>
        table {
            border-collapse: collapse;
        }

        td {
            border: 1px solid black;
            padding: 5px;
        }
    </style>
</head>
<body>
<div>
    <h4>a) Dado el array $frutas, utiliza un bucle for para imprimir cada fruta en una lista numerada.</h4>
    <p><?php imprimir($frutas); ?></p>
    <h4>b) Imprime la información en una tabla.</h4>
    <p><?php imprimirTabla($frutas); ?></p>
    <h4>c) Imprime la información en una tabla sin usar bucles</h4>
    <p><?php imprimirTablaSinBucles($frutas); ?></p>
</div>
</body>
</html>
