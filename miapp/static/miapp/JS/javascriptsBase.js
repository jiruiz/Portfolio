
document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.navbar-burger');
    const menu = document.querySelector('.navbar-menu');
    const dropdowns = document.querySelectorAll('.navbar-item.has-dropdown');
    const links = document.querySelectorAll('.navbar-menu .navbar-item a');

    // Función para cerrar el navbar
    const closeNavbar = () => {
        burger.classList.remove('is-active');
        menu.classList.remove('is-active');
    };

    // Toggle del menú hamburguesa
    if (burger && menu) {
        burger.addEventListener('click', () => {
            menu.classList.toggle('is-active');
            burger.classList.toggle('is-active');
        });
    }

    // Cerrar el navbar cuando se haga clic en cualquier enlace dentro de él (excepto en los dropdowns)
    links.forEach(link => {
        link.addEventListener('click', (event) => {
            if (!link.closest('.has-dropdown')) { // Evita cerrar si el enlace está en un dropdown
                closeNavbar();
            }
        });
    });

    // Habilitar el toggle independiente para cada dropdown
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', (event) => {
            event.stopPropagation(); // Evita que se propague y cierre el navbar
            dropdown.classList.toggle('is-active');
        });
    });

    // Cerrar el navbar cuando se haga clic fuera
    document.addEventListener('click', (event) => {
        if (!menu.contains(event.target) && !burger.contains(event.target)) {
            closeNavbar();
        }
    });
});












document.getElementById("contactForm").addEventListener("submit", function (event) {
    event.preventDefault();
    document.getElementById("successMsg").style.display = "block";
});

const scrollTopBtn = document.getElementById("scrollTopBtn");
window.onscroll = function () {
    scrollTopBtn.style.display = window.scrollY > 200 ? "block" : "none";
};
scrollTopBtn.onclick = function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
};






const text = "Bienvenido a mi sitio web personal.";
let index = 0;
let isDeleting = false;

function typeEffect() {
    const element = document.getElementById("typing-effect");

    if (!isDeleting) {
        if (index < text.length) {
            element.innerHTML += text.charAt(index);
            index++;
            setTimeout(typeEffect, 100);
        } else {
            isDeleting = true;
            setTimeout(typeEffect, 3000); // Espera 3 segundos antes de borrar
        }
    } else {
        if (index > 0) {
            element.innerHTML = text.substring(0, index - 1);
            index--;
            setTimeout(typeEffect, 50);
        } else {
            isDeleting = false;
            setTimeout(typeEffect, 500); // Espera un poco antes de volver a escribir
        }
    }
}

document.addEventListener("DOMContentLoaded", typeEffect);













let lastScrollTop = 0;
const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", function () {
    let scrollTop = window.scrollY || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
        // Oculta la navbar cuando el usuario baja
        navbar.style.top = "-70px"; /* Ajusta la altura según tu navbar */
    } else {
        // Muestra la navbar cuando el usuario sube
        navbar.style.top = "0";
    }

    lastScrollTop = scrollTop;
});






// Función para mostrar el navbar cuando el mouse se mueve cerca de la parte superior
document.addEventListener('mousemove', function (e) {
    const navbar = document.getElementById('navbar');
    if (e.clientY < 50) {
        navbar.classList.add('show');
    } else {
        navbar.classList.remove('show');
    }
});

// Función para mostrar el navbar cuando se toca la parte superior en pantallas táctiles
document.addEventListener('touchstart', function (e) {
    const navbar = document.getElementById('navbar');
    if (e.touches[0].clientY < 50) {
        navbar.classList.add('show');
    } else {
        navbar.classList.remove('show');
    }
});
