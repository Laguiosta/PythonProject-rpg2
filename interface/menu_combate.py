from engine.combate import Combate
from engine.personagem import *
from time import sleep
from utils.atalhos import *
combate = Combate()

def turno_personagem(personagem, inimigo):
        print_titulo('YOUR TURN')
        print(f"\nEnemy life: {inimigo.get_vida()}")
        print(f"Your life: {personagem.get_vida()}")
        linha()

def menu_combate(personagem, inimigo):
    while personagem.get_vida() > 0 and inimigo.get_vida() > 0:
        turno_personagem(personagem, inimigo)
        choice_opcao = int(input("\n1. Atacar\n2. Habilidades: "))
        if choice_opcao == 1:
            print(combate.atacar(personagem, inimigo))
            pressione_continuar()
            limpar_tela()
            if inimigo.get_vida() == 0:
                break
            print_titulo('ENEMY TURN')
            print(combate.atacar(inimigo, personagem))
            pressione_continuar()
        if choice_opcao == 2:
            limpar_tela()
            print_titulo('HABILIDADES')
            print(f'\n{personagem.listar_habilidades()}')
            linha()
            choice_habilidade = int(input("\nQual habilidade deseja usar: "))
            while True:
                habilidade_escolhida = personagem.habilidades[choice_habilidade - 1]
                os.system('cls')
                choice_descricao = input(f"Deseja ver a descrição da habilidade {Cores.VERDE}{habilidade_escolhida.get_nome()}{Cores.RESET} [y/n]: ")
                if choice_descricao == 'y':
                     print('\n',habilidade_escolhida.get_descricao())
                     pressione_continuar()
                     break
                elif choice_descricao == 'n':
                     break
                else:
                     print("Opção inválida! Tente novamente")
                     pressione_continuar()
            limpar_tela()
            print(combate.atacar_habilidade(personagem, habilidade_escolhida, inimigo))
            pressione_continuar()
        limpar_tela()


