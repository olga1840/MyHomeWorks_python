import csv
import json

class CsvFileHandler:
    def read_file(self, filepath, as_dict=False):
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file) if as_dict else csv.reader(file)
            return [row for row in reader]

    def write_file(self, filepath, data, as_dict=False):
        with open(filepath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys()) if as_dict else csv.writer(file)
            writer.writeheader() if as_dict else None
            writer.writerows(data)

    def append_file(self, filepath, data, as_dict=False):
        with open(filepath, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys()) if as_dict else csv.writer(file)
            writer.writerows(data)

class JsonFileHandler:
    def read_file(self, filepath, as_dict=False):
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data if as_dict else [list(row.values()) for row in data]

    def write_file(self, filepath, data, as_dict=False):
        with open(filepath, 'w') as file:
            if as_dict:
                json.dump(data, file, indent=2)
            else:
                json.dump([dict(zip(map(str, range(1, len(row) + 1)), row)) for row in data], file, indent=2)

    def append_file(self, filepath, data):
        raise TypeError("JSON file does not support append operation.")

class TxtFileHandler:
    def read_file(self, filepath):
        with open(filepath, 'r') as file:
            return file.readlines()

    def write_file(self, filepath, data):
        with open(filepath, 'w') as file:
            file.writelines(data)

    def append_file(self, filepath, data):
        with open(filepath, 'a') as file:
            file.writelines(data)

# Пример использования:
csv_handler = CsvFileHandler()
json_handler = JsonFileHandler()
txt_handler = TxtFileHandler()

# Чтение данных из файлов
csv_data = csv_handler.read_file('example.csv', as_dict=True)
json_data = json_handler.read_file('example.json', as_dict=True)
txt_data = txt_handler.read_file('example.txt')

# Запись данных в файлы
csv_handler.write_file('output.csv', csv_data, as_dict=True)
json_handler.write_file('output.json', json_data, as_dict=True)
txt_handler.write_file('output.txt', txt_data)

# Дописывание данных в файлы
csv_handler.append_file('output.csv', csv_data, as_dict=True)
# json_handler.append_file('output.json', json_data)  # TypeError: JSON file does not support append operation.
txt_handler.append_file('output.txt', ['New line 1\n', 'New line 2\n'])