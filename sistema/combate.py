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
        linha_heroi = f"{self.heroi.get_nome()} ({self.heroi.get_classe()}): {self.heroi.get_vida()}/{self.heroi.get_vida_maxima()}"
        linha_heroi += f" | For: {self.heroi.get_forca()} Des: {self.heroi.get_destreza()} Int: {self.heroi.get_inteligencia()} Sor: {self.heroi.get_sorte()}"
        linha_heroi += f" | Mana: {self.heroi.get_mana()}/{self.heroi.get_mana_maxima()}"
        print(linha_heroi)
        print(f"{self.inimigo.get_nome()}: {self.inimigo.get_vida()}/{self.inimigo.get_vida_maxima()}")

    def _pausar_e_limpar(self) -> None:
        input("\nPressione ENTER para continuar...")
        # Limpa a tela (Windows / Unix-like)
        os.system("cls" if os.name == "nt" else "clear")

    def menu(self) -> int:
        print("\n1 - Atacar")
        print("2 - Usar habilidade")
        print("3 - Ver status")
        print("4 - Inventário")
        print("5 - Fugir")
        while True:
            try:
                escolha = int(input("\nEscolha uma opção: "))
            except ValueError:
                print("Opção inválida.")
                continue
            if escolha in (1, 2, 3, 4, 5):
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
                if not self.heroi.habilidades:
                    print("Você não possui habilidades no momento.")
                    self._pausar_e_limpar()
                else:
                    print("\n=== HABILIDADES ===")
                    for i, hab in enumerate(self.heroi.listar_habilidades(), start=1):
                        print(f"{i} - {hab.get_nome()} - {hab.get_descricao()}")
                    print("0 - Voltar")

                    try:
                        escolha_hab = int(input("\nEscolha uma habilidade: "))
                    except ValueError:
                        print("Opção inválida.")
                        self._pausar_e_limpar()
                        continue

                    if escolha_hab == 0:
                        continue

                    indice = escolha_hab - 1
                    mensagem = self.heroi.usar_habilidade(indice, self.inimigo)
                    print(mensagem)
                    self._pausar_e_limpar()
            elif escolha == 3:
                self.exibir_status()
                continue
            elif escolha == 4:
                itens = self.heroi.inventario.listar_itens()
                if not itens:
                    print("Seu inventário está vazio.")
                    self._pausar_e_limpar()
                    continue

                print("\n=== INVENTÁRIO ===")
                for i, item in enumerate(itens, start=1):
                    print(f"{i} - {item.get_nome()} - {item.get_descricao()}")
                print("0 - Voltar")

                try:
                    escolha_item = int(input("\nEscolha um item para usar: "))
                except ValueError:
                    print("Opção inválida.")
                    self._pausar_e_limpar()
                    continue

                if escolha_item == 0:
                    continue

                indice_item = escolha_item - 1
                mensagem_item = self.heroi.inventario.usar_item_por_indice(indice_item, self.heroi)
                print(mensagem_item)
                self._pausar_e_limpar()
                # Usar item não gasta o turno do inimigo
                continue
            elif escolha == 5:
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

