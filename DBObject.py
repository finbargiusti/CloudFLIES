from langchain.utilities import SQLDatabase
from langchain.prompts import ChatPromptTemplate
from template import generateTemplate


class DBObject:
    db: SQLDatabase
    prompt_template: ChatPromptTemplate

    def __init__(self, db: SQLDatabase):
        self.prompt_template = generateTemplate()
        self.db = db

    def get_schema(self) -> str:
        return self.db.get_table_info()

    def generate_prompt(self, question: str, hints: list[str]) -> str:
        return self.prompt_template.format_prompt(
            schema=self.get_schema(), question=question, hints=", ".join(hints)
        ).to_string()


if __name__ == "__main__":
    # test generation

    db = SQLDatabase.from_uri("sqlite:///sampleDatabases/Northwind3.db?mode=ro")

    db_object = DBObject(db)

    print(db_object.generate_prompt("How many users have age over 45?", ["users"]))
