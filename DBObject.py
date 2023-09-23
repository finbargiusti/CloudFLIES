from langchain.utilities import SQLDatabase
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from template import generateTemplate


class DBObject:
    db: SQLDatabase
    prompt_template: ChatPromptTemplate

    def __init__(self, db: SQLDatabase):
        self.prompt_template = generateTemplate()
        self.db = db

    def get_schema(self) -> str:
        return self.db.get_table_info()

    def make_query(
        self, question: str, hints: list[str], chain: ConversationChain
    ) -> str:
        chain.prompt.template = self.prompt_template
        return chain.predict(
            question=question, hints=", ".join(hints), schema=self.get_schema()
        )
