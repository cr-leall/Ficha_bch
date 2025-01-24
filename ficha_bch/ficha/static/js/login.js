function ValidarDatos(){
    const formulario = document.getElementById('form');
    if (formulario.checkValidity()){
        window.open('index.html', '_blank');
    }else{
        alert('Por favor, completo todos los cambos requeridos.');
    }
} 
