from typing import Dict, Optional
from ..base_objects.File import File


class Voice(File):
    def __init__(self, voice_data: Dict):
        super().__init__(voice_data)
        self.duration: int = voice_data["duration"]
        self.mime_type: Optional[str] = voice_data.get('mime_type')
        self.file_size: Optional[int] = voice_data.get('file_size')
