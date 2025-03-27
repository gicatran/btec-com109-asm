class Model():
    def __init__(self, table_name: str):
        self.table_name = table_name

    def __str__(self) -> str:
        raise NotImplementedError

    def parse_from_string(self, string):
        raise NotImplementedError