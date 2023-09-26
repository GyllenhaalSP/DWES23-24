<?php

function concatenarPalabras(...$palabras): string
{
    $resultado = "";
    foreach ($palabras as $palabra) {
        $resultado .= $palabra . " ";
    }
    return trim($resultado);
}

function concatenaCon(&$cadena = " ", ...$palabras): string
{
    return " " . concatenarPalabras(implode($cadena, $palabras));
}

$suma = function ($a, $b) {
    return $a + $b;
};

$resta = function ($a, $b) {
    return $a - $b;
};

$multiplicacion = function ($a, $b) {
    return $a * $b;
};

function aplicarOperacion($operacion, $a, $b): int
{
    return $operacion($a, $b);
}

aplicarOperacion($multiplicacion, 3, 4);

function invertirCadena(string $cadena): string
{
    $resultado = "";
    for ($i = strlen($cadena) - 1; $i >= 0; $i--) {
        $resultado .= $cadena[$i];
    }
    return $resultado;
}

function invertirCadena2(string $cadena): string
{
    return strrev($cadena);
}


