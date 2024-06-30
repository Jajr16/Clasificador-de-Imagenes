document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var username = document.getElementById('username').value.trim();
    var password = document.getElementById('password').value.trim();

    if (username === '' || password === '') {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Por favor complete todos los campos.'
        });
    } else {
        setTimeout(function() {
            window.location.href = 'cargarFoto.html';
        }, 1000); 

        Swal.fire({
            icon: 'success',
            title: 'Inicio de sesión exitoso',
        });
    }
});
