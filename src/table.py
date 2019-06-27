from property import Property
from seed.seed import Seed

class Table:
    """
    テーブルです。
    データ構造を保持して、データの生成を行います。
    """

    def __init__(self, table_name, **properties):
        self.name = table_name 
        self.properties = Property(properties)

    def __call__(self, name):
        return self.properties.get(name)

    def create(self, count):
        records = [self._assemble(index=index) for index in range(count)]
        self.records = records
        return self

    def to_sql(self):
        if self.records is None:
            print("please run create method")
        else:
            sqls = list()
            for record in self.records:
                sql = (
                    f"INSERT INTO {self.name}"
                    + "("
                    + ", ".join([str(k) for k in record.keys()])
                    + ") VALUES ("
                    + ", ".join([self._str(v) for v in record.values()])
                    + ");"
                )
                sqls.append(sql)
            return sqls

    def show_sql(self):
        if self.records is None:
            print('data is not exist')
        else:
            for query in self.to_sql():
                print(query)

    def _assemble(self, index):
        record = dict()
        for name, seed in self.properties.items():
            record[name] = seed.get(index=index)
        return record

    def _str(self, val):
        if type(val) is str:
            return f"'{val}'"
        elif type(val) is int:
            return str(val) 
        else:
            return str(val)
