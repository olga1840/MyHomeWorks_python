# from marvel import full_dict
from marvel import small_dict

# print(full_dict)

# stage_dict = {
#     1: "Первая фаза",
#     2: "Вторая фаза",
#     3: "Третья фаза",
#     4: "Четвёртая фаза",
#     5: "Пятая фаза",
#     6: "Шестая фаза",
# }
#
# input_stage = input('Введите цифру, соответствующую фазе: ')
# if not input_stage.isdigit():
#     raise TypeError('Вы ввели не число!')
# user_stage = int(input_stage)
# if user_stage not in stage_dict.keys():
#     raise ValueError('Такой фазы не существует!')
# stage_str = stage_dict[user_stage]
# result_list = {film_dict['title'] for film, film_dict in full_dict.items() if film_dict['stage'] == stage_str}
# print(result_list)

# result = []
# for title, year in small_dict.items():
#     if year == 2023:
#         result.append(title)
# pprint(result)
result = [film for film, year in small_dict.items() if year ==2023]
print(result)