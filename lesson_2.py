# name = input('Введите Ваше имя: ')
# print(name)
# # type_name = type(name)
# print(type(name))

# integer = input('Введите целое число: ')
# integer = int(integer)
# print(type(integer))
# print()

# int_credit = input('Введите сумму кредита: ')
# int_st = input('Введите годовую ставку в процентах: ')
# int_time = input('Введите срок кредита в количестве месяцев: ')
# res = int(int_credit)/100*int(int_st)*int(int_time)
# print('Сумма выплат по процентам составляет: ', res)

int_credit = int(input('Введите сумму кредита: '))
int_st = int(input('Введите годовую ставку в процентах: '))
int_time = int(input('Введите срок кредита в количестве месяцев: '))
res = int_credit/100*int_st*int_time
print('Сумма выплат по процентам составляет: ', res)

