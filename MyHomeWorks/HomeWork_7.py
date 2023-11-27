# data_lst = ['1', '2', '3', '4d', 5]
# res_lst_1 = []
# res_lst_2 = []
# for item in data_lst:
#     try:
#         item = int(item)
#         res_lst_1 += str(item).split()
#
#     except ValueError:
#         res_lst_2 += str(item).split()
#
#     if res_lst_1:
#         print(f'Данные: {res_lst_1} являются числами')
#
# raise ValueError(f'Ошибка! Данные: {res_lst_2} не являются числами')


telefon_num = input('Введите номер телефона: ')
print(type(telefon_num))

telefon_num = telefon_num.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '').split(';')
# telefon_num += telefon_num.split(';')
for item in telefon_num:
    if len(item) < 11:
        raise ValueError(f'Ошибка! Введенный номер телефона {telefon_num} состоит не из 11 цифр!')
    if item[0] == '7' or '8':
        raise ValueError(f'Ошибка! Номер телефона {telefon_num} Начинается не с "8" и не с "+7"!')
    if item != item.isdigit():
        raise ValueError(f'Ошибка! ВВеденный номер телефона {telefon_num} состоит не из чисел!')
    if len(item) > 11:
        raise ValueError(f'Ошибка! Введенный номер телефона {telefon_num} содержит более 11 цифр!')
