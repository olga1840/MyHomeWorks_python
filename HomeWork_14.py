import csv

# Часть 1
password_input = input('Введите пароль: ')
def password_checker(func):
    def wrapper(password):
        #Проверяем длину пароля (не менее 8 символов):
        if len(password) < 8:
            return "Ошибка! Пароль должен состоять не менее чем из 8 символов!"

        # Проверяем наличие цифр:
        if not any(char.isdigit() for char in password):
            return "Ошибка! Пароль должен содержать хотя бы одну цифру!"

        # Проверяем наличие заглавной буквы:
        if not any(char.isupper() for char in password):
            return "Ошибка! Пароль должен содержать хотя бы одну заглавную букву!"

        # Проверяем наличие строчных букв:
        if not any(char.islower() for char in password):
            return "Ошибка! Пароль должен содержать хотя бы одну строчную букву!"

        # Проверяем наличие спецсимвола:
        if not any(char in "[!@#$%^&*((){}|\<>'" for char in password):
            return "Ошибка! Пароль должен содержать хотя бы один спецсимвол!"
        return func(password)
    return wrapper

@password_checker
def register_user(password):
    return "Поздравляем! Регистрация прошла успешно!"

result = register_user(password_input)
print(result)


# Часть 2

def password_validator(min_length=8, min_uppercase=1, min_lowercase=1, min_special_chars=1):
    def decorator(func):
        def wrapper(username, password):
            # Проверка длины пароля
            if len(password) < min_length:
                raise ValueError(f"Пароль должен быть не менее {min_length} символов")

            # Проверка количества букв верхнего регистра
            if sum(1 for char in password if char.isupper()) < min_uppercase:
                raise ValueError(f"Пароль должен содержать не менее {min_uppercase} букв верхнего регистра")

            # Проверка количества букв нижнего регистра
            if sum(1 for char in password if char.islower()) < min_lowercase:
                raise ValueError(f"Пароль должен содержать не менее {min_lowercase} букв нижнего регистра")

            # Проверка количества спец-знаков
            if sum(1 for char in password if not char.isalnum()) < min_special_chars:
                raise ValueError(f"Пароль должен содержать не менее {min_special_chars} спец-знаков")

            return func(username, password)
        return wrapper
    return decorator

def username_validator(func):
    def wrapper(username, password):
        # Проверка наличия пробелов в имени пользователя
        if ' ' in username:
            raise ValueError("Имя пользователя не должно содержать пробелов")

        return func(username, password)
    return wrapper

@password_validator()
@username_validator
def register_user(username, password):
    # Дозапись в CSV файл
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print(f"Пользователь {username} успешно зарегистрирован.")

try:
    register_user("user123", "Password123!")
except ValueError as e:
    print(f"Ошибка регистрации: {e}")
