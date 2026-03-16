from models.espada import Espada
from models.heroi import Heroi
from models.inimigo import Inimigo
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

    combate = Combate(heroi, inimigo)
    combate.iniciar()


if __name__ == "__main__":
    main()



