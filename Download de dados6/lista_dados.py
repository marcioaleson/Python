from decimal import Decimal

class Relationship:
    """Classe que representa um relacionamento entre DataTables
       Essa classe tem todas as informações que identifica um
       relacionamento entre tabelas. Em qual ocluna ele existe,
       de onde vem para onde vai.
    """
    def __init__(self, name, _from, to, on):
        """Construtor:

           Args:
               name: Nome
               from: Tabela de onde sai
               to: Tabela para onde vai
               on: instância de coluna onde existe
        """
        self._name = name
        self._from = _from
        self._to = to
        self._on = on


class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []


    def add_column(self, name, kind, description):
        column = Column(name, kind, description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        """Cria uma referencia dessaa tabela para outra tabela
           Args:
               name: Nome da relação
               to: Instâcia da tabela apontada
               on: Instâcia coluna em que existe a relação
        """
    def add_reefrenced(self, name, by, on):
        """Cria uma referencia para outra tabela que aponta para essa

           Args:
               name: Nome da relação
               by: Instância da tabela que aponta para essa
               on: Instâcia coluna em que existe a relação
        """
        relationship = Relatoinship(name, by, self, on)
        self._referenced.append(relationship)


class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=""):
        super()._init__(name, kind, description = description)
        self._is_pk  = True

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name, self._kind, self._description)

        return "{} - {}".format('PK', _str)

class Column:
    def __init__(self, name, kind ,description=""):
        self._name = name
        self._kind = kind
        self._description = description
        self.__is_pk = False

    def _validate(kind, data):
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True
        validate = staticmethod(_validate)


    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name, self._kind, self._description)
        return _str
