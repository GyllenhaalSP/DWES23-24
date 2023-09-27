<?php
$frutas = ["Manzana", "Plátano", "Naranja", "Uva"];

function imprimir($frutas): void
{
    foreach ($frutas as $k => $fruta) {
        echo ($k + 1) . ".- " . $fruta . "<br>";
    }
}

function imprimirTabla($frutas): void
{
    echo "<table>";
    foreach ($frutas as $k => $fruta) {
        echo "<tr><td>" . ($k + 1) . "</td><td>" . $fruta . "</td></tr>";
    }
    echo "</table>";
}

function imprimirTablaSinBucles($frutas): void
{
    array_map(function ($k, $fruta) {
        echo "<tr><td>" . ($k + 1) . "</td><td>" . $fruta . "</td></tr>";
    }, array_keys($frutas), $frutas);
}