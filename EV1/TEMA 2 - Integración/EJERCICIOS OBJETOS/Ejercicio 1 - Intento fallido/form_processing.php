<?php
require_once "config.php";
/**
 * @var SistemaSolar $sistemaSolar
 */

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $sistemaSolar->addPlaneta(
        Planeta::crearPlaneta(
            $_POST["nombre"],
            $_POST["masa"],
            $_POST["diametro"],
            $_POST["distanciaSol"]
        )
    );
}