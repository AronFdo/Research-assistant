from tools.web_search import web_search

if __name__ == "__main__":
    query = "Latest AI Breakthroughs in 2025"
    results = web_search(query)

    for idx, result in enumerate(results, 1):
        print(f"{idx}, {result['title']}\n{result['snippet']}\n")
