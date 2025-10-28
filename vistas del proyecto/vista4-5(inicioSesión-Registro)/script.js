// ...existing code...
document.addEventListener('DOMContentLoaded', () => {
    const btnLogin = document.getElementById('show-login');
    const btnRegister = document.getElementById('show-register');
    const formLogin = document.getElementById('form-login');
    const formRegister = document.getElementById('form-register');

    function showLogin() {
    formRegister.classList.add('hidden');
    formRegister.setAttribute('aria-hidden', 'true');
    formLogin.classList.remove('hidden');
    formLogin.removeAttribute('aria-hidden');
    formLogin.querySelector('input, button')?.focus();
    }

    function showRegister() {
    formLogin.classList.add('hidden');
    formLogin.setAttribute('aria-hidden', 'true');
    formRegister.classList.remove('hidden');
    formRegister.removeAttribute('aria-hidden');
    formRegister.querySelector('input')?.focus();
    }

    btnLogin.addEventListener('click', showLogin);
    btnRegister.addEventListener('click', showRegister);
});
// ...existing code...