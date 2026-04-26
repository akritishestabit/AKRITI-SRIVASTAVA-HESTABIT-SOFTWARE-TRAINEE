from src.retriever.hybrid_retriever import HybridRetriever
from src.pipelines.context_builder import ContextBuilder


def main():
    retriever = HybridRetriever()
    context_builder = ContextBuilder()

    while True:
        query = input("\nEnter your query (or 'exit'): ")

        if query.lower() == "exit":
            break

        
        chunks = retriever.retrieve(query)

        context = context_builder.build(chunks)

        print("\n🔹 FINAL CONTEXT:\n")
        print(context)


if __name__ == "__main__":
    main()