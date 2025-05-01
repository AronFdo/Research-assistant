## research-assistant-ai/README.md

# 🧠 Research Assistant AI

An AI agent that automates research by searching the web, summarizing content, and generating insightful analysis. Built with Crew AI, LangChain, DuckDuckGo, OpenAI, and FAISS.

---

## 🚀 Features
- Web search via DuckDuckGo
- Summarizes top results using OpenAI
- Analyzes insights and presents trends
- Modular Crew AI agent workflow

---

## 🛠️ Tech Stack
- Crew AI
- LangChain
- OpenAI
- DuckDuckGo Search API
- FAISS

---

## 📦 Installation
```bash
git clone https://github.com/your-username/research-assistant-ai.git
cd research-assistant-ai
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Add your `.env` with:
```env
OPENAI_API_KEY=your_key
```

---

## 🧩 File Structure
```
research-assistant-ai/
├── main.py
├── requirements.txt
├── agents/
│   ├── search_agent.py
│   ├── summarizer_agent.py
│   └── analyzer_agent.py
├── tools/web_search.py
├── vector_store/faiss_store.py
├── crew_config/config.yaml
└── prompts/summarize_prompt.txt
```

---

## 🧪 Run the Agent
```bash
python main.py
```

---

## ✅ Todo
- [ ] Web Search Agent
- [ ] Summarizer Agent
- [ ] Analyzer Agent
- [ ] Crew AI Orchestration
- [ ] FAISS Storage (Optional)

---

## 📄 License
MIT

---

## 🤝 Contributing
Pull requests welcome!

---

## ✨ Credits
Aron Fernando, built as part of AI Agent learning journey

---

## 🌐 Future Extensions
- Add UI using Streamlit
- Support for PDF & CSV summarization
- Trend visualization