
class Habilidade:
    def __init__(self, nome, descricao, dano, custo_mana, cooldown, tempo_resfriamento = 0):
        self.__nome = nome
        self.__descricao = descricao
        self.__dano = dano
        self.__custo_mana = custo_mana
        self.__cooldown = cooldown
        self.__tempo_resfriamento = tempo_resfriamento
    

    def get_custo_mana(self):
        return self.__custo_mana
    
    def get_cooldown(self):
        return self.__cooldown

    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao

    def get_dano(self):
        return self.__dano
    

    
    def get_tempo_resfriamento(self):
        return self.__tempo_resfriamento
    
    def calculo_mana(self, usuario):
        if usuario.get_mana() >= self.__custo_mana:
            usuario.mana -= self.__custo_mana
        else:
            self.__habilidade_negada = True
            return  self.__habilidade_negada
        
    def pode_usar(self):
        if self.__tempo_resfriamento == 0:
            self.__tempo_resfriamento = self.__cooldown
            return self.__tempo_resfriamento
        
    def reduzir_cooldown(self):
        if self.__tempo_resfriamento > 0:
            self.__tempo_resfriamento -= 1
    
    def iniciar_cooldown(self):
        self.__tempo_resfriamento = self.__cooldown
    
        
    
        
    
    
    
    

