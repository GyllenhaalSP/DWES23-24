<?php
require('fpdf.php');
$nombre = $_GET['nombre'] ?? '';
$empresa = $_GET['empresa'] ?? '';
$fecha = date("d/m/Y", strtotime($_GET['fecha'] ?? ''));

$carta = "$nombre <br class='salto'>
$fecha<br>
<p>Estimado/a señor/a de Recursos Humanos de $empresa,<br class='salto'>
me dirijo a usted como candidato/a para la posición de Programador Junior en $empresa. <br><br class='salto'>
Mi experiencia en PHP me ha preparado para poder contribuir de manera significativa al futuro éxito de $empresa. <br><br class='salto'>
Adjunto mi currículum vitae para su revisión y quedo a su disposición para una posible entrevista.
<br class='salto'>Agradezco su consideración y espero la oportunidad de formar parte de su equipo.<br><br class='salto'>
Atentamente,<br class='salto'>
$nombre</p>";

$pdfOutput = str_replace(["<br class='salto'>", "<p>", "</p>"], "", $carta);
$pdfOutput = str_replace("<br>", "\n", $pdfOutput);
$pdfOutput = iconv('UTF-8', 'windows-1252', $pdfOutput);

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link href="styles.css" rel="stylesheet">
    <title>CARTA DE PRESENTACIÓN</title>
    <script src="main.js"></script>
</head>
<body>
<div class="carta">
    <?php echo $carta ?>
</div>
<form action="generarPDF.php" method="POST" target="_blank">
    <input type="hidden" name="pdfContent" value="<?= base64_encode($pdfOutput) ?>">
    <div class="boton">
        <button type="submit" name="generatePdf" value="Obtener PDF">Obtener PDF</button>
    </div>
</form>
</body>
</html>
