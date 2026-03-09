import os
import warnings
from langchain_chroma import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader

# Suppress noisy torch/dataloader warnings on CPU
warnings.filterwarnings("ignore", message=".*pin_memory.*")

class MathRAG:
    def __init__(self):
        # Explicitly use CPU for FastEmbed to avoid overhead
        self.embeddings = FastEmbedEmbeddings(providers=["CPUExecutionProvider"])
        self.persist_dir = "./chroma_db"
        self.vector_db = None
        
        # Load from disk if exists, else build it
        if os.path.exists(self.persist_dir):
            self.vector_db = Chroma(persist_directory=self.persist_dir, embedding_function=self.embeddings)
        elif os.path.exists("knowledge_base"):
            self.load_knowledge()

    def load_knowledge(self):
        loader = DirectoryLoader("knowledge_base", glob="./*.md", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)
        self.vector_db = Chroma.from_documents(
            documents=chunks, 
            embedding=self.embeddings, 
            persist_directory=self.persist_dir
        )

    def retrieve(self, query):
        if not self.vector_db: return "No formula context found."
        docs = self.vector_db.similarity_search(query, k=2)
        return "\n\n".join([f"Formula Source: {d.metadata.get('source')}\nContent: {d.page_content}" for d in docs])