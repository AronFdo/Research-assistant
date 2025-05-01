from duckduckgo_search import DDGS

def web_search(query: str, max_results: int = 5)-> list:
    results = []
    with DDGS() as ddgs:
        for result in ddgs.text(query, max_results=max_results):
            results.append({
                "title":result.get("title"),
                "link":result.get("href"),
                "snippet":result.get("body")
            })
    return results
