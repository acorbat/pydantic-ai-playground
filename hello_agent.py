from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    "google-gla:gemini-2.5-flash",
    instructions="You're a Python Expert. Reply in one sentence.",
)

result = agent.run_sync("What is Pydantic AI?")
print(result.output)