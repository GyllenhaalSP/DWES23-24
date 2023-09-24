function cambiarOpacidad(){
    var imagen = document.getElementById("imagen");
    if (imagen.style.opacity === "0"){
        imagen.style.opacity = "1";
    } else {
        imagen.style.opacity = "0";
    }
}