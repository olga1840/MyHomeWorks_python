# palindrome = input('Введите слово: ')
# if palindrome.lower() == palindrome[::-1]:
#     print(f'Слово {palindrome} является палиндромом')
#
# else:
#     print(f'Слово {palindrome} не является палиндромом')


first_string = """
Скажи ка дядя ведь недаром
Москва, спаленная пожаром,
Французу отдана?
"""
sub_string = input('Введите слово: ')
num = first_string.count(sub_string)
index = first_string.find(sub_string)
if num > 0:
    print(f'Слово {sub_string} встречается в строке: {num} раз')
    print(f'Первое вхождение {sub_string}  в строке начинается с индекса: {index}')
else:
    print(f'Слово {sub_string} не встречается в строке')
