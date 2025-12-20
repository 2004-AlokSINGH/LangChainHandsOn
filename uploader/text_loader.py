from langchain_community.document_loaders import TextLoader
from ingestion.base import BaseLoader

class TxtIngestor(BaseLoader):

    def load(self, source: str):
        loader = TextLoader(source, encoding="utf-8")
        return loader.load()
