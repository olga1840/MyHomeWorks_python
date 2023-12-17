from abc import ABC, abstractmethod


# Часть 1

# Абстрактный класс Умное устройство
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_state(self):
        pass

# Класс Умная лампочка
class SmartBulb(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.state = False
        self.brightness = 0

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def get_state(self):
        return f"{self.name} is {'on' if self.state else 'off'}, brightness: {self.brightness}"

    def adjust_brightness(self, value):
        self.brightness = value

# Класс Умный датчик дыма
class SmartSmokeDetector(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.state = False

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def get_state(self):
        return f"{self.name} is {'on' if self.state else 'off'}"

    def check_smoke(self):
        # Логика проверки дыма
        pass

# Класс Умный увлажнитель воздуха
class SmartHumidifier(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.state = False
        self.humidity_level = 0

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def get_state(self):
        return f"{self.name} is {'on' if self.state else 'off'}, humidity level: {self.humidity_level}"

    def set_humidity(self, level):
        self.humidity_level = level


# Часть 2
# Миксин для умных устройств с возможностью отправки уведомлений

class NotificationMixin:
    def send_notification(self, message):
        print(f"Notification: {self.name} - {message}")

    # Миксин для умных устройств с таймером


class TimerMixin:
    def set_timer(self, seconds):
        print(f"{self.name} timer set for {seconds} seconds")
        # Логика таймера

    # Применяем миксины к классам

class SmartBulbWithNotification(SmartBulb, NotificationMixin):
    pass


class SmartSmokeDetectorWithTimer(SmartSmokeDetector, TimerMixin):
    pass


class SmartHumidifierWithNotificationAndTimer(SmartHumidifier, NotificationMixin, TimerMixin):
    pass

# Миксин Срочное уведомление
class UrgentNotificationMixin:
    def send_urgent_notification(self, message):
        print(f"Urgent Notification: {self.name} - {message}")

# Миксин Подключение к Wi-Fi
class WifiConnectionMixin:
    def connect_to_wifi(self, network_name, password):
        print(f"{self.name} connected to Wi-Fi network {network_name} with password {password}")

# Миксин Расписание работы
class ScheduleMixin:
    def __init__(self):
        self.schedule = {}

    def set_schedule(self, schedule):
        self.schedule = schedule

    def execute_schedule(self, time):
        if time in self.schedule:
            print(f"{self.name} executing scheduled task: {self.schedule[time]}")

# Применяем новые миксины к классам
class SmartBulbWithUrgentNotification(SmartBulb, UrgentNotificationMixin):
    pass

class SmartSmokeDetectorWithWifi(SmartSmokeDetector, WifiConnectionMixin):
    pass

class SmartHumidifierWithSchedule(SmartHumidifier, ScheduleMixin):
    pass

# Класс Умная лампочка со срочным уведомлением
class SmartBulbWithUrgentNotification(SmartBulb, UrgentNotificationMixin):
    pass

# Часть 3

# Класс Умный датчик дыма с Wi-Fi подключением
class SmartSmokeDetectorWithWifi(SmartSmokeDetector, WifiConnectionMixin):
    pass

# Класс Умный увлажнитель воздуха с расписанием работы
class SmartHumidifierWithSchedule(SmartHumidifier, ScheduleMixin):
    pass

# Создаем объекты с конкретными устройствами
bulb = SmartBulbWithUrgentNotification("Living Room Bulb")
detector = SmartSmokeDetectorWithWifi("Kitchen Smoke Detector")
humidifier = SmartHumidifierWithSchedule("Bedroom Humidifier")

# Используем методы миксинов
bulb.send_urgent_notification("Power outage detected!")
detector.connect_to_wifi("HomeNetwork", "Password123")
humidifier.set_schedule({"08:00": "Turn on", "22:00": "Turn off"})

# Используем методы базового класса и получаем состояние
bulb.turn_on()
detector.turn_on()
humidifier.turn_on()
print(bulb.get_state())
print(detector.get_state())
print(humidifier.get_state())

# Выполняем расписание для увлажнителя воздуха
humidifier.execute_schedule("08:00")
humidifier.execute_schedule("22:00")