document.addEventListener('DOMContentLoaded', function() {
    var cerrarSesionBtn = document.getElementById('cerrarSesion');
    var procesarBtn = document.getElementById('Procesar');


    cerrarSesionBtn.addEventListener('click', function() {
        Swal.fire({
            title: 'Cerrar Sesión',
            text: '¡Has cerrado sesión correctamente!',
            icon: 'success',
            timer: 1500, 
            showConfirmButton: false 
        }).then(() => {
            window.location.href = 'login.html';
        });
    });

    procesarBtn.addEventListener('click', function() {
        window.location.href = 'mejorada.html';
    });
});
