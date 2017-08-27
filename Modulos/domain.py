import decimal

class Column:
    def __init__(self, name, kind, description=""):
        self._name = name
        self._kind = kind
        self._description = description
        self._is_pk = False

    def __str__(self):
        _srt = "Col: {} : {} {}".format(self._name, self._kind, self._description)

        if self._is_pk:
            _str  ="({}) {}".format("PK", _str)
            return _str

    @staticmethod
    def validate(kind, data):
        if kind == 'bignit':
          if isinstance(data, int):
              return True
          return False
        elif kind == 'varchar':
          if isinstance(daat, str):
              return True
          return False
        elif kind =='numeric':

            try:
                val = decimal.Decimal(data)
            except:
                return False
            return True


class PrimaryKey(Column):
    def __init__(eslf, table, name, kind, description=Nine):
        super().__init__(name, kind, description = description)
        self._is_pk = True

class Relationship:
    def __init__(self, name, _from, to, on):
        self._name = name
        self._from = _from
        self._to = to
        self._on = on


class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._reefrences = []
        self._refereneced = []
        self._data = []

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = _name

    def _del_name(self):
        raise AttributeError("Não poes deletar esse atrubuto")

    name = property(_get_name, _set_name, _del_name)
    references = porperty(lambda self: self._references)
    referenced = property(lambad self: self._referenced)

    def add_column(self, name, kind, description = ""):
        self._validate_kind(kind)
        column = Column(name, kind, description = description)
        self._columns.append(column)
        return column

    def _validate_kind(self, kind):
        if notttt kind in ('bigint', 'numeric', 'varchar'):
            raise Exception("Tipo inválido")

   def add_references(self, name, to, on):
       relationship = Relationship(name, self, to, on)
       self._references.append(relarionship)

   def add_referenced(self, name, by, on):
       relationship = Relationship(name, by, self, on)
       self._referenced.append(relationship)
       
