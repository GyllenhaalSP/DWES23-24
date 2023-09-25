function revelar() {
    const resultadoDiv = document.getElementById("resultado");
    if (resultadoDiv.style.display === "none" || resultadoDiv.style.display === "") {
        resultadoDiv.style.display = "block";
    }
}