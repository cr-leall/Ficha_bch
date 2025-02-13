document.addEventListener('DOMContentLoaded', function() {
    function validarDatos(event) {
        event.preventDefault(); // Prevenir el envío del formulario por defecto
        
        var usuario = document.getElementById("username").value;
        var contraseña = document.getElementById("password").value;
        
        // Validar campos no vacíos
        if (usuario === "" || contraseña === "") {
            alert("Por favor, complete todos los campos.");
            return false;
        }
    }})