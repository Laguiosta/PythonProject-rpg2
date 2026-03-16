from __future__ import annotations

from models.personagem import Personagem


class Habilidade:
    def __init__(self, nome: str, descricao: str, dano: int = 0, cura: int = 0) -> None:
        self.__nome = nome
        self.__descricao = descricao
        self.__dano = int(dano)
        self.__cura = int(cura)

    def get_nome(self) -> str:
        return self.__nome

    def get_descricao(self) -> str:
        return self.__descricao

    def usar(self, usuario: Personagem, alvo: Personagem) -> str:
        texto_partes: list[str] = []

        if self.__dano > 0:
            dano = max(0, self.__dano)
            alvo.receber_dano(dano)
            texto_partes.append(
                f"{usuario.get_nome()} usa {self.__nome} em {alvo.get_nome()} causando {dano} de dano."
            )

        if self.__cura > 0:
            cura = max(0, self.__cura)
            valor_curado = usuario.curar(cura)
            texto_partes.append(
                f"{usuario.get_nome()} recupera {valor_curado} de vida com {self.__nome}."
            )

        if not texto_partes:
            return f"{usuario.get_nome()} usa {self.__nome}, mas nada acontece."

        return " ".join(texto_partes)

