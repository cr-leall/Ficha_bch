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
        
        // Validación personalizada (puedes añadir más reglas)
        if (usuario === "Admin" && contraseña === "123456") {
            alert("Validación exitosa.");
            // Redirigir a otra vista usando la variable de URL
            window.location.href = urlIndex;
        } else {
            alert("Usuario o contraseña incorrectos.");
        }
    }
    
    // Enlazar la función de validación al evento onsubmit del formulario
    document.querySelector('.form').addEventListener('submit', validarDatos);
});
