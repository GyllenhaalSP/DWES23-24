<?php

class Personaje
{
    public string $nombre;
    public int $vida;
    public float $ataque;
    public float $defensa;
    public float $magia;
    public float $velocidad;
    public int $nivel;

    public function __construct($nombre, $vida, $ataque, $defensa)
    {
        $this->nombre = $nombre;
        $this->vida = $vida;
        $this->ataque = $ataque;
        $this->defensa = $defensa;
        $this->magia = 0;
        $this->velocidad = 0;
        $this->nivel = 0;
    }

    public function masPS($masVida): void
    {
        $this->vida += $masVida;
    }

    public function masAtaque($masAtaque): void
    {
        $this->ataque += $masAtaque;
    }

    public function menosAtaque($menosAtaque): void
    {
        $this->ataque -= $menosAtaque;
    }

    public function masDefensa($masDefensa): void
    {
        $this->defensa += $masDefensa;
    }

    public function menosDefensa($menosDefensa): void
    {
        $this->defensa -= $menosDefensa;
    }

    public function masMagia($masMagia): void
    {
        $this->magia += $masMagia;
    }

    public function menosMagia($menosMagia): void
    {
        $this->magia -= $menosMagia;
    }

    public function masVelocidad($masVelocidad): void
    {
        $this->velocidad += $masVelocidad;
    }

    public function menosVelocidad($menosVelocidad): void
    {
        $this->velocidad -= $menosVelocidad;
    }

    public function printCharacter(): void
    {
        echo "Nombre: " . $this->nombre . "<br>";
        echo "Vida: " . $this->vida . "<br>";
        echo "Ataque: " . $this->ataque . "<br>";
        echo "Defensa: " . $this->defensa . "<br>";
        if ($this->magia > 0) {
            echo "Magia: " . $this->magia . "<br>";
        }
        if ($this->velocidad > 0) {
            echo "Velocidad: " . $this->velocidad . "<br>";
        }
        echo "Nivel: " . $this->nivel . "<br>";
    }

    public function subirNivel(): void
    {
        $this->nivel++;
    }

    public function ataque($personaje): void
    {
        $dano = $this->ataque - $personaje->defensa;
        if ($dano < 0) {
            $dano = 0;
        }
        $personaje->menosPS($dano);
        echo $this->nombre . " ataca a " . $personaje->nombre . " y le hace " . $dano . " puntos de daño. <br>";
        echo $personaje->nombre . " tiene " . $personaje->vida . " puntos de vida. <br>";
    }

    public function menosPS($menosVida): void
    {
        $this->vida -= $menosVida;
    }
}