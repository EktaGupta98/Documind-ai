from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    Docx2txtLoader,
)

from langchain_community.document_loaders.excel import (
    UnstructuredExcelLoader
)

from langchain_community.document_loaders import JSONLoader


def load_documents(data_dir="data"):

    documents = []

    path = Path(data_dir)

    for file in path.rglob("*"):

        try:

            if file.suffix == ".pdf":
                loader = PyPDFLoader(str(file))

            elif file.suffix == ".txt":
                loader = TextLoader(str(file))

            elif file.suffix == ".csv":
                loader = CSVLoader(str(file))

            elif file.suffix == ".docx":
                loader = Docx2txtLoader(str(file))

            elif file.suffix == ".xlsx":
                loader = UnstructuredExcelLoader(str(file))

            elif file.suffix == ".json":
                loader = JSONLoader(
                    file_path=str(file),
                    jq_schema=".",
                    text_content=False
                )

            else:
                continue

            loaded_docs = loader.load()

            for doc in loaded_docs:

                doc.metadata["file_type"] = file.suffix

            documents.extend(loaded_docs)

        except Exception as e:

            print(
                f"Error loading {file}: {e}"
            )

    return documents