from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano, n_portas):
        super().__init__(marca, modelo, placa, ano)
        self.__n_portas = n_portas

    def __str__(self):
        return super().__str__() + f"    Portas: {self.__n_portas}"

    def getPortas(self):
        return self.__n_portas