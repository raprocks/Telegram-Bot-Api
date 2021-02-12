from typing import Dict, Optional
from ..base_objects.File import File


class PhotoSize(File):
    def __init__(self, photo_size_data: Dict):
        super().__init__(photo_size_data)
        self.width: int = photo_size_data['width']
        self.height: int = photo_size_data['height']
        self.file_size: Optional[int] = photo_size_data.get('file_size')
