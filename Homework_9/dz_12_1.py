class Car:

    def __init__(self, make: str, model: str, mileage: float = 0):
        self.__make = make
        self.__model = model
        self.__mileage = 0
        self.mileage = mileage

    @property
    def mileage(self) -> float:
        return self.__mileage

    @mileage.setter
    def mileage(self, value: float):
        if value < 0:
            raise ValueError('Пробег не может быть отрицательным числом.')
        if value < self.__mileage:
            raise ValueError(
                f'Новый пробег ({value}) не может быть меньше текущего'
                f' ({self.__mileage}).'
            )
        self.__mileage = value


car = Car('Toyota', 'Camry', 50000)
print(f'Пробег {car.mileage}')

car.mileage = 50500
print(f'Пробег: {car.mileage}')
