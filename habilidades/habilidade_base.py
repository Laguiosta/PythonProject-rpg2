class Habilidade:
    def __init__(self, nome, descricao, dano):
        self.__nome = nome
        self.__descricao = descricao
        self.__dano = dano

    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao

    def get_dano(self):
        return self.__dano
    
    
    
ataque_rapido = Habilidade('Ataque rápido', 'Um golpe muito rápido', 20)
soco = Habilidade('Soco', 'Um soco forte', 15)
    
