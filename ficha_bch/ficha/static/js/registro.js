function validarRegistro() {
  var nombres = document.getElementById("nombres").value.trim();
  var apellidos = document.getElementById("apellidos").value.trim();
  var email = document.getElementById("email").value.trim();
  var username = document.getElementById("username").value.trim();
  var password = document.getElementById("password").value.trim();
  var password2 = document.getElementById("password2").value.trim();
  var roles = document.getElementById("roles").value.trim();

  if (!nombres || !apellidos || !email || !username || !password || !password2 || !roles) {
    alert("Todos los campos son obligatorios y no deben contener solo espacios en blanco.");
    return false;
  }

  if (password !== password2) {
    alert("Las contraseñas no coinciden.");
    return false;
  }

  return true;
}