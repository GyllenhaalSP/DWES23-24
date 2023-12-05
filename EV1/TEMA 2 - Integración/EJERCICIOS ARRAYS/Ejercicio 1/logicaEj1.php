<?php
$frutas = ["Manzana", "Plátano", "Naranja", "Uva"];

function imprimir($frutas): void
{
    echo $html = "<ol>";
    foreach ($frutas as $fruta) {
        echo "<li>" . $fruta . "</li>";
    }
    echo substr_replace($html, "/", 1, 0);
}

function imprimirTabla($frutas): void
{
    echo $html = "<table>";
    foreach ($frutas as $k => $fruta) {
        echo "<tr><td>" . ($k + 1) . "</td><td>" . $fruta . "</td></tr>";
    }
    echo substr_replace($html, "/", 1, 0);
}

function imprimirTablaSinBucles($frutas): void
{
    echo $html = "<table>";
    array_map(function ($k, $fruta) {
        echo "<tr><td>" . ($k + 1) . "</td><td>" . $fruta . "</td></tr>";
    }, array_keys($frutas), $frutas);
    echo substr_replace($html, "/", 1, 0);
}