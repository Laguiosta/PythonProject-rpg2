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
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, nova_vida):
         self.__vida = nova_vida

    #   Funções da classe


    def status(self):
        print(f"Vida: {self.__vida} | Mana: {self.__mana} | Nivel: {self.__nivel}")


