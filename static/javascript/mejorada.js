document.addEventListener('DOMContentLoaded', function() {
    var volverBtn = document.getElementById('volver');
    var archivoBtn = document.getElementById('archivo');


    volverBtn.addEventListener('click', function() {
        window.location.href = 'cargarFoto.html';
    });

    archivoBtn.addEventListener('click', function() {
        window.location.href = 'proyectos.html';
    });
});
