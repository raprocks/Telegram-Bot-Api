from typing import Dict, Tuple
from .PhotoSize import PhotoSize


class UserProfilePhotos:
    def __init__(self, user_profile_data: Dict):
        self.total_count: int = user_profile_data['total_count']
        self.photos: Tuple[PhotoSize, ...] = user_profile_data['photos']
