// Гамбургер-меню

const hamburgerBtn = document.getElementById('hamburgerBtn');
const dropdownMenu = document.getElementById('dropdownMenu');

// Функция переключения меню
function toggleMenu() {
    dropdownMenu.classList.toggle('show');
    hamburgerBtn.classList.toggle('active');
}

// Открытие/закрытие меню по клику на кнопку
hamburgerBtn.addEventListener('click', function(event) {
    event.stopPropagation(); // Предотвращаем всплытие события
    toggleMenu();
});

// Закрытие меню при клике вне его области
document.addEventListener('click', function(event) {
    if (!hamburgerBtn.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.classList.remove('show');
        hamburgerBtn.classList.remove('active');
    }
});

// Закрытие меню при клике на пункт меню (опционально)
dropdownMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function() {
        dropdownMenu.classList.remove('show');
        hamburgerBtn.classList.remove('active');
    });
});