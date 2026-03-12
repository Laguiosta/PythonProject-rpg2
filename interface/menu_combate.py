from engine.combate import *
from engine.personagem import *
from time import sleep

def menu_combate(personagem, inimigo):
    while personagem.get_vida() >= 0 and inimigo.get_vida() >= 0:
        choice = int(input(f"1. Atacar\n2. Habilidades"))
        if choice == 1:
            personagem_ataca = personagem.atacar(inimigo)
            print(personagem_ataca)

            print("="*20)
            print(f"\nTurno do {inimigo.get_nome()}")
            print("="*20)
            print("")
            inimigo_ataca = inimigo.atacar(personagem)
            print(inimigo_ataca)
