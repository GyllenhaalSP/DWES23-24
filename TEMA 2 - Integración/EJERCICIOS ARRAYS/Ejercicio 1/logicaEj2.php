<?php
$alumnos = [
    ["nombre" => "Juan", "edad" => 20, "curso" => "Matemáticas"],
    ["nombre" => "Ana", "edad" => 19, "curso" => "Historia"],
    ["nombre" => "Carlos", "edad" => 21, "curso" => "Inglés"],
];

function alumnoMasJovenWhile($alumnos): void
{
    $alumnoMasJovenIndex = 0;
    while ($alumnoMasJovenIndex == 0) {
        $alumnoMasJoven = $alumnos[0];
        for ($i = 0; $i < count($alumnos); $i++) {
            if ($alumnos[$i]["edad"] < $alumnoMasJoven["edad"]) {
                $alumnoMasJoven = $alumnos[$i];
                $alumnoMasJovenIndex = $i;
            }
        }
        echo "El alumno más joven es " . $alumnoMasJoven["nombre"] . " con " . $alumnoMasJoven["edad"] . " años.";
    }
}

function alumnoMasJoven($alumnos): void
{
    $alumnosCopia = $alumnos;
    usort($alumnosCopia, function ($a, $b) {
        return $a['edad'] - $b['edad'];
    });
    $alumnoMasJoven = $alumnosCopia[0];
    echo "El alumno más joven es " . $alumnoMasJoven["nombre"] . " con " . $alumnoMasJoven["edad"] . " años.";
}

function alumnosOrdenadosEdad($alumnos): void
{
    $alumnosCopia = $alumnos;
    array_multisort(array_column($alumnosCopia, 'edad'), SORT_ASC, $alumnosCopia);
    echo $html = "<table>";
    echo "<tr>
            <td>Nombre</td>
            <td>Edad</td>
            <td>Curso</td>
         </tr>";
    foreach ($alumnosCopia as $alumno) {
        echo "<tr>
                <td>" . $alumno["nombre"] . "</td>
                <td>" . $alumno["edad"] . "</td>
                <td>" . $alumno["curso"] . "</td>
              </tr>";
    }
    echo substr_replace($html, "/", 1, 0);
}
