class Road:
    def __init__(self, length=None, width=None):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        mass_sq_meter = 25
        thickness = 5
        total_mass = self._length * self._width * mass_sq_meter * thickness / 1000
        print(f'{total_mass} т')


calc_mass = Road(20, 5000)
calc_mass.asphalt_mass()
