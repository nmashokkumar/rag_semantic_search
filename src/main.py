from data_loader import load_data, convert_to_text
from embedder import Embedder
from vector_store import VectorStore
from retriever import Retriever
from generator import Generator


def handle_analytical_query(query, df):
    query_lower = query.lower()

    # Highest sales by region
    if "highest sales" in query_lower and "region" in query_lower:
        result = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
        return f"{result.idxmax()} region has the highest total sales."

    # Most profitable category
    if "most profitable" in query_lower and "category" in query_lower:
        result = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
        return f"{result.idxmax()} category is the most profitable."

    # Top selling product
    if (
    "top selling product" in query_lower
    or "highest selling product" in query_lower
    or "most sold product" in query_lower
    ):
        result = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)
        return f"{result.idxmax()} is the top selling product with total sales of {round(result.max(), 2)}."
        return None  # fallback to RAG


def main():
    print("🔄 Loading data...")
    df = load_data("../data/superstore.csv")
    documents = convert_to_text(df)

    print("🔄 Generating embeddings (one-time process)...")
    embedder = Embedder()
    embeddings = embedder.encode(documents)

    print("🔄 Building vector store...")
    dimension = len(embeddings[0])
    vector_store = VectorStore(dimension)
    vector_store.add(embeddings, documents)

    retriever = Retriever(embedder, vector_store)
    generator = Generator()

    print("\n✅ System Ready! Ask your business questions.\n")

    while True:
        query = input("💬 Ask a question (or type 'exit'): ")

        if query.lower() == "exit":
            print("👋 Exiting...")
            break

        # Step 1: Try analytical handling
        analytical_answer = handle_analytical_query(query, df)

        if analytical_answer:
            print("\n📊 Answer (Data Analysis):")
            print(analytical_answer)
            continue

        # Step 2: Use RAG for descriptive queries
        context = retriever.retrieve(query, k=20)
        context_text = "\n".join(context)

        answer = generator.generate(query, context_text)

        print("\n🤖 Answer (RAG):")
        print(answer)


if __name__ == "__main__":
    main()