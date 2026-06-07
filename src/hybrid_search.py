from rank_bm25 import BM25Okapi

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


DB_FAISS_PATH = "vector_store/db_faiss"


class HybridRetriever:

    def __init__(self, db_path=DB_FAISS_PATH):

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = FAISS.load_local(
            db_path,
            self.embeddings,
            allow_dangerous_deserialization=True
        )

        self.documents = list(
            self.db.docstore._dict.values()
        )

        self.corpus = [
            doc.page_content
            for doc in self.documents
        ]

        tokenized_corpus = [
            text.split()
            for text in self.corpus
        ]

        self.bm25 = BM25Okapi(
            tokenized_corpus
        )

    def retrieve(
        self,
        query,
        k_vector=3,
        k_bm25=3,
        final_k=5
    ):

        # -------------------------
        # Vector Search
        # -------------------------

        vector_docs = self.db.similarity_search(
            query,
            k=k_vector
        )

        # -------------------------
        # BM25 Search
        # -------------------------

        tokenized_query = query.split()

        bm25_docs = self.bm25.get_top_n(
            tokenized_query,
            self.documents,
            n=k_bm25
        )

        # -------------------------
        # Merge Results
        # -------------------------

        combined = []
        seen = set()

        for doc in (vector_docs + bm25_docs):

            text = doc.page_content

            if text not in seen:

                combined.append(doc)

                seen.add(text)

        return combined[:final_k]

    def get_confidence(
        self,
        query
    ):

        docs = self.db.similarity_search_with_score(
            query,
            k=1
        )

        if len(docs) == 0:

            return "Low"

        score = docs[0][1]

        if score < 1.5:

            return "High"

        elif score < 3:

            return "Medium"

        else:

            return "Low"