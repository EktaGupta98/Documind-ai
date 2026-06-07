import streamlit as st
import os

from src.create_vectorstore import create_vectorstore
from src.rag_chain import load_rag_chain

st.set_page_config(
    page_title="DocuMind AI",
    layout="wide"
)

st.title("📚 DocuMind AI")

# ---------------------------
# Session State
# ---------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "processed" not in st.session_state:
    st.session_state.processed = False

# ---------------------------
# Sidebar
# ---------------------------

st.sidebar.header("📂 Upload Documents")

uploaded_files = st.sidebar.file_uploader(
    "Upload Files",
    accept_multiple_files=True,
    type=["pdf", "txt", "csv", "docx", "xlsx", "json"]
)

file_filter = st.sidebar.selectbox(
    "File Type",
    [
        "All",
        ".pdf",
        ".txt",
        ".csv",
        ".docx",
        ".xlsx",
        ".json"
    ]
)

if uploaded_files:

    os.makedirs("data", exist_ok=True)

    st.sidebar.write(
        f"📄 {len(uploaded_files)} file(s) selected"
    )

    st.sidebar.subheader("Files")

    for file in uploaded_files:

        st.sidebar.write(
            f"• {file.name}"
        )

        filepath = os.path.join(
            "data",
            file.name
        )

        if not os.path.exists(filepath):

            with open(filepath, "wb") as f:

                f.write(
                    file.getbuffer()
                )

    if st.sidebar.button(
        "🚀 Process Documents"
    ):

        with st.spinner(
            "Creating embeddings..."
        ):

            create_vectorstore()

            st.session_state.processed = True

        st.sidebar.success(
            f"✅ {len(uploaded_files)} document(s) indexed successfully!"
        )

# ---------------------------
# Stop if not processed
# ---------------------------

if not st.session_state.processed:

    st.info(
        "👈 Upload documents and click 'Process Documents' first."
    )

    st.stop()

# ---------------------------
# Chat History
# ---------------------------

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):

        st.markdown(
            msg["content"]
        )

# ---------------------------
# User Query
# ---------------------------

query = st.chat_input(
    "Ask anything from your documents..."
)

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message(
        "user"
    ):

        st.markdown(query)

    try:

        rag = load_rag_chain()

        response = rag(query)

        answer = response["answer"]

        confidence = response["confidence"]

        sources = []

        for doc in response["context"]:

            source = doc.metadata.get(
                "source",
                "Unknown"
            )

            page = doc.metadata.get(
                "page",
                "N/A"
            )

            sources.append(
                f"{os.path.basename(source)} (Page {page})"
            )

        with st.chat_message(
            "assistant"
        ):

            st.markdown(answer)

            st.metric(
                  "Retrieval Quality",
                    confidence
            )

            st.markdown(
                "### 📌 Sources"
            )

            for s in set(sources):

                st.write(s)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )