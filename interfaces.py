from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Flyable):
    def fly(self):
        return "Flies in the sky"

class Airplane(Flyable):
    def fly(self):
        return "Flies through the clouds"

bird = Bird()
airplane = Airplane()
print(bird.fly())      # Output: Flies in the sky
print(airplane.fly()) # Output: Flies through the clouds
