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
        
        // Realizar una solicitud AJAX para validar las credenciales
        fetch('', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: new URLSearchParams({
                'username': usuario,
                'password': contraseña
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.valid) {
                alert("Validación exitosa.");
                window.location.href = urlIndex;
            } else {
                alert("Usuario o contraseña incorrectos.");
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    
    // Enlazar la función de validación al evento onsubmit del formulario
    document.querySelector('.form').addEventListener('submit', validarDatos);
});