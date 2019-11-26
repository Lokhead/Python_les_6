class Car:
    def __init__(self, speed=None, color='', name='', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} машина марки {self.name} поехала')

    def stop(self):
        print(f'{self.color} машина марки {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} машина марки {self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.color} машина марки {self.name}, скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'{self.color} машина марки {self.name}, скорость: {self.speed}')
        if self.speed > 60:
            print(f'Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.color} машина марки {self.name}, скорость: {self.speed}')
        if self.speed > 40:
            print(f'Превышение скорости')


class PoliceCar(Car):
    pass


car_1 = SportCar(speed=90, color='красная', name='Infinity')
car_1.show_speed()
car_1.turn('налево')
car_2 = TownCar(speed=55, color='синяя', name='Nissan')
car_2.go()
car_2.show_speed()
car_2.stop()
car_3 = WorkCar(speed=45, color='желтая', name='Dodge')
car_3.show_speed()
car_3.turn('направо')
