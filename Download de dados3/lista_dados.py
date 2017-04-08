class DataTable:
    """Representa uma Tabela de dados.
    Essa classe repersenta uma tabela de dados do portal
    da transparência. Deve ser capaz de validar linhas
    inseriads de acordo com as colunas que possue. As
    linhas inseridas de acordo com as colunas que possui. As
    linhas inseridas ficam registardas dentro dela.

    Attribuets:
    name: Nome da Tabela
    columns: [Lista de colunas]
    data: [Lista de dados]
    """

    def __init__(self, name):
        """Construtor

        Args:
        name: Nome da Tabela
        """
        self._name = name
        self._columns = []
        self._data = []


    class Column:
        """Representa uma coluna em um DataTable.
        Essa classe contém as informações de uma colunas
        e deve validar um dado de acordo com o tipo de
        dado configurado no construtor.

        Attributes:
        name: Nome da Coluna
        kind: Tipo do Dado (varchar, bigint, numeric)
        description: Descrição da coluna
        """

        def __init__(self, name, kind, description=""):
            """Construtor

            Args:
            name: Nome da Coluna
            kind: Tipo od dado (varchra, bigint, numeric)
            description: Descrição da colina
            """
            self._name  = name
            self._kind = kind
            self._description = description
