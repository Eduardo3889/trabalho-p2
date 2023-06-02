from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro faz: Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("O gato faz: Miau!")

animais = [Cachorro(), Gato()]


for animal in animais:
    animal.fazer_som()
