from typing import Dict, Optional
from ..base_objects.File import File
from .PhotoSize import PhotoSize


class Animation(File):
    def __init__(self, animation_data: Dict):
        super().__init__(animation_data)
        self.width: int = animation_data['width']
        self.height: int = animation_data['height']
        self.duration: int = animation_data['duration']
        self.thumb: Optional[PhotoSize] = PhotoSize(
            animation_data.get('thumb', {}))
        self.file_name: Optional[str] = animation_data.get('file_name')
        self.mime_type: Optional[str] = animation_data.get('mime_type')
        self.file_size: Optional[int] = animation_data.get('file_size')
