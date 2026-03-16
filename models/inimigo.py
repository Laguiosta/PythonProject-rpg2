from __future__ import annotations

from models.personagem import Personagem


class Inimigo(Personagem):
    def __init__(self, nome: str, vida: int, dano_base: int, vida_maxima: int | None = None) -> None:
        super().__init__(nome, vida, vida_maxima)
        self.__dano_base = int(dano_base)

    def get_dano_base(self) -> int:
        return self.__dano_base

    def atacar(self, alvo: Personagem) -> str:
        dano = max(0, self.__dano_base)
        alvo.receber_dano(dano)
        return f"{self.get_nome()} ataca {alvo.get_nome()} e causa {dano} de dano."

