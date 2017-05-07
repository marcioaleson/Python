from column import Column

class DataTable:
    def add_column(self, name, kind, description = ""):
        self._validate_kind(kind)
        column = Column(name, kind, description = description)
        self._column.append(column)
        return column

    def _validate_kind(self, kind):
        if not kind in ('bigint', 'numeric', 'varchar'):
            raise Exception("Tipo inválido")
    
