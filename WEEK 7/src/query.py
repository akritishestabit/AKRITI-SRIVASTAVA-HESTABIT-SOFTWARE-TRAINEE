from retriever.query_engine import QueryEngine


qe = QueryEngine()


question = "Find the record where where country is El Salvador and show its details"


results = qe.query(question)

print("\n🔍 Top Results:\n")

for i, r in enumerate(results):
    print(f"Result {i+1}:")
    print("Text:", r["text"][:400])
    print("Source:", r["source"])
    print("Type:", r.get("type", "unknown"))
    print("-" * 60)