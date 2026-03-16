from __future__ import annotations

import os

from models.espada import Espada
from models.habilidade import Habilidade
from models.heroi import Heroi
from models.inimigo import Inimigo
from models.item import PocaoCura
from models.npc import Mercador
from sistema.combate import Combate


def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pausar() -> None:
    input("\nPressione ENTER para continuar...")


def introducao() -> None:
    limpar_tela()
    print("==============================")
    print("      ECOS DE ELDORIA        ")
    print("==============================\n")
    print(
        "Você desperta em uma carroça seguindo por uma estrada de terra, cercada por uma floresta densa.\n"
        "As lembranças são vagas, mas você sabe que Eldoria está à beira do caos: criaturas surgiram das sombras\n"
        "e boatos falam de um antigo mal despertando nas ruínas ao norte."
    )
    pausar()


def selecionar_classe() -> Heroi:
    limpar_tela()
    print("Escolha sua classe:\n")
    print("1 - Guerreiro  (Força alta, muita vida)")
    print("2 - Mago       (Inteligência alta, muita mana)")
    print("3 - Ladino     (Destreza e sorte altas)")

    while True:
        try:
            escolha = int(input("\nClasse: "))
        except ValueError:
            print("Opção inválida.")
            continue

        if escolha == 1:
            # Guerreiro: foco em força e vida
            heroi = Heroi(
                nome="Guerreiro",
                vida=40,
                vida_maxima=40,
                classe="Guerreiro",
                forca=10,
                destreza=6,
                inteligencia=3,
                sorte=4,
                mana=5,
                mana_maxima=5,
                ouro=20,
            )
            arma = Espada(
                nome="Espada Longa",
                descricao="Uma espada resistente usada por veteranos de guerra.",
                valor=20,
                dano=8,
                dano_habilidade=12,
            )
            heroi.equipar_arma(arma)
            golpe_pesado = Habilidade(
                nome="Golpe Pesado",
                descricao="Um ataque brutal que concentra toda a força do guerreiro.",
                dano=6 + heroi.get_forca() // 2,
            )
            heroi.adicionar_habilidade(golpe_pesado)
            break

        if escolha == 2:
            # Mago: foco em inteligência e mana
            heroi = Heroi(
                nome="Mago",
                vida=28,
                vida_maxima=28,
                classe="Mago",
                forca=3,
                destreza=5,
                inteligencia=10,
                sorte=4,
                mana=20,
                mana_maxima=20,
                ouro=15,
            )
            cajado = Espada(  # Reaproveitando estrutura de arma
                nome="Cajado Arcano",
                descricao="Um cajado simples, mas sintonizado com as energias arcanas.",
                valor=25,
                dano=4,
                dano_habilidade=10,
            )
            heroi.equipar_arma(cajado)
            bola_de_fogo = Habilidade(
                nome="Bola de Fogo",
                descricao="Concentra mana em uma esfera flamejante devastadora.",
                dano=8 + heroi.get_inteligencia() // 2,
            )
            escudo_arcano = Habilidade(
                nome="Escudo Arcano",
                descricao="Energias mágicas envolvem o mago, restaurando parte de sua vitalidade.",
                cura=6 + heroi.get_inteligencia() // 3,
            )
            heroi.adicionar_habilidade(bola_de_fogo)
            heroi.adicionar_habilidade(escudo_arcano)
            break

        if escolha == 3:
            # Ladino: foco em destreza e sorte
            heroi = Heroi(
                nome="Ladino",
                vida=32,
                vida_maxima=32,
                classe="Ladino",
                forca=6,
                destreza=10,
                inteligencia=4,
                sorte=8,
                mana=8,
                mana_maxima=8,
                ouro=25,
            )
            adaga = Espada(
                nome="Adaga Rápida",
                descricao="Uma adaga leve, perfeita para ataques rápidos e precisos.",
                valor=15,
                dano=5,
                dano_habilidade=11,
            )
            heroi.equipar_arma(adaga)
            ataque_furtivo = Habilidade(
                nome="Ataque Furtivo",
                descricao="Um golpe preciso vindo das sombras, explorando a fraqueza do inimigo.",
                dano=6 + heroi.get_destreza() // 2,
            )
            passo_sombrio = Habilidade(
                nome="Passo Sombrio",
                descricao="Um movimento ágil que permite respirar e se recompor.",
                cura=4 + heroi.get_sorte() // 2,
            )
            heroi.adicionar_habilidade(ataque_furtivo)
            heroi.adicionar_habilidade(passo_sombrio)
            break

        print("Opção inválida.")

    # Itens iniciais comuns
    pocao_pequena = PocaoCura(
        nome="Poção Pequena",
        descricao="Recupera um pouco de vida.",
        valor=5,
        cura=10,
    )
    pocao_media = PocaoCura(
        nome="Poção Média",
        descricao="Recupera uma quantidade moderada de vida.",
        valor=10,
        cura=15,
    )
    heroi.inventario.adicionar_item(pocao_pequena)
    heroi.inventario.adicionar_item(pocao_media)

    return heroi


def pre_historia_primeiro_inimigo() -> None:
    limpar_tela()
    print(
        "Você desce da carroça na pequena vila de Arvendale.\n"
        "Após algumas poucas instruções do cocheiro, você segue pela estrada em direção à floresta,\n"
        "onde relatos de criaturas hostis têm assustado os viajantes."
    )
    pausar()


def historia_pos_primeiro_combate() -> None:
    limpar_tela()
    print(
        "O inimigo cai ao chão, e o silêncio volta a tomar conta da floresta.\n"
        "Você percebe pegadas mais pesadas seguindo trilhas diferentes — sinais de que ameaças maiores o aguardam.\n"
        "Mesmo assim, a sensação de propósito cresce dentro de você."
    )
    pausar()


def historia_antes_mercador() -> None:
    limpar_tela()
    print(
        "Depois de outro confronto árduo, você retorna à estrada principal.\n"
        "Mais adiante, um pequeno acampamento com uma carroça coberta e lamparinas chama sua atenção.\n"
        "Um mercador acena, convidando-o para se aproximar."
    )
    pausar()


def historia_final_antes_boss() -> None:
    limpar_tela()
    print(
        "Reabastecido e um pouco mais confiante após negociar com o mercador,\n"
        "você segue para as ruínas antigas de Eldoria. O ar fica pesado, e uma presença opressora se faz sentir.\n"
        "Diante de um antigo portal rachado, uma figura colossal emerge das sombras: o líder das criaturas."
    )
    pausar()


def iniciar_jogo() -> None:
    introducao()
    heroi = selecionar_classe()

    pre_historia_primeiro_inimigo()
    # Primeiro inimigo
    lobo = Inimigo("Lobo Faminto", vida=18, dano_base=3)
    combate1 = Combate(heroi, lobo)
    combate1.iniciar()
    if not heroi.esta_vivo() or combate1.fugiu:
        print("\nSua jornada termina cedo demais...")
        return

    historia_pos_primeiro_combate()

    # Segundo inimigo
    bandido = Inimigo("Bandido da Estrada", vida=24, dano_base=5)
    combate2 = Combate(heroi, bandido)
    combate2.iniciar()
    if not heroi.esta_vivo() or combate2.fugiu:
        print("\nSeu nome se perde entre tantos que tombaram em Eldoria.")
        return

    historia_antes_mercador()

    # NPC mercador
    itens_mercador = [
        PocaoCura(
            nome="Poção Grande",
            descricao="Restaura uma grande quantidade de vida.",
            valor=18,
            cura=25,
        ),
        PocaoCura(
            nome="Poção de Emergência",
            descricao="Um preparado raro, usado em momentos críticos.",
            valor=25,
            cura=35,
        ),
    ]
    mercante = Mercador(
        nome="Ronan, o Mercante",
        dialogo="Saudações, viajante! Tenho exatamente o que você precisa para sobreviver nas ruínas.",
        itens=itens_mercador,
    )
    mercante.interagir(heroi)

    historia_final_antes_boss()

    # Chefe final
    chefe = Inimigo("Chefe Orc das Ruínas", vida=40, dano_base=7)
    combate_final = Combate(heroi, chefe)
    combate_final.iniciar()

    if heroi.esta_vivo() and not combate_final.fugiu and not chefe.esta_vivo():
        print(
            "\nCom um último golpe, o Chefe Orc cai. As sombras que envolviam as ruínas começam a se dissipar.\n"
            "Talvez este seja apenas o primeiro passo para restaurar Eldoria... mas, por agora, você venceu."
        )
    elif combate_final.fugiu:
        print(
            "\nVocê foge das ruínas, carregando tanto o peso da derrota quanto a esperança de um dia retornar mais forte."
        )
    else:
        print(
            "\nAs ruínas silenciam novamente, enquanto seu corpo cai ao chão.\n"
            "Seu sacrifício se torna mais uma história sussurrada entre os viajantes de Eldoria."
        )

