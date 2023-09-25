def modifyQuestionTemplate():
    format = """Given an input question in english and a database schema, change any words that are referencing a column, and replace them with the explicit column name.
    

For this Problem you can use the following table Schema:

Some example responses:
<example>
<table_schema>
CREATE TABLE covid_vaccinations(
  STATISTIC_CODE varchar(10),
  Statistic_Label varchar(30),
  `TLIST(M1)` int,
  Month varchar(20),
  `C03898V04649` varchar(30),
  `Local Electoral Area` varchar(50),
  `C02076V03371` varchar(10),
  `Age Group` varchar(30),
  `UNIT` varchar(10),
  `VALUE` float
);
</table_schema>
<question>
What was the biggest vaccination rate achieved?
</question>
<result>
What was the biggest vaccination VALUE achieved?
</result>
</example>

<example>
<table_schema>
CREATE TABLE covid_vaccinations(
  STATISTIC_CODE varchar(10),
  Statistic_Label varchar(30),
  `TLIST(M1)` int,
  Month varchar(20),
  `C03898V04649` varchar(30),
  `Local Electoral Area` varchar(50),
  `C02076V03371` varchar(10),
  `Age Group` varchar(30),
  `UNIT` varchar(10),
  `VALUE` float
);
</table_schema>
<question>
What's the statistic code used for fully vaccinated?
</question>
<result>
What is the STATISTIC_CODE used for fully vaccinated?
</result>
</example>

Your answer:

IMPORTANT: DO NOT OUTPUT SQL, just output modified natural language.

For this Problem you can use the following table Schema:
<table_schema>
{schema}
</table_schema>

<question>{input}</question>
Result: """
    return format

def generateConversationTemplate():
    format = """
Example of correct solution:
<example>
<table_schema>
CREATE TABLE tallest_buildings(
  rank int,
  name varchar(50),
  height_m float,
  height_ft float,
  year_built int,
  floors_above int,
  floors_below_ground int,
  city varchar(50),
  country varchar(50)
);
</table_schema>
<question>What's the height of Landmark 81 in meters?</question>
<query>SELECT height_m FROM tallest_buildings WHERE name='Landmark 81'</query>
</example>
<example>
<table_schema>
CREATE TABLE users(
  user_id int,
  username varchar(50),
  password varchar(50),
  is_admin bool
);
</table_schema>
<question>How many users are in the database?</question>
<query>SELECT count(*) FROM users</query>
</example>

<sql_schema>
{schema}
</sql_schema>

<question>{input}</question>

Given the input question and sql schema above, produce a valid SQL query to find the requested information.

NOTE: the query may ONLY use tables and columns that are present in the database schema above.

Query: """
    return format

def generateNaturalResponseTemplate():
    return """
Given an input question, and a response from a database, convert the database information into a natural language response, which is accurate to the information returned. If the database returns an error, kindly explain the error to the user. 

<question>
How many users in the system?
</question>
<data>
[(2,)]
</data>
There are currently two users in the system.

<question>
What's total orders value of non-admin users?
</question>
<data>
[(1400.0,)]
</data>
The total orders value of non-admin users is 1400. 

<question>
What's the statistic code used for fully vaccinated?
</question>
<data>
Error: (sqlite3.OperationalError) no such column: M1
[SQL: SELECT STATISTIC_CODE FROM COVID_VACCINATIONS WHERE TLIST(M1);]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
</data>
Unfortunately, there is no such statistic code available for "fully vaccinated".

<question>
{input}
</question>

<data>
{data}
</data>

Response: """