# 📊 Business Data Q&A System using RAG (Retrieval-Augmented Generation)

## 🧠 Problem Statement
Large Language Models (LLMs) cannot access or reason over private business data such as sales records or internal reports. This limits their usefulness in real-world business decision-making. This project solves that by building a Retrieval-Augmented Generation (RAG) system that retrieves relevant business data and uses it to generate accurate, context-aware answers to user queries.

## 🚀 Project Overview
This project implements an end-to-end RAG pipeline that allows users to ask natural language questions on structured business data. The system converts structured data into meaningful text, generates embeddings for semantic understanding, retrieves relevant data using FAISS vector search, and uses a locally hosted LLM via Ollama to generate answers. A hybrid approach is used where analytical queries are handled using pandas for accurate computation and descriptive queries are handled using RAG with an LLM.

## 🏗️ Architecture
User Query → Embedding (Sentence Transformers) → Vector Search (FAISS) → Retrieve Relevant Context → LLM (Ollama Local Model) → Final Answer

## ⚙️ Tech Stack
Python, Pandas, NumPy, FAISS (Vector Search), Sentence Transformers (Embeddings), Ollama (Local LLM)

## 📂 Project Structure
rag-business-qa/
data/superstore.csv
src/data_loader.py
src/embedder.py
src/vector_store.py
src/retriever.py
src/generator.py
src/main.py
requirements.txt
README.md

## ▶️ How to Run Locally
1. Clone Repository
git clone <your-repo-link>
cd rag-business-qa

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Install & Run Ollama (Important)
Make sure Ollama is installed and running
ollama run llama3
(or use your model: llama3.2:3b-instruct-q4_K_M)

5. Run the Project
python src/main.py

## 💬 Example Queries
Which region has highest sales?
What is the top selling product?
Describe customer segments
What trends do you see in sales?

## 🧠 Key Concepts Used
Retrieval-Augmented Generation (RAG), Semantic Search using Embeddings, Vector Search with FAISS, Hybrid Query Handling (Pandas + LLM), Local LLM Inference using Ollama

## 🎯 Key Highlights
Built end-to-end RAG pipeline from scratch, integrated structured business data with LLM reasoning, avoided incorrect aggregation using pandas-based computation, designed hybrid system for accurate and reliable responses

## 🔮 Future Improvements
Improve retrieval using advanced embedding models, implement real-time data pipeline, add Streamlit dashboard for interaction, optimize LLM response latency, experiment with agent-based workflows using LangChain
