from engine.personagem import Personagem


class Heroi(Personagem):
    def __init__(self, nome, vida, mana, nivel,):
        super().__init__(nome, vida, mana, nivel)
        self.__habilidades = list()
