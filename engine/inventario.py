

class Intenvario:
    def __init__(self):
        self.__inventario = list()

    def adicionar_item(self, item):
        self.__inventario.append(item)

    def remover_item(self, item):
        self.__inventario.remove(item)

    def exibir_inventario(self):
        return f"\n".join(
            f" - {item.get_nome()}"
            for item in self.__inventario
        )