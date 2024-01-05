import json
from typing import Set


class JsonFile:
    """
    Класс для работы с JSON файлами.
    Методы:
    - read_data() - чтение данных из JSON файла
    - write_data() - запись данных в JSON файл
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        """
        Чтение данных из JSON файла
        :return: данные из JSON файла
        """
        with open(self.file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    def write_data(self, data):
        """
        Запись данных в JSON файл
        :param data: данные для записи
        :return: None
        """
        with open(self.file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)


"""
1. Создаем Дата классы для города
2. Внедряем в Cities
"""


class Cities:
    """
    Класс для представлением данных о городах из JSON файла
    Метод:
    __init__(self, city_data) - конструктор класса
    """

    def __init__(self, city_data):
        self.city_data = city_data
        self.names_set = self.__get_names_set()

    def __get_names_set(self):
        """
        Получение множества названий городов
        :return: множество названий городов
        """
        names_set = set()
        for city in self.city_data:
            names_set.add(city['name'])
            return names_set


class CityGame:
    def __init__(self, cities: Cities):
        self.cities_obj = cities
        self.cities: Set[str] = self.cities_obj.names_set
        self.human_city: str = ''
        self.computer_city: str = ''

    @staticmethod
    def check_game_rules(last_city: str, new_city: str) -> bool:
        """
        Метод проверки правил игры.
        Возвращает True, если правила соблюдены, иначе False
        :param last_city: последний обозначенный город
        :param new_city: новый город
        :return:
        """
        if last_city[-1].lower() == new_city[0].lower():
            return True
        else:
            return False

    def human_step(self):
        """
        Метод для хода человека
        :return:
        """
        self.human_city = input('Введите название города: ')
        if self.human_city == 'стоп':
            print('Вы проиграли')
            return False
        if self.human_city not in self.cities:
            print(f'Города с названием {self.human_city} нет в списке городов. Вы проиграли!')
            return False

        if self.computer_city:
            if not self.check_game_rules(self.computer_city, self.human_city):
                print(f'Вы проиграли! Ваш ответ не начинается на букву {self.computer_city[-1]}')
                return False

            self.cities.remove(self.human_city)
            self.human_city = self.human_city
            return True

    def computer_step(self):
        """
        Метод для хода компьютера
        :return:
        """

        for city in self.cities:
            if self.check_game_rules(self.human_city, city):
                print(f'Ход компьютера: {city}')
                self.computer_city = city
                self.cities.remove(city)
                return True

            else:
                print('Вы победили!')
                return False


class GameManager:
    def __init__(self, json_file: JsonFile, cities: Cities, game: CityGame):
        self.json_file = json_file
        self.cities = cities
        self.game = game

    def __start__game(self):
        """
        Метод для начала игры
        :return:
        """

        while True:
            if not self.game.human_step():
                break
            if not self.game.computer_step():
                break

    def __call__(self):
        """
        Метод для запуска игры
        :return:
        """
        self.__start_game()
        print('Игра окончена')
        input('Нажмите Enter для выхода')


if __name__ == "__main__":
    # Создаем экземпляр класса JsonFile
    json_file = JsonFile("../cities_project/cities.json")
    # Создаем экземпляр класса Cities
    cities = Cities(json_file.read_data())
    # Создаем экземпляр класса CityGame
    game = CityGame(cities)
    # Создаем экземпляр класса GameManager
    game_manager = GameManager(json_file, cities, game)
    # Запускаем игру
    game_manager()
