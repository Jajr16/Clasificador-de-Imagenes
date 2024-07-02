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
        const enhancedImage = document.getElementById('enhanced-image');
        enhancedImage.src = url;
        enhancedImage.style.display = 'block';

        // Configurar la descarga al hacer clic en el botón
        const downloadBtn = document.getElementById('download-btn');
        downloadBtn.style.visibility = 'visible';
        downloadBtn.addEventListener('click', () => {
            const a = document.createElement('a');
            a.href = url;
            a.download = 'imagen_mejorada.jpg';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        });

        // Funcionalidad de zoom
        const range = document.getElementById('zoom-range');
        range.addEventListener('input', (event) => {
            const scale = event.target.value;
            enhancedImage.style.transform = `scale(${scale})`;
            originalImage.style.transform = `scale(${scale})`;
        });
    } else {
        alert('Error al mejorar la foto');
    }
});
