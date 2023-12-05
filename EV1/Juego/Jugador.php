<?php

class Jugador extends Personaje
{
    public int $experiencia;
    public int $puntosHabilidad;
    public int $oro;

    public function __construct($nombre, $vida, $ataque, $defensa)
    {
        parent::__construct($nombre, $vida, $ataque, $defensa);
        $this->experiencia = 0;
        $this->puntosHabilidad = 0;
        $this->oro = 0;
    }

    public function printCharacter(): void
    {
        parent::printCharacter();
        echo "Experiencia: " . $this->experiencia . "<br>";
        echo "Puntos de habilidad: " . $this->puntosHabilidad . "<br>";
    }

    public function masExp($cantidadExp): void
    {
        $this->experiencia += $cantidadExp;
        if ($this->experiencia >= 100) {
            parent::subirNivel();
            $this->experiencia = 0;
        }
        echo $cantidadExp . " puntos de experiencia añadidos. <br>";
        echo "Experiencia actual: " . $this->experiencia . "<br>";
    }

    public function subirNivel(): void
    {
        parent::subirNivel();
        $this->puntosHabilidad += 5;
        echo "¡Has subido de nivel! <br>";
        echo "Nivel actual: " . $this->nivel . "<br>";
        echo "Puntos de habilidad: " . $this->puntosHabilidad . "<br>";
    }

    public function masOro($cantidadOro): void
    {
        $this->oro += $cantidadOro;
        echo $cantidadOro . " monedas de oro añadidas. <br>";
        echo "Oro actual: " . $this->oro . "<br>";
    }
}