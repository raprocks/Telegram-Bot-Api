from typing import Dict, Optional
from ..base_objects.File import File
from .PhotoSize import PhotoSize


class Document(File):
    def __init__(self, document_data: Dict):
        super().__init__(document_data)
        self.thumb: Optional[PhotoSize] = PhotoSize(document_data.get('thumb'))
        self.file_name: str = document_data.get('file_name')
        self.mime_type: Optional[str] = document_data.get('mime_type')
        self.file_size: Optional[int] = document_data.get('file_size')
