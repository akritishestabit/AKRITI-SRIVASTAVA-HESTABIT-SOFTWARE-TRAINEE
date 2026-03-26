class ContextBuilder:
    def __init__(self, max_chunks=5):
        self.max_chunks = max_chunks

    def build(self, chunks):
        """
        chunks: list of retrieved chunks
        returns: formatted context string
        """

        # ---------------------------
        # 1. Limit chunks
        # ---------------------------
        selected_chunks = chunks[:self.max_chunks]

        # ---------------------------
        # 2. Remove duplicates
        # ---------------------------
        seen = set()
        unique_chunks = []

        for chunk in selected_chunks:
            text = chunk["text"]

            if text not in seen:
                seen.add(text)
                unique_chunks.append(chunk)

        # ---------------------------
        # 3. Format context
        # ---------------------------
        context_parts = []

        for i, chunk in enumerate(unique_chunks):
            formatted = (
                f"[Source: {chunk.get('source', 'unknown')} | "
                f"Page: {chunk.get('page', 'N/A')}]\n"
                f"{chunk['text']}\n"
            )
            context_parts.append(formatted)

        # ---------------------------
        # 4. Join everything
        # ---------------------------
        final_context = "\n---\n".join(context_parts)

        return final_context