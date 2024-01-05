import json

from cities import cities_list

cities_set = set()

for city in cities_list:
    cities_set.add(city['name'])

russian_letters_set = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

bad_letters = {'ь', 'ё', 'ъ', 'ы'}



#
# with open('cities.json', 'w', encoding='utf-8') as file:
#     json.dump(list(cities_set), file, ensure_ascii=False, indent=4)
#
# with open('cities.json', 'r', encoding='utf-8') as file:
#     cities_set = set(json.load(file))
#
#
# computer_city = None
#
# while cities_set:
#     humans_city = input('Введите название города: ').strip()
#     if humans_city == 'стоп':
#         print('Вы проиграли!')
#         break
#
#     if humans_city not in cities_set:
#         print('Такого города не существует! Вы проиграли!')
#         break
#
#     if computer_city:
#         if computer_city[-1].lower() != humans_city[0].lower():
#             print('Вы проиграли!')
#             break
#
#     cities_set.remove(humans_city)
#
#     print(f'Вы ввели: {humans_city}')
#
#     for city in cities_set:
#         if city[0].lower() == humans_city[-1].lower():
#             computer_city = city
#
#     cities_set.remove(computer_city)
#
#     print(f'Ход компьютера: {computer_city}')
#
# else:
#     print('Поздравляем! Вы выиграли!')


def get_cities_set_from_json(file_name: str = 'cities.json') -> set:
    """
    Функция читает json файл и возвращает сет городов
    :param file_name: По умолчанию 'cities.json
    :return: Сет городов
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        cities_set = set(json.load(file))

    return cities_set


def get_bad_startswith_letters(letters_set, cities_set) -> set:
    """
    Функция возвращает сет плохих первых букв
    :param letters_set: Сет букв для поиска
    :param cities_set: Сет городов для анализа
    :return: Сет плохих букв, с которых не начинаются города в cities_set
    """
    bad_startswith_letters: set = set()

    for letter in letters_set:
        if not any(city.startswith(letter.upper()) for city in cities_set):
            bad_startswith_letters.add(letter)

    return bad_startswith_letters


def check_bad_startswith_letters(city: str, bad_letters: set) -> bool:
    """
    Функция проверяет город и возвращает True, если он начинается на плохую букву
    :param city: Название города
    :param bad_letters: Сет плохих букв
    :return: bool
    """
    if city[0].lower() in bad_letters:
        return True
    else:
        return False


def check_main_game_rule(last_round_city: str, current_round_city: str) -> bool:
    """
    Функция принимает два города и проверяет, что первая буква города Current_round_city
    равна последней букве города Last_round_city
    :param last_round_city: Город из прошлого раунда
    :param current_round_city: Город из текущего раунда
    :return: bool
    """
    if last_round_city[-1].lower() == current_round_city[0].lower():
        return True
    else:
        return False


def computer_move(cities_set: set, last_round_city: str) -> str | None:
    """
    Функция принимает сет городов и город из прошлого раунда.
    Проходит циклом по сету, проверяя главное правило игры
    :param cities_set:
    :param last_round_city:
    :return:
    """
    for city in cities_set:
        if check_main_game_rule(last_round_city, city):
            return city
    else:
        return None


def main():
    cities_set = get_cities_set_from_json()

    bad_letters = get_bad_startswith_letters(russian_letters_set, cities_set)

    computer_city = None

    while cities_set:
        humans_city = input('Введите название города: ').strip()

        if humans_city == 'стоп':
            print('Вы проиграли!')
            break

        if humans_city not in cities_set:
            print('Такого города не существует! Вы проиграли!')
            break

        if computer_city:
            if not check_main_game_rule(computer_city, humans_city):
                print('Вы проиграли')
                break

        cities_set.remove(humans_city)

        print(f'Вы ввели: {humans_city}')

        computer_city = computer_move(cities_set, humans_city)

        if not computer_city:
            print('Вы выиграли!')
            break

        cities_set.remove(computer_city)
        print(f'Ход компьютера: {computer_city}')

    else:
        print('Поздравляем! Вы выиграли!')

main()
