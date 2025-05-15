from agno.agent import Agent
from agno.tools.postgres import PostgresTools
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize PostgresTools with connection details
postgres_tools = PostgresTools(
    host="dpg-d0iggcbe5dus73dt0jhg-a.ohio-postgres.render.com",
    port=5532,
    db_name="dbname_4ocy",
    user="dbname_4ocy_user",
    password="pOSe9EZpXT402mHTMha0jsQYMhHi1i5K",
    table_schema="public",
)

# Create an agent with the PostgresTools
agent = Agent(tools=[postgres_tools],
              model=Groq(id="llama-3.3-70b-versatile"))

agent.print_response("Liste todas as tabelas do banco de dados", markdown=True)

agent.print_response("""
Faça uma query para pegar todas as cotações de bitcoin
""")
