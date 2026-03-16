from __future__ import annotations

import os

from models.heroi import Heroi
from models.inimigo import Inimigo


class Combate:
    def __init__(self, heroi: Heroi, inimigo: Inimigo) -> None:
        self.heroi = heroi
        self.inimigo = inimigo
        self.fugiu = False

    def exibir_status(self) -> None:
        print("\n=== STATUS ===")
        print(f"{self.heroi.get_nome()}: {self.heroi.get_vida()}/{self.heroi.get_vida_maxima()}")
        print(f"{self.inimigo.get_nome()}: {self.inimigo.get_vida()}/{self.inimigo.get_vida_maxima()}")

    def _pausar_e_limpar(self) -> None:
        input("\nPressione ENTER para continuar...")
        # Limpa a tela (Windows / Unix-like)
        os.system("cls" if os.name == "nt" else "clear")

    def menu(self) -> int:
        print("\n1 - Atacar")
        print("2 - Usar habilidade")
        print("3 - Ver status")
        print("4 - Fugir")
        while True:
            try:
                escolha = int(input("\nEscolha uma opção: "))
            except ValueError:
                print("Opção inválida.")
                continue
            if escolha in (1, 2, 3, 4):
                return escolha
            print("Opção inválida.")

    def iniciar(self) -> None:
        print(f"\n{self.heroi.get_nome()} encontrou {self.inimigo.get_nome()}!")
        self.exibir_status()

        while self.heroi.esta_vivo() and self.inimigo.esta_vivo() and not self.fugiu:
            escolha = self.menu()

            if escolha == 1:
                print(self.heroi.atacar(self.inimigo))
                self._pausar_e_limpar()
            elif escolha == 2:
                print(self.heroi.usar_habilidade_da_arma(self.inimigo))
                self._pausar_e_limpar()
            elif escolha == 3:
                self.exibir_status()
                continue
            elif escolha == 4:
                self.fugiu = True
                break

            if not self.inimigo.esta_vivo():
                break

            print(self.inimigo.atacar(self.heroi))
            self.exibir_status()

        if self.fugiu:
            print("\nVocê fugiu do combate.")
        elif self.heroi.esta_vivo() and not self.inimigo.esta_vivo():
            print(f"\n{self.inimigo.get_nome()} foi derrotado!")
        elif self.inimigo.esta_vivo() and not self.heroi.esta_vivo():
            print(f"\n{self.heroi.get_nome()} foi derrotado...")

