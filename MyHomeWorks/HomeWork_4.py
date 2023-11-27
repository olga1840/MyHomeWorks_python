# Задача 1 - проверка телефона
telefon_num = input('Введите номер телефона: ')
replaced_telefon_num = telefon_num.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
num = len(replaced_telefon_num)
if replaced_telefon_num.isdigit() and num == 11 and replaced_telefon_num.startswith(
        '8') or replaced_telefon_num.startswith('7'):
    print(f'Ваш номер телефона {telefon_num} прошел проверку')
else:
    print('Ошибка: неверный формат ввода!')

# Задача 2 - проверка пароля на валидность
password_input = input('Введите пароль: ')
num = len(password_input)
if (password_input.isalnum() == True) or (password_input.islower() == True) or (
        password_input.isupper() == True) or num <= 7 or " " in password_input:
    print(f'Введенный пароль {password_input} не прошел проверку! Придумайте более надежный пароль!')
else:
    print(f'Ваш пароль {password_input} успешно прошел проверку!')
