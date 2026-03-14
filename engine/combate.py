from random import randint
from utils.cores import Cores
from habilidades.habilidade_base import *


class Combate:
    def receber_dano(self, alvo, dano):
        alvo.vida -= dano
        if alvo.get_vida() <= 0:
            alvo.vida = 0

    def atacar(self, atacante, alvo):
        dano = randint(atacante.get_nivel() * 2, atacante.get_nivel() * 4)
        self.receber_dano(alvo, dano)
        return f"\n{atacante.get_nome()} Atacou {alvo.get_nome()} e causou {Cores.VERMELHO}{dano}{Cores.RESET} de dano"
    
    def atacar_habilidade(self, atacante, habilidade, alvo):
        dano = randint(atacante.get_nivel() * 2, atacante.get_nivel() * 4) + habilidade.get_dano()
        self.receber_dano(alvo, dano)
        return f"\n{atacante.get_nome()} Usou {Cores.VERDE}{habilidade.get_nome()}{Cores.RESET} e causou {Cores.VERMELHO}{dano}{Cores.RESET} de dano"
        
