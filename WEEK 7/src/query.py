# from retriever.hybrid_retriever import HybridRetriever

# hr = HybridRetriever()

# question = "Find the record where Organization Id is 5Cd7efccCcba38f"

# results = hr.retrieve(question)

# print("\n Hybrid Results:\n")

# for i, r in enumerate(results):
#     print(f"Result {i+1}:")
#     print("Text:", r["text"][:300])
#     print("Source:", r["source"])
#     print("Type:", r.get("type", "unknown"))
#     print("-" * 60)


from retriever.hybrid_retriever import HybridRetriever
from pipelines.context_builder import ContextBuilder

hr = HybridRetriever()
cb = ContextBuilder()

question = "Find record where Organization Id is 4e0719FBE38e0aB"

chunks = hr.retrieve(question)

context = cb.build(chunks)

print("\n FINAL CONTEXT:\n")

print(context)