document.addEventListener('DOMContentLoaded', function() {
    function navegarPilar() {
        var select = document.getElementById('pilar-select');
        var url = select.value;

        if (url) {
            window.location.href = url;
        }
    }
    // Enlazar la función de navegación al evento onchange del select
    document.getElementById('pilar-select').addEventListener('change', navegarPilar);
});
