# tools/my_duckduckgo_tool.py

from crewai.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchRun

class MyCustomDuckDuckGoTool(BaseTool):
    name: str = "DuckDuckGo Search Tool"
    description: str = "Search the web for a given query and return relevant results."

    def _run(self, query: str) -> str:
        duckduckgo_tool = DuckDuckGoSearchRun()
        return duckduckgo_tool.run(query)
