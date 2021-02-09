from typing import Dict, Optional
from ..base_objects.File import File
from .PhotoSize import PhotoSize


class Audio(File):
    def __init__(self, audio_data: Dict):
        super().__init__(audio_data)
        self.duration: int = audio_data['duration']
        self.performer: Optional[str] = audio_data.get('performer')[
            'performer']
        self.title: Optional[str] = audio_data.get('title')
        self.file_name: Optional[str] = audio_data.get('file_name')
        self.mime_type: Optional[str] = audio_data.get('mime_type')
        self.file_size: Optional[int] = audio_data.get('file_size')
        self.thumb: Optional[PhotoSize] = PhotoSize(audio_data.get('thumb'))
