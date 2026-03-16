from random import randint
from utils.cores import Cores


class Combate:
    contador_do_turno = 0 
    def receber_dano(self, alvo, dano):
        alvo.vida -= dano
        if alvo.get_vida() <= 0:
            alvo.vida = 0

    def atacar(self, atacante, alvo):
        dano = randint(atacante.get_nivel() * 2, atacante.get_nivel() * 4)
        self.receber_dano(alvo, dano)
        return (
            f"\n{atacante.get_nome()} Atacou {alvo.get_nome()} e causou {Cores.VERMELHO}{dano}{Cores.RESET} de dano",
            True,
        )
    
    def atacar_habilidade(self, atacante, habilidade, alvo):
        if atacante.get_mana() < habilidade.get_custo_mana():
            return (f"Mana insuficiente para usar {habilidade.get_nome()}", False)
        
        if not habilidade.pode_usar():
            return (f"{habilidade.get_nome()} em recarga {habilidade.get_tempo_resfriamento()}", False)
            
        atacante.mana -= habilidade.get_custo_mana()
        dano = randint(atacante.get_nivel() * 2, atacante.get_nivel() * 4) + habilidade.get_dano()
        self.receber_dano(alvo, dano)
        habilidade.iniciar_cooldown()
        return (
            f"\n{atacante.get_nome()} Usou {Cores.VERDE}{habilidade.get_nome()}{Cores.RESET} e causou {Cores.VERMELHO}{dano}{Cores.RESET} de dano",
            True,
        )
    
    def contador_turno(self):
        self.__class__.contador_do_turno += 1
        return self.__class__.contador_do_turno
        
