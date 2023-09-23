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
    format = """You are an AI assistant whose purpose is to determine if an SQL query is valid, given the database schema. You must output "True" if the query is valid, and "False" otherwise.

Schema:
"""+schema+"""

Query: {input}
Response:"""
    return format
