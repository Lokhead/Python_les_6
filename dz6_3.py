class Worker:
    def __init__(self, name='', surname='', position='', wage=None, bonus=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(total_income)


worker_1 = Position(name='Иван',
                    surname='Иванов',
                    position='инженер',
                    wage=35000,
                    bonus=10000
                    )
worker_2 = Position(name='Сергей',
                    surname='Сергеев',
                    position='техник',
                    wage=25000,
                    bonus=7000
                    )
worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()
