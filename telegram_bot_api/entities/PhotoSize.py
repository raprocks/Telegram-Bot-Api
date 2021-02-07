from typing import Dict, Optional


class PhotoSize:
    def __init__(self, photo_size_data: Dict):
        self.file_id: str = photo_size_data['file_id']
        self.file_unique_id: str = photo_size_data['file_unique_id']
        self.width: int = photo_size_data['width']
        self.height: int = photo_size_data['height']
        self.file_size: Optional[int] = photo_size_data.get('file_size')
