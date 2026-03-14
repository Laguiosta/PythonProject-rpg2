import os

def pressione_continuar():
    while True:
        input("\nPressione ENTER para continuar:")
        break

def print_titulo(titulo):
        print("="*30)
        print(f"{titulo:^30}")
        print("="*30)

def linha():
     print('-'*30)

def limpar_tela():
     os.system('cls')