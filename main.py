from crewai import Crew, Task
from agents.analyzer_agent import create_analyzer_agent
from agents.search_agent import create_search_agent
from agents.summarizer_agent import create_summarizer_agent
from utils.pdf_generator import save_to_pdf
from vectore_store.faiss_store import store_in_vector_db

def run_research_agent(query: str):
    search_agent = create_search_agent()
    summarizer_agent = create_summarizer_agent()
    analyzer_agent = create_analyzer_agent()

    search_task = Task(
        description=f"Research the topic: {query}",
        agent=search_agent,
        expected_output=f"A detailed list of findings with sources related to: {query}"
    )

    summarize_task = Task(
        description=(
            f"Create a long, detailed summary of the research on '{query}'.\n"
            "The summary should cover:\n"
            "- All key points and insights\n"
            "- Logical structure (intro, body, conclusion)\n"
            "- Properly cite all sources (e.g., [1], [2]) with URLs or names.\n"
            "Length: At least 5 paragraphs."
        ),
        agent=summarizer_agent,
        expected_output="A 5+ paragraph, well-organized summary with full source citations.",
        context=[search_task]
    )

    analyze_task = Task(
        description=(
            f"Take the detailed summary of the topic '{query}' and provide an analysis report with:\n"
            "- 🧠 Key actionable insights\n"
            "- ✅ Suggested next steps or projects\n"
            "- 🔍 Related areas/topics worth exploring further\n"
            "Ensure recommendations are practical and relevant."
        ),
        agent=analyzer_agent,
        expected_output="An organized analysis with bullet points for insights, actions, and related research ideas.",
        context=[summarize_task]
    )

    crew = Crew(
        agents=[search_agent, summarizer_agent, analyzer_agent],
        tasks=[search_task, summarize_task, analyze_task],
        verbose=True
    )

    result = crew.kickoff()
    summary = summarize_task.output

    # Save to PDF
    pdf_path = save_to_pdf(summary, result, query)

    # Store in vector DB
    store_in_vector_db(
        summary=summary,
        analysis=result,
        metadata={"query": query, "pdf_path": pdf_path}
    )

    return summary, result, pdf_path
