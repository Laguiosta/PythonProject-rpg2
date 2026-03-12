from utils.cores import Cores
class Item:
    def __init__(self, nome, descricao, valor):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    #   Getters
    
    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def get_valor(self):
        return self.__valor
    
    def exibir_descricao(self):
        tamanho = len(self.__descricao) + len(self.__nome) + 2
        print(f"{Cores.AMARELO}={Cores.RESET}" * tamanho)
        print("DESCRIÇÃO".center(tamanho))
        print(f"{Cores.AMARELO}={Cores.RESET}" * tamanho)
        print(f"\n{Cores.VERDE}{self.__nome}{Cores.RESET}: {self.__descricao}")

class Espada(Item):
    def __init__(self, nome, descricao, valor, dano):
        super().__init__(nome, descricao, valor)
        self.__dano = dano


