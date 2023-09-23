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
    format = """You are an AI assistant whose purpose is to determine if an SQL query will return an error. You must output "True" if the query will return an error, and "False" otherwise.

Schema:
"""+schema+"""

Query: {input}
Response:"""
    return format
