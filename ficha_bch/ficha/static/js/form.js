document.addEventListener('DOMContentLoaded', function() {
    const codigoOficinaElement = document.getElementById('codigo-oficina');
    if (codigoOficinaElement) {
        codigoOficinaElement.addEventListener('change', fetchAndFillData);
        codigoOficinaElement.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault(); // Evitar que el formulario se envíe
                fetchAndFillData();
            }
        });
    } else {
        console.error('Elemento con ID "codigo-oficina" no encontrado.');
    }

    const rutElement = document.getElementById('rut');
    if (rutElement) {
        rutElement.addEventListener('change', fetchAndFillData);
    } else {
        console.error('Elemento con ID "rut" no encontrado.');
    }

    document.querySelector('form').addEventListener('submit', function(event) {
        let isValid = true;

        // Validar Código Oficina
        const codigoOficina = document.getElementById('codigo-oficina').value;
        if (codigoOficina.trim() === '') {
            alert('El Código Oficina es obligatorio.');
            isValid = false;
        }

        // Validar Rut
        const rut = document.getElementById('rut').value;
        if (rut === '') {
            alert('Debe seleccionar un Rut.');
            isValid = false;
        }

        // Validar Ejec. Responsable
        const ejecResponsable = document.getElementById('ejec-responsable').value;
        if (ejecResponsable.trim() === '') {
            alert('El Ejec. Responsable es obligatorio.');
            isValid = false;
        }

        // Validar Login Creador
        const loginCreador = document.getElementById('login-creador').value;
        if (loginCreador.trim() === '') {
            alert('El Login Creador es obligatorio.');
            isValid = false;
        }

        // Validar Tipo de Cliente
        const tipoCliente = document.getElementById('tipo-cliente').value;
        if (tipoCliente === '') {
            alert('Debe seleccionar un Tipo de Cliente.');
            isValid = false;
        }

        // Validar Sucursal
        const sucursal = document.getElementById('sucursal').value;
        if (sucursal.trim() === '') {
            alert('La Sucursal es obligatoria.');
            isValid = false;
        }

        // Validar Producto
        const producto = document.getElementById('producto').value;
        if (producto.trim() === '') {
            alert('El Producto es obligatorio.');
            isValid = false;
        }

        // Validar M. Solicitado
        const mSolicitado = document.getElementById('m-solicitado').value;
        if (mSolicitado.trim() === '') {
            alert('El M. Solicitado es obligatorio.');
            isValid = false;
        }

        // Validar Rut Modificar
        const rutModificar = document.getElementById('rut-modificar').value;
        if (rutModificar === '') {
            alert('Debe seleccionar un Rut Modificar.');
            isValid = false;
        }

        // Validar Revisión N°
        const revisionNumero = document.getElementById('revision-numero').value;
        if (revisionNumero.trim() === '') {
            alert('La Revisión N° es obligatoria.');
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
        }
    });
});

function fetchAndFillData() {
    const codigoOficina = document.getElementById('codigo-oficina').value;
    const rut = document.getElementById('rut').value;

    if (codigoOficina && rut) {
        fetch(`/api/get-data/?codigo_oficina=${codigoOficina}&rut=${rut}`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById('ejec-responsable').value = data.ejec_responsable;
                    document.getElementById('login-creador').value = data.login_creador;
                    document.getElementById('tipo-cliente').value = data.tipo_cliente;
                    document.getElementById('sucursal').value = data.sucursal;
                    document.getElementById('producto').value = data.producto;
                    document.getElementById('m-solicitado').value = data.m_solicitado;
                    document.getElementById('rut-modificar').value = data.rut_modificar;
                    document.getElementById('revision-numero').value = data.revision_numero;
                } else {
                    alert('No se encontraron datos para los filtros proporcionados.');
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                alert('Hubo un error al obtener los datos.');
            });
    }
}