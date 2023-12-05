<?php
include("logicaEj1.php");
include("logicaEj2.php");
/**
 * @var array $frutas
 * @var array $alumnos
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
    <h1>EJERCICIOS ARRAYS</h1>
    <h2>Ejercicio 1</h2>
    <h3>i. Dado el array $frutas, utiliza un bucle for para imprimir cada fruta en una lista numerada.</h3>
    <p><?php imprimir($frutas); ?></p>
    <h3>ii. Imprime la información en una tabla.</h3>
    <p><?php imprimirTabla($frutas); ?></p>
    <h3>iii. Imprime la información en una tabla sin usar bucles</h3>
    <p><?php imprimirTablaSinBucles($frutas); ?></p>
    <h2>Ejercicio 2</h2>
    <h3>i. Dado el array $alumnos, utiliza un bucle while para encontrar al alumno más joven y mostrar su nombre y
        edad.</h3>
    <p><?php alumnoMasJovenWhile($alumnos); ?></p>
    <h3>ii. Realiza la anterior tarea sin bucle.</h3>
    <p><?php alumnoMasJoven($alumnos); ?></p>
    <h3>iii. Muestra una tabla de los alumnos ordenados por edad.</h3>
    <p><?php alumnosOrdenadosEdad($alumnos); ?></p>
    <h2>Ejercicio 3</h2>

    <h2>Ejercicio 4</h2>

    <h2>Ejercicio 5</h2>

    <h2>Ejercicio 6</h2>

    <h2>Ejercicio 7</h2>

    <h2>Ejercicio 8</h2>

    <h2>Ejercicio 9</h2>
</div>
</body>
</html>
