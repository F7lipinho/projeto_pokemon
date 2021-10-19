class Programacao:
    def __init__(self, id, nome, duracao, genero, idioma, legenda, ano, avaliacao):
        self.__id = int(id)
        self.__nome = str(nome)
        self.__duracao = str(duracao)
        self.__genero = str(genero)
        self.__idioma = str(idioma)
        self.__legenda = str(legenda)
        self.__ano= int(ano)
        self.__avaliacao = int(0)
        self.__favorito = False

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def duracao(self):
        return self.__duracao
    @property
    def genero(self):
        return self.__genero
    
    @property
    def idioma(self):
        return self.__idioma
    
    @property
    def legenda(self):
        return self.__legenda
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def avaliacao(self):
        return self.__avaliacao

    @property
    def favorito(self):
        return self.__favorito

    def incrementa_avaliacao(self):
        self.__avaliacao += 1
    
    def imprime_detalhes(self):
        print(f'filme: {self.__nome}')
    
    def __str__(self):
        pass
    
    def favoritar_programacao(self):
        self.__favorito = True 

    def desfavoritar_programacao(self):
        self.__favorito = False 
    
    def reproduzir(self):
        print('Programação sendo reproduzida')

    def velocidade_reproducao(self, velocidade_reproducao):
        print('Programação sendo reproduzida na velocidade x{velocidade_reproducao}')



'''new_programacao = Programacao(1,'teste', '24', 'ação', 'inglês', 'português', '2020')
new_programacao.imprime_detalhes()
print(new_programacao)'''