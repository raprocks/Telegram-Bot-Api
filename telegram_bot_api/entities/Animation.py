from typing import Dict, Optional
from..base_objects.File import File


class Animation(File):
    def __init__(self, animation_data):
        super().__init__(animation_data)
        self.