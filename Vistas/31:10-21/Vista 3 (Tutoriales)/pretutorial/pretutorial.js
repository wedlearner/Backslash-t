document.querySelectorAll('.desplegable').forEach(boton => {
    boton.addEventListener('click', () => {
        const submenu = boton.nextElementSibling;
        submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';
    });
});