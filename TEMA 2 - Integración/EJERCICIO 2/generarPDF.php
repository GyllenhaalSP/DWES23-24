<?php
require('fpdf.php');

if (isset($_POST['generatePdf'])) {
    $pdfContent = base64_decode($_POST['pdfContent']);

    // Configurar cabeceras para indicar que se está enviando un PDF
    header('Content-Type: application/pdf');
    header('Content-Disposition: inline; filename="carta.pdf"');

    // Crear una instancia de FPDF y agregar el contenido
    $pdf = new FPDF();
    $pdf->AddPage();
    $pdf->SetFont('Arial', 'B', 16);
    $pdf->MultiCell(0, 10, $pdfContent, 0, 1);

    // Generar el PDF y enviarlo al navegador
    $pdf->Output();
}
