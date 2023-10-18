<?php
require "SistemaSolar.php";
require "Planeta.php";

session_start();

if (!isset($_SESSION['sistemaSolar'])) {
    $_SESSION['sistemaSolar'] = new SistemaSolar();
}

$sistemaSolar = $_SESSION['sistemaSolar'];