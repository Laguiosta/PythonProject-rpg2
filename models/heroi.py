from __future__ import annotations

from models.espada import Espada
from models.habilidade import Habilidade
from models.personagem import Personagem
from sistema.inventario import Inventario


class Heroi(Personagem):
    def __init__(self, nome: str, vida: int, vida_maxima: int | None = None) -> None:
        super().__init__(nome, vida, vida_maxima)
        self.arma: Espada | None = None
        self.habilidades: list[Habilidade] = []
        self.inventario = Inventario()

    def equipar_arma(self, arma: Espada) -> None:
        self.arma = arma

    def adicionar_habilidade(self, habilidade: Habilidade) -> None:
        self.habilidades.append(habilidade)

    def listar_habilidades(self) -> list[Habilidade]:
        return self.habilidades

    def atacar(self, alvo: Personagem) -> str:
        dano = self.arma.get_dano() if self.arma is not None else 1
        alvo.receber_dano(dano)
        nome_arma = self.arma.get_nome() if self.arma is not None else "punhos"
        return f"{self.get_nome()} ataca {alvo.get_nome()} com {nome_arma} e causa {dano} de dano."

    def usar_habilidade(self, indice: int, alvo: Personagem) -> str:
        try:
            habilidade = self.habilidades[indice]
        except IndexError:
            return "Habilidade inválida."
        return habilidade.usar(self, alvo)

    def usar_habilidade_da_arma(self, alvo: Personagem) -> str:
        if self.arma is None:
            return "Você não tem arma equipada."
        return self.arma.usar_habilidade(alvo)

