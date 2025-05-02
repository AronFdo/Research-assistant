from crewai import Agent
from langchain_openai import ChatOpenAI

def create_analyzer_agent():
    return Agent(
        role="AI Research Analyzer",
        goal="Analyze summarized research and recommend next actions or related topics.",
        backstory="You're a strategic AI advisor that extracts insights and provides actionable follow-ups for deepening research.",
        llm=ChatOpenAI(model="gpt-4", temperature=0.7, max_tokens=1500)
    )
