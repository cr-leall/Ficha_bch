document.addEventListener('DOMContentLoaded', function() {
    function validateForm(event) {
        event.preventDefault();
        var valid = true; 
        var verificacionLaboral = document.getElementById("respuesta-verificacion-laboral").value;
        var tipoErrorVerificacionLaboral = document.querySelector('select[name="tipo-error-verificacion-laboral"]').value;
        if (verificacionLaboral === "") {
            alert("Por favor, seleccione una opción para Verificación Laboral.");
            valid = false;
        } else if (verificacionLaboral === "error" && tipoErrorVerificacionLaboral === "") {
            alert("Por favor, seleccione un tipo de error para Verificación Laboral.");
            valid = false;
        }

        var estadoSituacion = document.getElementById("respuesta-estado-situacion").value;
        var tipoErrorEstadoSituacion = document.querySelector('select[name="tipo-error-estado-situacion"]').value;
        if (estadoSituacion === "") {
            alert("Por favor, seleccione una opción para Estado de Situación.");
            valid = false;
        } else if (estadoSituacion === "error" && tipoErrorEstadoSituacion === "") {
            alert("Por favor, seleccione un tipo de error para Estado de Situación.");
            valid = false;
        }

        var acreditacionIngresos = document.getElementById("respuesta-acreditacion-ingresos").value;
        var tipoErrorAcreditacionIngresos = document.querySelector('select[name="tipo-error-acreditacion-ingresos"]').value;
        if (acreditacionIngresos === "") {
            alert("Por favor, seleccione una opción para Acreditación de Ingresos.");
            valid = false;
        } else if (acreditacionIngresos === "error" && tipoErrorAcreditacionIngresos === "") {
            alert("Por favor, seleccione un tipo de error para Acreditación de Ingresos.");
            valid = false;
        }

        if (valid) {
            document.querySelector('#form-evaluacion').submit(); // Enviar el formulario si todo es válido
        }

        return valid;
    }

    document.querySelector('#form-evaluacion').addEventListener('submit', validateForm);    
});
