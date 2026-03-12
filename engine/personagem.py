from random import randint
from utils.cores import Cores


class Personagem:
    def __init__(self, nome, vida, mana, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__mana = mana
        self.__nivel = nivel

    #   Getters

    def get_nome(self):
        return self.__nome
    def get_vida(self):
        return self.__vida
    def get_mana(self):
        return self.__mana
    def get_nivel(self):
        return self.__nivel
    

    #   Funções da classe
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = randint(self.__nivel * 2, self.__nivel * 4)
        alvo.receber_dano(dano)
        return f"{self.__nome} Atacou {alvo.get_nome()} e causou {Cores.VERMELHO}{dano}{Cores.RESET} de dano"

    def status(self):
        print(f"Vida: {self.__vida} | Mana: {self.__mana} | Nivel: {self.__nivel}")


