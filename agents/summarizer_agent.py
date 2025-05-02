from crewai import Agent
from langchain_openai import ChatOpenAI

def create_summarizer_agent():
    return Agent(
        role="AI Research Summarizer",
        goal="Generate a comprehensive summary with detailed explanations and citations.",
        backstory="You're an expert at turning raw research into extended, well-organized summaries with proper source attributions.",
        llm=ChatOpenAI(model="gpt-4", temperature=0.5)
    )
