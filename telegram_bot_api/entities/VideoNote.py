from typing import Dict, Optional
from ..base_objects.File import File
from .PhotoSize import PhotoSize


class VideoNote(File):
    def __init__(self, videonote_data: Dict[str, str, int]):
        super().__init__(videonote_data)
        self.length: int = int(videonote_data['length'])
        self.duration: int = int(videonote_data['duration'])
        self.thumb: Optional[PhotoSize] = PhotoSize(
            videonote_data.get('thumb', {}))
        self.file_size: Optional[int] = int(videonote_data.get('file_size', 0))
