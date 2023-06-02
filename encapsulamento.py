class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._kilometragem = 0
        self.__velocidade_maxima = 200

    def acelerar(self, velocidade):
        if velocidade > self.__velocidade_maxima:
            print("Velocidade excedeu o limite máximo.")
        else:
            self._kilometragem += velocidade

    def obter_kilometragem(self):
        return self._kilometragem


meu_carro = Carro("Toyota", "Corolla")
meu_carro.acelerar(100)
meu_carro.acelerar(150)
print(meu_carro.obter_kilometragem())
print(meu_carro._kilometragem)  # Acessando um membro protegido (convenção)

print(meu_carro.__velocidade_maxima)  # Tentando acessar um membro privado


 #encapsulamento é um conceito que permite ocultar a implementação interna de uma classe, fornecendo uma interface externa para interagir com os objetos dessa classe. O encapsulamento busca proteger os dados internos da classe e controlar o acesso a eles, evitando que sejam modificados de forma inadequada.