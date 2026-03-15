from engine.personagem import Personagem
from engine.item import *
from interface.menu_combate import *

class Jogo:
    def __init__(self):
        self.heroi = Personagem("Herói", 10, 10, 1)
        self.inimigo = Personagem("Inimigo", 10, 10, 1)
        
    def iniciar(self):
        menu_combate(self.heroi, self.inimigo)



jogo = Jogo()
jogo.iniciar()



