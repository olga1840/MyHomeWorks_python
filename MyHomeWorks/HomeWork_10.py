from cities import cities_list
import random
import time
from typing import List, Callable, Any

# cities_set = []
# for city in cities_list:
#   cities_set.append(city['name'])
# used_city = list(cities_set)
# random.shuffle(cities_set)
# random_city = used_city.pop()
# print(random_city)
# if city['name'][-1].lower() not in 'ьъы':
#     cities_set.append(city['name'])
#
# import json
#
# with open('cities.json', 'w', encoding='UTF-8') as file:
#     json.dump(list(cities_set), file, ensure_ascii=False, indent=4)
# with open('cities.json', 'r', encoding='UTF-8') as file:
#     cities_set = set(json.load(file))
#
# while True:
#     user_answer = input('Введите название города: ')
#     if user_answer == "стоп":
#         print("Вы проиграли!")
#     elif (user_answer.lower()[0] != random_city[-1]):
#         print(f"Ошибка! Город должен начинаться с буквы '{random_city[-1]}: '!")
#     elif user_answer not in cities_set:
#         print(f"Ошибка! Города с названием '{user_answer}' нет!")
#     elif user_answer not in used_city:
#         print("Вы проиграли! Такой город уже называли!")
#
#     else:
#         used_city.remove(user_answer)
#     for candidate in used_city:
#         if candidate.lower()[0] == user_answer[-1]:
#             random_city = candidate
#             used_city.remove(candidate)
#             print(candidate)
#             break


def check_time_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        finish_time = time.perf_counter()
        result_time = finish_time - start_time
        print(f'Прошло {result_time:.10f} секунд')
    return wrapper


@check_time_decorator
def get_city_by_letter_in_for(letter: str) -> List[str]:
    result_list: List[str] = []
    for city in cities_list:
        if letter in city:
            result_list.append(city)
    return result_list

@check_time_decorator
def get_city_by_letter_in_comprehension(letter: str) -> List[str]:
    return [city for city in cities_list if letter in city]

get_city_by_letter_in_for('а')
get_city_by_letter_in_comprehension('а')

