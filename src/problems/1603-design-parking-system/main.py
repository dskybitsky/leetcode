class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.space = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        carTypeIndex = carType - 1

        if self.space[carTypeIndex] > 0:
            self.space[carTypeIndex] -= 1

            return True

        return False