from engine.combate import Combate
from engine.personagem import *
from time import sleep
from utils.atalhos import *
import os

def menu_combate(personagem, inimigo):
    while personagem.get_vida() > 0 and inimigo.get_vida() > 0:
        print("="*30)
        print(F"{'YOUR TURN':^30}")
        print("="*30)
        print(f"\nEnemy life: {inimigo.get_vida()}")
        print(f"Your life: {personagem.get_vida()}")
        print("-"*30)
        choice = int(input("\n1. Atacar: "))
        if choice == 1:
            combate = Combate()
            print(combate.atacar(personagem, inimigo))
            sleep(1)
            os.system('cls')
            print("="*30)
            print(F"{'ENEMY TURN':^30}")
            print("="*30)
            print(combate.atacar(inimigo, personagem))
            pressione_continuar()

        os.system('cls')


