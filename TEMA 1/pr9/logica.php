<?php

$iteraciones = rand(10, 30);


function piramide(int $iteraciones): void
{
    if ($iteraciones % 2 == 0) {
        $iteraciones--;
    }
    $medio = $iteraciones % 2;
    for ($i = 1; $i <= $iteraciones; $i++) {
        for ($j = 0; $j < $iteraciones - $i; $j++) {
            echo "<span>&nbsp;&nbsp;&nbsp;</span>";
        }
        for ($k = 0; $k < $medio; $k++) {
            $rgb = "rgb(" . rand(0, 255) . " " . rand(0, 255) . " " . rand(0, 255) . ")";
            echo "<span id='span' style='background-color: $rgb;'>&nbsp;&nbsp;&nbsp;</span>";
        }
        echo "<br>";
        $medio += 2;
    }
}