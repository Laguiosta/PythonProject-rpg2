from __future__ import annotations


class Personagem:
    def __init__(self, nome: str, vida: int, vida_maxima: int | None = None) -> None:
        self.__nome = nome
        self.__vida_maxima = vida if vida_maxima is None else vida_maxima
        self.__vida = min(max(vida, 0), self.__vida_maxima)

    def get_nome(self) -> str:
        return self.__nome

    def get_vida(self) -> int:
        return self.__vida

    def get_vida_maxima(self) -> int:
        return self.__vida_maxima

    def receber_dano(self, dano: int) -> int:
        dano = max(0, int(dano))
        self.__vida = max(0, self.__vida - dano)
        return dano

    def curar(self, valor: int) -> int:
        valor = max(0, int(valor))
        vida_antes = self.__vida
        self.__vida = min(self.__vida_maxima, self.__vida + valor)
        return self.__vida - vida_antes

    def esta_vivo(self) -> bool:
        return self.__vida > 0

