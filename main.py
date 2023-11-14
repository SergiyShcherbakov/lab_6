# Створіть класи "ТранспортнийЗасіб" та два підкласи, "Автомобіль" і "Велосипед",
# які успадковують властивості та методи батьківського класу.
# Кожен транспортний засіб повинен мати атрибути "швидкість" та "потужність", а також метод "прискорити",
# який збільшує швидкість на певну величину. Автомобіль повинен мати додатковий атрибут "пальне",
# а велосипед - "кількість педалей". Створіть об'єкти для кожного підкласу,
# змініть їх атрибути та викличте метод "прискорити" для кожного.

class Transport:
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def accelerate(self, increase):
        self.speed += increase


class Car(Transport):
    def __init__(self, speed, power, fuel):
        super().__init__(speed, power)
        self.fuel = fuel


class Bicycle(Transport):
    def __init__(self, speed, power, pedals):
        super().__init__(speed, power)
        self.pedals = pedals


# Створення об'єктів
car_instance = Car(speed=60, power=200, fuel='gasoline')
bicycle_instance = Bicycle(speed=20, power=50, pedals=2)

# Зміна атрибутів
car_instance.accelerate(10)
bicycle_instance.accelerate(5)

# Вивід атрибутів для перевірки
print("Car Speed:", car_instance.speed)
print("Bicycle Speed:", bicycle_instance.speed)
