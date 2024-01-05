from cities import cities_list
import random

# print(cities_list)

cities_set = []
for city in cities_list:
    cities_set.append(city['name'])
used_city = list(cities_set)
random.shuffle(cities_set)
random_city = used_city.pop()
print(random_city)

# cities_set2 = {item['name'] for item in cities_list}

# print(cities_set)
# print(len(cities_set2))

while True:
    user_answer = input('Введите название города: ')
    if user_answer == "стоп":
        print("Вы проиграли!")
    elif (user_answer.lower()[0] != random_city[-1]):
        print(f"Ошибка! Город должен начинаться с буквы '{random_city[-1]}: '!")
    elif user_answer not in cities_set:
        print(f"Ошибка! Города с названием '{user_answer}' нет!")
    elif user_answer not in used_city:
        print("Вы проиграли! Такой город уже называли!")

    else:
        used_city.remove(user_answer)
    for candidate in used_city:
        if candidate.lower()[0] == user_answer[-1]:
            random_city = candidate
            used_city.remove(candidate)
            print(candidate)
            break


