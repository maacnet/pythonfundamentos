# Classe Carro para ser importada em um arquivo separado
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def descricao(self):
        print(f"{self.marca} {self.modelo} {self.ano}")

    def leitura_odometro(self):
        print(f"Este carro tem {self.odometro} KM rodados.")

    def atualiza_odometro(self, km):
        if km >= self.odometro:
            self.odometro = km
        else:
            print("Voce não pode diminuir o odometro.")