class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("O animal faz algum som.")


class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro faz au au!")


animal_generico = Animal("Animal Genérico")
animal_generico.fazer_som()

meu_cachorro = Cachorro("Rex")
meu_cachorro.fazer_som()


#Em programação, herança é um conceito que permite criar classes novas com base em classes existentes. A classe nova, chamada de classe derivada ou subclasse, herda as características e comportamentos da classe existente, chamada de classe base ou superclasse. A herança permite reutilizar código e estabelecer relações hierárquicas entre classes.