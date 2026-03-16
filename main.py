from models.espada import Espada
from models.habilidade import Habilidade
from models.heroi import Heroi
from models.inimigo import Inimigo
from models.item import PocaoCura
from sistema.combate import Combate


def main() -> None:
    heroi = Heroi("Herói", vida=30)
    inimigo = Inimigo("Goblin", vida=20, dano_base=4)

    espada = Espada(
        nome="Espada de Treino",
        descricao="Uma espada simples, mas confiável.",
        valor=10,
        dano=6,
        dano_habilidade=10,
    )
    heroi.equipar_arma(espada)

    # Habilidades básicas
    golpe_forte = Habilidade(
        nome="Golpe Forte",
        descricao="Um ataque poderoso que causa dano adicional.",
        dano=8,
    )
    cura_simples = Habilidade(
        nome="Cura Simples",
        descricao="Recupera uma pequena quantidade de vida.",
        cura=6,
    )
    heroi.adicionar_habilidade(golpe_forte)
    heroi.adicionar_habilidade(cura_simples)

    # Itens iniciais
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

    combate = Combate(heroi, inimigo)
    combate.iniciar()


if __name__ == "__main__":
    main()



