from __future__ import annotations

from models.item import Item, PocaoCura
from models.heroi import Heroi


class NPC:
    def __init__(self, nome: str, dialogo: str) -> None:
        self._nome = nome
        self._dialogo = dialogo

    def falar(self) -> None:
        print(f"\n{self._nome}: {self._dialogo}")


class Mercador(NPC):
    def __init__(self, nome: str, dialogo: str, itens: list[Item]) -> None:
        super().__init__(nome, dialogo)
        self._itens = itens

    def interagir(self, heroi: Heroi) -> None:
        self.falar()
        while True:
            print("\n=== LOJA DO MERCANTE ===")
            print(f"Ouro: {heroi.get_ouro()}")
            for i, item in enumerate(self._itens, start=1):
                print(f"{i} - {item.get_nome()} ({item.get_valor()} ouro) - {item.get_descricao()}")
            print("0 - Sair da loja")

            try:
                escolha = int(input("\nEscolha um item para comprar: "))
            except ValueError:
                print("Opção inválida.")
                continue

            if escolha == 0:
                print("\nVocê se despede do mercador.")
                break

            indice = escolha - 1
            if indice < 0 or indice >= len(self._itens):
                print("Opção inválida.")
                continue

            item_escolhido = self._itens[indice]
            if heroi.get_ouro() < item_escolhido.get_valor():
                print("Você não tem ouro suficiente.")
                continue

            heroi.gastar_ouro(item_escolhido.get_valor())
            heroi.inventario.adicionar_item(item_escolhido)
            print(f"Você comprou {item_escolhido.get_nome()}!")

