import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(BASE_DIR)

import json
from datetime import datetime
import streamlit as st

from src.memory.memory_store import MemoryStore
from src.pipelines.context_builder import ContextBuilder
from src.retriever.hybrid_retriever import HybridRetriever
from src.retriever.image_search import ImageSearch
from src.pipelines.sql_pipeline import SQLPipeline
from src.evaluation.rag_eval import RAGEvaluator
from src.evaluation.refiner import Refiner

LOG_PATH = "CHAT-LOGS.json"



class ChatLogger:
    def __init__(self, log_path=LOG_PATH):
        self.log_path = log_path

        if not os.path.exists(self.log_path):
            with open(self.log_path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

    def log(self, mode, query, answer, confidence=None):
        try:
            with open(self.log_path, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except Exception:
            logs = []

        logs.append({
            "timestamp": datetime.now().isoformat(),
            "mode": mode,
            "query": query,
            "answer": answer,
            "confidence": confidence,
        })

        with open(self.log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4)



memory = MemoryStore()
logger = ChatLogger()


@st.cache_resource
def load_text_modules():
    return HybridRetriever(), ContextBuilder()


@st.cache_resource
def load_image_module():
    return ImageSearch()


@st.cache_resource
def load_sql_module():
    return SQLPipeline()


@st.cache_resource
def load_evaluator():
    return RAGEvaluator()


@st.cache_resource
def load_refiner():
    return Refiner()



st.set_page_config(page_title="Week 7 RAG Assistant", layout="wide")
st.title("Week 7 Advanced RAG Assistant")

mode = st.sidebar.selectbox("Choose mode", ["Text QA", "Image QA", "SQL QA"])

if st.sidebar.button("Clear Memory"):
    memory.clear_memory()
    st.sidebar.success("Memory cleared")

st.sidebar.subheader("Recent Memory")
st.sidebar.text(memory.get_recent_context() or "No recent memory")


# Text QA
if mode == "Text QA":
    st.header("Text Question Answering")

    query = st.text_input("Ask about your documents")

    if st.button("Ask") and query:
        retriever, context_builder = load_text_modules()
        evaluator = load_evaluator()
        refiner = load_refiner()

        chunks = retriever.retrieve(query)
        context = context_builder.build(chunks)

        answer = context

        eval_result = evaluator.evaluate(context, answer)

        if not eval_result["faithful"]:
            answer = refiner.refine(query, context, answer)

        memory.add_message("user", query)
        memory.add_message("assistant", answer)
        logger.log("text", query, answer, eval_result["confidence"])

        st.subheader("Answer")
        st.write(answer)
        st.caption(f"Confidence: {eval_result['confidence']}")



elif mode == "Image QA":
    st.header("Image Question Answering")

    image_mode = st.selectbox(
        "Choose Image Mode",
        ["Text → Image", "Image → Image", "Image → Text"]
    )

    searcher = load_image_module()
    evaluator = load_evaluator()

    # TEXT → IMAGE
    if image_mode == "Text → Image":
        query = st.text_input("Enter text query")

        if st.button("Search") and query:
            results = searcher.text_to_image(query)

            st.subheader("Results")
            st.write(results["message"])  

            if not results["results"]:
                st.warning("No results found")
            else:
                for r in results["results"]:  
                    image_path = os.path.join("src/data/raw/images", r["image"])
                    st.image(image_path, caption=r["caption"], width=300)

    # IMAGE → IMAGE
    elif image_mode == "Image → Image":
        uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

        if uploaded_file is not None:
            temp_path = f"temp_{uploaded_file.name}"

            with open(temp_path, "wb") as f:
                f.write(uploaded_file.read())

            results = searcher.image_to_image(temp_path)

            st.image(temp_path, caption="Uploaded image", width=300)
            st.subheader("Similar Images")
            st.write(results["message"])  

            if not results["results"]:
                st.warning("No results found")
            else:
                for r in results["results"]:  
                    image_path = os.path.join("src/data/raw/images", r["image"])
                    st.image(image_path, caption=r["caption"], width=300)

            os.remove(temp_path)

    # IMAGE → TEXT
    elif image_mode == "Image → Text":
        uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

        if uploaded_file is not None:
            temp_path = f"temp_{uploaded_file.name}"

            with open(temp_path, "wb") as f:
                f.write(uploaded_file.read())

            answer = searcher.image_to_text(temp_path)

            context = answer
            eval_result = evaluator.evaluate(context, answer)

            memory.add_message("user", f"Image uploaded: {uploaded_file.name}")
            memory.add_message("assistant", answer)
            logger.log("image", uploaded_file.name, answer, eval_result["confidence"])

            st.subheader("Uploaded Image")
            st.image(temp_path, width=300)

            st.subheader("Answer")
            st.write(answer)
            st.caption(f"Confidence: {eval_result['confidence']}")

            os.remove(temp_path)


# SQL QA
elif mode == "SQL QA":
    st.header("SQL Question Answering")

    query = st.text_input("Ask about your database")

    if st.button("Run SQL") and query:
        sql_pipeline = load_sql_module()

        sql = sql_pipeline.generator.generate_sql(query)

        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        if not sql_pipeline.validate_query(sql):
            st.error("Unsafe SQL query")
        else:
            columns, result = sql_pipeline.execute_query(sql)

            if columns is None:
                st.error(f"SQL Error: {result}")
            else:
                answer = sql_pipeline.summarize_result(columns, result)

                st.subheader("Answer")
                st.write(answer)