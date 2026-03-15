from engine.combate import Combate
from habilidades.habilidade_base import *
from engine.personagem import *
from utils.atalhos import *

combate = Combate()


def reduzir_cooldowns(personagem):
    for habilidade in personagem.habilidades:
        habilidade.reduzir_cooldown()


def turno_personagem(personagem, inimigo):

    print_titulo('YOUR TURN')

    personagem.status()

    print(f"\nEnemy life: {inimigo.get_vida()}")
    print(f"Your life: {personagem.get_vida()}")

    linha()


def turno_inimigo(personagem, inimigo):

    if inimigo.get_vida() <= 0:
        return

    print_titulo('ENEMY TURN')

    print(combate.atacar(inimigo, personagem))

    pressione_continuar()


def menu_combate(personagem, inimigo):

    while personagem.get_vida() > 0 and inimigo.get_vida() > 0:

        turno_personagem(personagem, inimigo)

        acao_realizada = False

        try:
            choice_opcao = int(input("\n1. Atacar\n2. Habilidades: "))
        except ValueError:
            print("Opção inválida")
            pressione_continuar()
            limpar_tela()
            continue


        # ATAQUE NORMAL
        if choice_opcao == 1:

            print(combate.atacar(personagem, inimigo))
            pressione_continuar()
            acao_realizada = True


        # MENU DE HABILIDADES
        elif choice_opcao == 2:

            while True:

                limpar_tela()

                print_titulo('HABILIDADES')

                print(f'\n{personagem.listar_habilidades()}')
                print("\n0. Voltar")

                linha()

                try:
                    choice_habilidade = int(input("\nQual habilidade deseja usar: "))
                except ValueError:
                    print("Opção inválida")
                    pressione_continuar()
                    continue

                # VOLTAR SEM GASTAR TURNO
                if choice_habilidade == 0:
                    limpar_tela()
                    break

                if choice_habilidade < 1 or choice_habilidade > len(personagem.habilidades):
                    print("Habilidade inválida")
                    pressione_continuar()
                    continue

                habilidade_escolhida = personagem.habilidades[choice_habilidade - 1]

                limpar_tela()

                resultado = combate.atacar_habilidade(
                    personagem,
                    habilidade_escolhida,
                    inimigo
                )

                print(resultado)

                pressione_continuar()

                if "causou" in resultado:
                    acao_realizada = True
                    break


        else:
            print("Escolha uma opção válida")
            pressione_continuar()
            limpar_tela()
            continue


        # se nenhuma ação válida aconteceu, reinicia turno
        if not acao_realizada:
            limpar_tela()
            continue


        if inimigo.get_vida() <= 0:
            break


        limpar_tela()

        # TURNO DO INIMIGO
        turno_inimigo(personagem, inimigo)

        # REDUZ COOLDOWN
        reduzir_cooldowns(personagem)

        limpar_tela()


    personagem.status()