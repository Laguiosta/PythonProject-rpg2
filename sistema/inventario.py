from __future__ import annotations

from models.item import Item
from models.personagem import Personagem


class Inventario:
    def __init__(self) -> None:
        self._itens: list[Item] = []

    def adicionar_item(self, item: Item) -> None:
        self._itens.append(item)

    def remover_item(self, item: Item) -> None:
        if item in self._itens:
            self._itens.remove(item)

    def listar_itens(self) -> list[Item]:
        return list(self._itens)

    def usar_item_por_indice(self, indice: int, alvo: Personagem) -> str:
        try:
            item = self._itens[indice]
        except IndexError:
            return "Item inválido."

        mensagem = item.usar(alvo)
        # Consumíveis somem após uso
        self._itens.pop(indice)
        return mensagem

