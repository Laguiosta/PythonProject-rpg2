from __future__ import annotations

from models.espada import Espada
from models.habilidade import Habilidade
from models.personagem import Personagem
from sistema.inventario import Inventario


class Heroi(Personagem):
    def __init__(
        self,
        nome: str,
        vida: int,
        vida_maxima: int | None = None,
        classe: str = "Aventureiro",
        forca: int = 1,
        destreza: int = 1,
        inteligencia: int = 1,
        sorte: int = 1,
        mana: int = 0,
        mana_maxima: int | None = None,
        ouro: int = 0,
    ) -> None:
        super().__init__(nome, vida, vida_maxima)
        self.arma: Espada | None = None
        self.habilidades: list[Habilidade] = []
        self.inventario = Inventario()

        self.__classe = classe
        self.__forca = int(forca)
        self.__destreza = int(destreza)
        self.__inteligencia = int(inteligencia)
        self.__sorte = int(sorte)
        self.__mana_maxima = mana if mana_maxima is None else mana_maxima
        self.__mana = max(0, min(int(mana), self.__mana_maxima))
        self.__ouro = int(ouro)

    def equipar_arma(self, arma: Espada) -> None:
        self.arma = arma

    def adicionar_habilidade(self, habilidade: Habilidade) -> None:
        self.habilidades.append(habilidade)

    def listar_habilidades(self) -> list[Habilidade]:
        return self.habilidades

    def get_classe(self) -> str:
        return self.__classe

    def get_forca(self) -> int:
        return self.__forca

    def get_destreza(self) -> int:
        return self.__destreza

    def get_inteligencia(self) -> int:
        return self.__inteligencia

    def get_sorte(self) -> int:
        return self.__sorte

    def get_mana(self) -> int:
        return self.__mana

    def get_mana_maxima(self) -> int:
        return self.__mana_maxima

    def get_ouro(self) -> int:
        return self.__ouro

    def gastar_ouro(self, quantidade: int) -> bool:
        if quantidade <= 0 or quantidade > self.__ouro:
            return False
        self.__ouro -= quantidade
        return True

    def atacar(self, alvo: Personagem) -> str:
        dano_base = self.arma.get_dano() if self.arma is not None else 1

        if self.__classe.lower() == "guerreiro":
            bonus = self.__forca // 2
        elif self.__classe.lower() == "mago":
            bonus = self.__inteligencia // 2
        elif self.__classe.lower() == "ladino":
            bonus = self.__destreza // 2
        else:
            bonus = 0

        dano = max(1, dano_base + bonus)
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

