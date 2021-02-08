from typing import Dict, Optional
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(
    __file__, __name__, str(__package__)))
from ..base_objects.File import File
# from telegram_bot_api.base_objects.File import File


class PhotoSize(File):
    def __init__(self, photo_size_data: Dict):
        super().__init__(photo_size_data)
        self.width: int = photo_size_data['width']
        self.height: int = photo_size_data['height']
        self.file_size: Optional[int] = photo_size_data.get('file_size')
