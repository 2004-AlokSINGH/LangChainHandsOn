from langchain_community.document_loaders import YoutubeLoader
from ingestion.base import BaseLoader

class YouTubeIngestor(BaseLoader):

    def load(self, source: str):
        loader = YoutubeLoader.from_youtube_url(
            source,
            add_video_info=True
        )
        return loader.load()
