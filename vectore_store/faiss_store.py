from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
import os

embeddings = OpenAIEmbeddings()

def store_in_vector_db(summary: str, analysis: str, metadata: dict):
    text = str(summary) + "\n\n" + str(analysis)
    document = Document(page_content=text, metadata=metadata)

    if os.path.exists("faiss_index"):
        db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    else:
        db = FAISS.from_documents([document], embeddings)

    db.add_documents([document])
    db.save_local("faiss_index")
