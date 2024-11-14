// JavaScript básico para desplazamiento automático
let currentIndex = 0;
const slides = document.querySelectorAll("#slider input");
const numSlides = slides.length;

function nextSlide() {
    currentIndex = (currentIndex + 1) % numSlides;
    slides[currentIndex].checked = true;
}

setInterval(nextSlide, 3000); // Cambia cada 3 segundos
