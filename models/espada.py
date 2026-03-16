from __future__ import annotations

from models.item import Item
from models.personagem import Personagem


class Espada(Item):
    def __init__(self, nome: str, descricao: str, valor: int, dano: int, dano_habilidade: int) -> None:
        super().__init__(nome, descricao, valor)
        self.__dano = int(dano)
        self.__dano_habilidade = int(dano_habilidade)

    def get_dano(self) -> int:
        return self.__dano

    def usar_habilidade(self, alvo: Personagem) -> str:
        dano = max(0, self.__dano_habilidade)
        alvo.receber_dano(dano)
        return f"{self.get_nome()} usa habilidade e causa {dano} de dano em {alvo.get_nome()}."

