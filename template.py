from langchain.prompts import ChatPromptTemplate


def generateTemplate():
    format = """Based on the table schema and array of related hints blow, write a SQL query that would answer the user's question

Schema:
{schema}

Hints:
{hints}

Question: {question}
SQL Query:"""
    return ChatPromptTemplate.from_template(format)
