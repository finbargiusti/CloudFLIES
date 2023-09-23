from langchain.utilities import SQLDatabase
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from template import generateTemplate


class DBObject():
    db: SQLDatabase
    chain: ConversationChain

    def __init__(self, db: SQLDatabase, llm):
        self.db = db
        chat_template = PromptTemplate(template=generateTemplate(self.get_schema(), ), input_variables=["history", "input"])
        self.chain = ConversationChain(
                prompt=chat_template,
                llm=llm,
                memory=ConversationBufferMemory(k=4),
        )


    def get_schema(self) -> str:
        return self.db.get_table_info()

    def make_query(
        self, question: str, hints: list[str]
    ) -> str:
        return self.chain.predict(
            input=f"Question: {question} \nTable name hints: {', '.join(hints)}"
        )

