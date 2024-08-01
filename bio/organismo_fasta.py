from bio.constantes import CONVERSOR_DE_BASES
from bio.sequencia import Sequencia


class OrganismoFasta:
    def __init__(self, id, nome, sequencia):
        self.id = id
        self.nome = nome
        self.sequencia = Sequencia(sequencia)
