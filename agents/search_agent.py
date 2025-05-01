# agents/search_agent.py

from crewai import Agent
from langchain_openai import ChatOpenAI
from tools.web_search_tool import web_search

def create_search_agent():
    return Agent(
        role="Web Researcher",
        goal="Find current, accurate data from the internet.",
        backstory="You are an internet research expert.",
        tools=[web_search],  # Correct tool format
        llm=ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")
    )
