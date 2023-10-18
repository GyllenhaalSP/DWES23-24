<?php

class Planeta
{
    public string $nombre;
    public float $masa;
    public float $diametro;
    public float $distanciaSol;

    public static function crearPlaneta($nombre, $masa, $diametro, $distanciaSol): Planeta
    {
        $planeta = new Planeta();
        $planeta->nombre = $nombre;
        $planeta->masa = $masa;
        $planeta->diametro = $diametro;
        $planeta->distanciaSol = $distanciaSol;
        return $planeta;
    }

    public function muestraDivSpan()
    {

    }

    public function muestraEdicion()
    {

    }

    function muestraFilaTabla(): void
    {
        echo "<tr><td>$this->nombre</td><td>$this->masa</td><td>$this->diametro</td><td>$this->distanciaSol</td></tr>";
    }
}

