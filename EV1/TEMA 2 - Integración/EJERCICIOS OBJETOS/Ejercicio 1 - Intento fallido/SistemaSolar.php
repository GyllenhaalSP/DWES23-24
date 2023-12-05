<?php

class SistemaSolar
{
    private array $planetas = [];

    public function getPlanetas(): array
    {
        return $this->planetas;
    }

    function guardarEnFichero()
    {

    }

    function cargarEnFichero()
    {

    }

    function mostrarTabla(): void
    {
        echo "<table>";
        echo "<tr><th>Nombre</th><th>Masa</th><th>Diámetro</th><th>Distancia al Sol</th></tr>";
        foreach ($this->planetas as $planeta) {
            $planeta->muestraFilaTabla();
        }
        echo "</table>";
    }

    function addPlaneta(Planeta $planeta): void
    {
        $this->planetas[] = $planeta;
    }
}