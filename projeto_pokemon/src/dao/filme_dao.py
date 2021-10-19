from src.dao.programacao_dao import programacaoDAO

class FilmeDAO(programacaoDAO):
    def __init__(self, instancia_filme):
        super().__init__(instancia_filme)
        self._programacao_json ['duracao'] = instancia_filme.duracao
        