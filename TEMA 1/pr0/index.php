<html lang="es">
<?php
$nombre = "<p><h3>Daniel Alonso Lázaro</h3>";
$titulo = "estudiante de 2º de DAW";
$fecha = date("d-m-Y");
$hora = date("H:i:s");
$texto = "Me llamo $nombre y soy $titulo. <br><br>Estamos a $fecha a las $hora y ya me estoy muriendo con el curso.... GL</p>";
$estilo = (date("s") % 2 == 0) ? "blanco" : "verde";
?>
<head>
    <style>
        .verde {
            color: green;
            background: white;
        }

        .blanco {
            color: white;
            background: green;
        }
    </style>
    <title>
        Prueba PHP
    </title>
</head>
<body class="<?php echo $estilo ?>">
<?php
echo $texto;
?>
</body>
</html>
