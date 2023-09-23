from langchain.prompts import ChatPromptTemplate


def generateTemplate():
    format = """You are an AI chatbot designed to create SQL queries based on a schema, a series of table name hints, and inputs from the user.

Schema:
{schema}

Hints:
{hints}

History: 
{history}

Current Question: {question}
SQL Query:"""
    return format
