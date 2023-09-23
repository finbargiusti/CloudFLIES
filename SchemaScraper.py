import sqlite3


class SchemaScraper:

    # TODO: maybe add strategy injection
    def __init__(self, db: sqlite3.Connection):
        return

    def connect_function(self, name: str):
        return sqlite3.connect(name)

    def get_schema(self) -> str:
        return ""


if __name__ == "__main__":
    # some testing code
    pass
