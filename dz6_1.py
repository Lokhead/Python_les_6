from time import sleep


class TrafficLight:
    __color = 'red'

    def running(self):
        TrafficLight.__color = 'красный'
        print(TrafficLight.__color)
        sleep(7)
        TrafficLight.__color = 'желтый'
        print(TrafficLight.__color)
        sleep(2)
        TrafficLight.__color = 'зеленый'
        print(TrafficLight.__color)
        sleep(4)


start = TrafficLight()
start.running()
