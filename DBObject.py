from langchain.utilities import SQLDatabase
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain, LLMChain
from langchain.memory import ConversationBufferMemory
from template import generateConversationTemplate, generateVerificationTemplate


class DBObject():
    db: SQLDatabase
    chat_chain: ConversationChain
    verify_chain: LLMChain

    def __init__(self, db: SQLDatabase, llm):
        self.db = db

        schema = self.get_schema()
        

        chat_template = PromptTemplate(template=generateConversationTemplate(schema, ), input_variables=["history", "input"])
        self.chat_chain = ConversationChain(
                prompt=chat_template,
                llm=llm,
                memory=ConversationBufferMemory(k=4),
        )

        verify_template = PromptTemplate.from_template(generateVerificationTemplate(schema))

        self.verify_chain = LLMChain(
            prompt=verify_template,
            llm=llm
        )


    def get_schema(self) -> str:
        return self.db.get_table_info()

    def make_query(
        self, question: str, hints: list[str]
    ) -> str:

        concat_input = f"Question: {question} \nTable name hints: {', '.join(hints)}"

        sql_query = self.chat_chain.predict(
            input= concat_input
        )

        verification_result = self.verify_chain.predict(input=sql_query)
        
        invalid_response = """
I'm sorry, I'm not sure how to answer that given this database.
        """

        if verification_result.lower().strip() == "true":
            return invalid_response

        try:
            response = self.db.run(sql_query)
        except (e):
            return """
An unexpected error occured.
            """
