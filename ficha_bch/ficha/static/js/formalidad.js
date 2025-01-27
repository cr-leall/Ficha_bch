function validateForm() {
    var valid = true;

    // Verificación Laboral
    var verificacionLaboral = document.getElementById("respuesta-verificacion-laboral").value;
    if (verificacionLaboral === "") {
        alert("Por favor, seleccione una opción para Verificación Laboral.");
        valid = false;
    }

    // Estado de Situación
    var estadoSituacion = document.getElementById("respuesta-estado-situacion").value;
    if (estadoSituacion === "") {
        alert("Por favor, seleccione una opción para Estado de Situación.");
        valid = false;
    }


    return valid;
}
