from typing import Dict, Optional
from ..base_objects.File import File
from .PhotoSize import PhotoSize


class Video(File):
    def __init__(self, video_data: Dict):
        super().__init__(video_data)
        self.width: int = video_data['width']
        self.height: int = video_data['height']
        self.duration: int = video_data['duration']
        self.thumb: Optional[PhotoSize] = PhotoSize(video_data.get('thumb'))
        self.file_name: str = video_data.get('file_name')
        self.mime_type: Optional[str] = video_data.get('mime_type')
        self.file_size: Optional[int] = video_data.get('file_size')
