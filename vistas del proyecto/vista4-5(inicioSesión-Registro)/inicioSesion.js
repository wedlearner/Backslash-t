// ...existing code...
document.addEventListener('DOMContentLoaded', () => {
    const btnLogin = document.getElementById('show-login');
    const btnRegister = document.getElementById('show-register');
    const formLogin = document.getElementById('form-login');
    const formRegister = document.getElementById('form-register');
    const headLogin = document.getElementById('head-login');
    const headRegister = document.getElementById('head-register');

    function showLogin() {
    formRegister.classList.add('hidden');
    formRegister.setAttribute('aria-hidden', 'true');
    formLogin.classList.remove('hidden');
    formLogin.removeAttribute('aria-hidden');
    formLogin.querySelector('input, button')?.focus();
    headLogin.classList.remove('hidden');
    headRegister.classList.add('hidden');
    }

    function showRegister() {
    formLogin.classList.add('hidden');
    formLogin.setAttribute('aria-hidden', 'true');
    formRegister.classList.remove('hidden');
    formRegister.removeAttribute('aria-hidden');
    formRegister.querySelector('input')?.focus();
    headRegister.classList.remove('hidden');
    headLogin.classList.add('hidden');
    }

    btnLogin.addEventListener('click', showLogin);
    btnRegister.addEventListener('click', showRegister);


    document.querySelectorAll('.form-submit-link').forEach(link => {
        link.addEventListener('click', (e) => {
        e.preventDefault(); // prevenir navegación inmediata
            const targetFormId = link.dataset.target;
            const form = document.getElementById(targetFormId);

            if (!form) {
            // si no existe el form, navegar normalmente
            window.location.href = link.href;
            return;
            }

        // opcional: validar con reportValidity antes de enviar
            if (typeof form.reportValidity === 'function' && !form.reportValidity()) {
            return; // hay campos inválidos
            }

        // asignar el action del form a la href del enlace y enviar
            form.action = link.href;
        // si quieres método POST explícito:
        // form.method = 'post';
            form.submit();
        });
    });
});
// ...existing code...