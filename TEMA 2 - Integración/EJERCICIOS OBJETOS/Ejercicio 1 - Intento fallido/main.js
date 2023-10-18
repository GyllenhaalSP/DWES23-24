function resetear() {
    document.getElementById("resetear").addEventListener("click", function () {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "session_reset.php", true);
        xhr.send();

        xhr.onload = function () {
            if (xhr.status === 200) {
                const checkSession = new XMLHttpRequest();
                checkSession.open("GET", "check_session.php", true);
                checkSession.send();

                checkSession.onload = function () {
                    if (checkSession.status === 200 && checkSession.responseText === "success") {
                        location.reload();
                    } else {
                        alert("Error al reiniciar la sesión");
                    }
                };
            } else {
                alert("Error al resetear la sesión '" + xhr.status + " : " + xhr.statusText + "'");
            }
        };
    });
}