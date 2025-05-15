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
    host=os.getenv("POSTGRES_HOST"),
    port=int(os.getenv("POSTGRES_PORT")),
    db_name=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    table_schema="public"
)


# Create an agent with the PostgresTools
agent = Agent(tools=[postgres_tools],
              model=Groq(id="llama-3.3-70b-versatile"))

agent.print_response("Liste todas as tabelas do banco de dados", markdown=True)

agent.print_response("""
Faça uma query para pegar todas as cotações de bitcoin
""")
