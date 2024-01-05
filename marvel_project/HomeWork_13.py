from marvel import full_dict


from pprint import pprint
from typing import List, Dict, Any, Callable

# 1-2
user_nums: List[str] = input('Введите числа через пробел: ').split(' ')
user_input_int: List[int | None] = list(map(lambda x: int(x) if x.isdigit() else None, user_nums))
pprint(f'Задание 2 выполнено: {user_input_int}')

# 3
filtered_id: dict = dict(filter(lambda x: x[0] in user_input_int, full_dict.items()))
print('Задание 3 выполнено:')
pprint(filtered_id)

# 4
dir_set_comprehension: set = {movie['director'] for movie in full_dict.values()}
print('Задание 4 выполнено:')
pprint(dir_set_comprehension)

# 5
dict_comprehension: Dict[int, Dict[str, str]] = {key:
                                                     {'title': value['title'],
                                                      'year': str(value['year']),
                                                      'director': value['director'],
                                                      'stage': value['stage']}
                                                 for key, value in full_dict.items()}
print('Задание 5 выполнено:')
pprint(dict_comprehension)

# 6
filtered_ch: Dict[int, Dict[str, Any]] = dict(filter(lambda x: x[1]['title'].startswith('Ч'), full_dict.items()))
print('Задание 6 выполнено:')
pprint(filtered_ch)

# 7 сортируем по одном параметру - названию фильма
sorted_title: Dict[int, Dict[str, str | int]] = dict(sorted(full_dict.items(), key=lambda x: x[1]['title']))
print('Задание 7 выполнено:')
pprint(sorted_title, sort_dicts=False)

# 8 сортируем по двум параметрам - году выпуска фильма и по названию
sorted_year_title: Dict[int, Dict[str, str | int]] = dict(
    sorted(full_dict.items(), key=lambda x: (x[1]['year'], x[1]['title'])))
print('Задание 8 выполнено:')
pprint(sorted_year_title, sort_dicts=False)
