import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from src.hybrid_search import HybridRetriever

load_dotenv()


def load_rag_chain():

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

    hybrid = HybridRetriever()

    prompt = ChatPromptTemplate.from_template(
        """
You are an intelligent document assistant.

Use ONLY the provided context.

If the answer is not present in the context, say:

"I could not find this information in uploaded documents."

Do not hallucinate.

Context:
{context}

Question:
{question}

Answer:
"""
    )

    def ask(query):

        docs = hybrid.retrieve(
            query=query,
            k_vector=3,
            k_bm25=3,
            final_k=5
        )

        confidence = hybrid.get_confidence(
            query
        )

        context = "\n\n".join(
            [
                doc.page_content
                for doc in docs
            ]
        )

        messages = prompt.format_messages(
            context=context,
            question=query
        )

        response = llm.invoke(
            messages
        )

        return {
            "answer": response.content,
            "context": docs,
            "confidence": confidence
        }

    return ask