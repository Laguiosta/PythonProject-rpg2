from __future__ import annotations


class Item:
    def __init__(self, nome: str, descricao: str, valor: int) -> None:
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    def get_nome(self) -> str:
        return self.__nome

    def get_descricao(self) -> str:
        return self.__descricao

    def get_valor(self) -> int:
        return self.__valor

    def exibir_descricao(self) -> None:
        tamanho = len(self.__descricao) + len(self.__nome) + 2
        print("=" * tamanho)
        print("DESCRIÇÃO".center(tamanho))
        print("=" * tamanho)
        print(f"\n{self.__nome}: {self.__descricao}")

