var modal = document.getElementById("myModal");
var modalImg = document.getElementById("img01");
var images = document.querySelectorAll(".modal-img");
var span = document.getElementsByClassName("close")[0];

images.forEach(image => {
    image.onclick = function () {
        modal.style.display = "flex";
        modalImg.src = this.src;
    }
});

span.onclick = function () {
    modal.style.display = "none";
}

modal.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}

modalImg.onclick = function () {
    if (this.classList.contains('zoomed')) {
        this.classList.remove('zoomed');
    } else {
        this.classList.add('zoomed');
    }
}