<?php

class Enemigo extends Personaje
{
    public int $experienciaAlDerrotar;
    public int $oroAlDerrotar;

    public function __construct($nombre, $vida, $ataque, $defensa, $experienciaAlDerrotar, $oroAlDerrotar)
    {
        parent::__construct($nombre, $vida, $ataque, $defensa);
        $this->experienciaAlDerrotar = $experienciaAlDerrotar;
        $this->oroAlDerrotar = $oroAlDerrotar;
    }

    public function printCharacter(): void
    {
        parent::printCharacter();
        echo "Experiencia al derrotar: " . $this->experienciaAlDerrotar . "<br>";
        echo "Oro al derrotar: " . $this->oroAlDerrotar . "<br>";
    }

    
}