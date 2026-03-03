document.addEventListener('DOMContentLoaded', function() {
    var phoneInput = document.querySelector('.telephone');

    if (!phoneInput) return;

    // Функция для форматирования номера
    function formatPhoneNumber(value) {
        // Удаляем все нецифровые символы
        var digits = value.replace(/\D/g, '');

        // Ограничиваем количество цифр (11 для российских номеров)
        digits = digits.slice(0, 11);

        // Форматируем в зависимости от количества цифр
        var formatted = '';

        if (digits.length > 0) {
            formatted = '+7';

            if (digits.length > 1) {
                formatted += ' (' + digits.slice(1, 4);
            } else {
                formatted += ' (';
            }

            if (digits.length >= 4) {
                formatted += ') ' + digits.slice(4, 7);
            } else if (digits.length > 1) {
                formatted += ') ';
            }

            if (digits.length >= 7) {
                formatted += '-' + digits.slice(7, 9);
            }

            if (digits.length >= 9) {
                formatted += '-' + digits.slice(9, 11);
            }
        }

        return formatted;
    }

    // Обработка ввода
    phoneInput.addEventListener('input', function(e) {
        var cursorPosition = this.selectionStart;
        var oldValue = this.value;
        var newValue = formatPhoneNumber(this.value);

        if (oldValue !== newValue) {
            this.value = newValue;

            // Корректируем позицию курсора
            var newCursorPosition = cursorPosition + newValue.length - oldValue.length;
//            if (newValue.length > oldValue.length) {
//                newCursorPosition++;
//            } else if (newValue.length < oldValue.length) {
//                newCursorPosition--;
//            }

            // Устанавливаем курсор в правильное место
            this.setSelectionRange(newCursorPosition, newCursorPosition);
        }
    });

    // Блокировка ввода нецифровых символов на уровне клавиатуры
    phoneInput.addEventListener('keydown', function(e) {
        var key = e.key;

        // Разрешаем управляющие клавиши
        var controlKeys = [
            'Backspace', 'Delete', 'Tab', 'Enter',
            'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown',
            'Home', 'End', 'Ctrl', 'Alt', 'Shift', 'Meta'
        ];

        if (controlKeys.includes(key) || e.ctrlKey || e.metaKey) {
            return true; // Разрешаем
        }

        // Разрешаем только цифры
        if (key.length === 1 && !/[0-9]/.test(key)) {
            e.preventDefault();
            return false;
        }
    });

    // Обработка вставки из буфера обмена
    phoneInput.addEventListener('paste', function(e) {
        e.preventDefault();

        // Получаем текст из буфера обмена
        var pastedText = (e.clipboardData || window.clipboardData).getData('text');

        // Удаляем все нецифровые символы
        var digits = pastedText.replace(/\D/g, '');

        // Добавляем к существующему значению
        var currentDigits = this.value.replace(/\D/g, '');
        var newDigits = (currentDigits + digits).slice(0, 11);

        // Создаем новое значение
        var newValue = formatPhoneNumber(newDigits);

        // Устанавливаем новое значение
        this.value = newValue;

        // Устанавливаем курсор в конец
        this.setSelectionRange(newValue.length, newValue.length);
    });

    // Автоматически показывать маску при фокусе
    phoneInput.addEventListener('focus', function() {
        if (!this.value) {
            this.value = '+7 ';
        }
    });
});