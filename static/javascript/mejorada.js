document.getElementById('upload-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData();
    const fileInput = document.getElementById('file-input');
    formData.append('image', fileInput.files[0]);

    const originalImage = document.getElementById('original-image');
    originalImage.src = URL.createObjectURL(fileInput.files[0]);
    originalImage.style.display = 'block';

    const response = await fetch('/mejorar', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        const img = document.getElementById('enhanced-image');
        img.src = url;
        img.style.display = 'block';

        // Configurar la descarga al hacer clic en el botón
        const downloadBtn = document.getElementById('download-btn');
        downloadBtn.style.visibility = 'visible'
        downloadBtn.addEventListener('click', () => {
            const a = document.createElement('a');
            a.href = url;
            a.download = 'imagen_mejorada.jpg';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        });
    } else {
        alert('Error al mejorar la foto');
    }
});