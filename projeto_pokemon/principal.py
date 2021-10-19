from src.classes.serie import Serie
from src.classes.filme import Filme
from src.dao.serie_dao import SerieDAO

novo_filme = Filme(1,'Jhon Wick', 'Ação','inglês', 'português', '2020', 93)
print(novo_filme)

nova_serie = Serie(1, 'Peaky Blinders', 'Crime', 'Inglês', 'Português', '2020', 77)