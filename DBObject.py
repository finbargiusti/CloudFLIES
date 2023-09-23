import SchemaScraper
import sqlite3

def DBObject():

    schema: str
    db: sqlite3.Connection

    def __init__(self, db: sqlite3.Connection):
        scraper = SchemaScraper(db)

        self.db = db
        self.schema = scraper.get_schema()
