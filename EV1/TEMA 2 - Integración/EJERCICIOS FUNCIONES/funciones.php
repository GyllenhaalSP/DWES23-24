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

function invertirCadena(string &$cadena): void
{
    $resultado = "";
    for ($i = strlen($cadena) - 1; $i >= 0; $i--) {
        $resultado .= $cadena[$i];
    }
    echo $cadena = $resultado;
}

function invertirCadena2(string $cadena): string
{
    return strrev($cadena);
}

$esPrimo = function (int $numero): bool {
    if ($numero < 2) {
        return false;
    }
    for ($i = 2; $i < $numero; $i++) {
        if ($numero % $i === 0) {
            return false;
        }
    }
    return true;
};

function filtra_array(callable $esPrimo, ...$numeros): array
{
    $resultado = [];
    foreach ($numeros as $elemento) {
        if ($esPrimo($elemento)) {
            $resultado[] = $elemento;
        }
    }
    return $resultado;
}

function magia(string $etiqueta = "li", mixed ...$elementos): void
{
    if ($etiqueta == "li") {
        echo "<ul>";
    } else {
        echo "<$etiqueta>";
    }
    foreach ($elementos as $elemento) {
        echo "<$etiqueta>$elemento</$etiqueta>";
    }

    if ($etiqueta == "li") {
        echo "</ul>";
    } else {
        echo "</$etiqueta>";
    }
}

function acumuladorGlobal(int &$acumulador, array $valores): void
{
    foreach ($valores as $valor) {
        $acumulador += $valor;
    }
}

function acumuladorGlobalVariable(int &$valor, mixed ...$valores): void
{
    foreach ($valores as $elemento) {
        $valor += $elemento;
    }
}

function acumuladorGlobalVariable2(int &$valor, mixed ...$valores): void
{
    $valor = array_sum($valores);
}

$esImpar = function (int $numero): bool {
    return $numero % 2 !== 0;
};

function filtra_array2(callable $esImpar, ...$numeros): array
{
    $resultado = [];
    foreach ($numeros as $elemento) {
        if ($esImpar($elemento)) {
            $resultado[] = $elemento;
        }
    }
    return $resultado;
}