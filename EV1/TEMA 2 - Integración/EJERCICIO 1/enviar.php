<?php
$cadena = $_GET['cadena'] ?? '';
$resultadoVisible = $_GET['resultadoVisible'] ?? 'false';

function esPalindromo($cadena): bool
{
    $cadena = str_replace(' ', '', $cadena);
    $cadena = strtolower($cadena);
    $cadenaInvertida = strrev($cadena);
    if ($cadena == $cadenaInvertida) {
        return true;
    } else {
        return false;
    }
}

function numVocales($cadena): int
{
    $cadena = strtolower($cadena);
    $vocales = ['a', 'e', 'i', 'o', 'u'];
    $contador = 0;
    for ($i = 0; $i < strlen($cadena); $i++) {
        if (in_array($cadena[$i], $vocales)) {
            $contador++;
        }
    }
    return $contador;
}

function numConsonantes($cadena): int
{
    $cadena = strtolower($cadena);
    $consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
        'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'];
    $contador = 0;
    for ($i = 0; $i < strlen($cadena); $i++) {
        if (in_array($cadena[$i], $consonantes)) {
            $contador++;
        }
    }
    return $contador;
}