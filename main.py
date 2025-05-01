# main.py

from agents.search_agent import create_search_agent

def main():
    agent = create_search_agent()
    query = input("Enter your research query: ")
    result = agent.execute(query)
    print("\n🔍 Results:\n", result)

if __name__ == "__main__":
    main()
