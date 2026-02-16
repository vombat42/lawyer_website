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



// Меню контактов

const floatingBtn = document.getElementById('contactBtn');
const floatingContent = document.getElementById('contactList');

// Открытие/закрытие меню
floatingBtn.addEventListener('click', function(event) {
    event.stopPropagation();
    floatingContent.classList.toggle('show');
    floatingBtn.classList.toggle('active');
});

// Закрытие при клике на пункт меню
floatingContent.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function() {
        floatingContent.classList.remove('show');
        floatingBtn.classList.remove('active');
    });
});

// Закрытие при клике вне меню
document.addEventListener('click', function(event) {
    if (!floatingBtn.contains(event.target) && !floatingContent.contains(event.target)) {
        floatingContent.classList.remove('show');
        floatingBtn.classList.remove('active');
    }
});



// Кнопка ВВЕРХ

const btnUp = {
  el: document.querySelector('.btn-up'),
  show() {
    // удалим у кнопки класс btn-up_hide
    this.el.classList.remove('btn-up_hide');
  },
  hide() {
    // добавим к кнопке класс btn-up_hide
    this.el.classList.add('btn-up_hide');
  },
  addEventListener() {
    // при прокрутке содержимого страницы
    window.addEventListener('scroll', () => {
      // определяем величину прокрутки
      const scrollY = window.scrollY || document.documentElement.scrollTop;
      // если страница прокручена больше чем на 400px, то делаем кнопку видимой, иначе скрываем
      scrollY > 400 ? this.show() : this.hide();
    });
    // при нажатии на кнопку .btn-up
    document.querySelector('.btn-up').onclick = () => {
      // переместим в начало страницы
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
      });
    }
  }
}

btnUp.addEventListener();