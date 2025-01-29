function validarRegistro() {
  var nombres = document.getElementById("nombres").value;
  var apellidos = document.getElementById("apellidos").value;
  var email = document.getElementById("email").value;
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var confirmPassword = document.getElementById("confirm_password").value;
  var roles = document.getElementById("roles").value;

  if (!nombres || !apellidos || !email || !username || !password || !confirmPassword || !roles) {
    alert("Todos los campos son obligatorios.");
    return false;
  }

  if (password !== confirmPassword) {
    alert("Las contraseñas no coinciden.");
    return false;
  }
  return true; 
}