import SchemaScraper
import sqlite3

def DBObject():

    db: sqlite3.Connection

    def __init__(self, db: sqlite3.Connection):

        self.db = db

    def get_schema(self) -> str:
        scraper = SchemaScraper(db)
        return scraper.get_schema()

