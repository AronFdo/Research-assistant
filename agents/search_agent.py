# agents/search_agent.py

from crewai import Agent
from langchain_openai import ChatOpenAI
from tools.web_search_tool import MyCustomDuckDuckGoTool

def create_search_agent():
    return Agent(
        role="Web Researcher",
        goal="Search the internet for the most relevant and recent data.",
        backstory="You're a web data expert who excels at finding accurate, up-to-date info.",
        tools=[MyCustomDuckDuckGoTool()],
        llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)
    )
