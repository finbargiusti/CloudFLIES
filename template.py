def generateConversationTemplate(schema: str):
    format = """You are an AI chatbot designed to create SQL queries based on a schema, a series of table name hints, and inputs from the user.

Schema:
"""+schema+"""

History: 
{history}

{input}
SQL Query:"""
    return format

def generateVerificationTemplate(schema: str):
    format = """You are an AI system designed to determine if the answer to a natural language query can be found in the database described in the schema below. If the answer can be found, you will simply respond "True", otherwise you will respond "False". 

Schema:
"""+schema+"""

{input}
Response:"""
    return format
