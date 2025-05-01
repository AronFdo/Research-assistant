# tools/web_search_tool.py

from langchain_core.tools import tool
from duckduckgo_search import DDGS

@tool
def web_search(query: str) -> str:
    """Searches the web using DuckDuckGo and returns relevant results."""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)
        if not results:
            return "No results found."
        return "\n\n".join([f"{r['title']}\n{r['href']}\n{r['body']}" for r in results])
