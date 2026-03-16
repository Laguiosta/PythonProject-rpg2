from __future__ import annotations

from models.espada import Espada
from models.personagem import Personagem


class Heroi(Personagem):
    def __init__(self, nome: str, vida: int, vida_maxima: int | None = None) -> None:
        super().__init__(nome, vida, vida_maxima)
        self.arma: Espada | None = None

    def equipar_arma(self, arma: Espada) -> None:
        self.arma = arma

    def atacar(self, alvo: Personagem) -> str:
        dano = self.arma.get_dano() if self.arma is not None else 1
        alvo.receber_dano(dano)
        nome_arma = self.arma.get_nome() if self.arma is not None else "punhos"
        return f"{self.get_nome()} ataca {alvo.get_nome()} com {nome_arma} e causa {dano} de dano."

    def usar_habilidade_da_arma(self, alvo: Personagem) -> str:
        if self.arma is None:
            return "Você não tem arma equipada."
        return self.arma.usar_habilidade(alvo)

