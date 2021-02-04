from typing import Optional, Dict
from .ChatPhoto import ChatPhoto
from .ChatPermissions import ChatPermissions
from .Message import Message
from .ChatLocation import ChatLocation

class Chat:
    def __init__(self, chat_data: Dict):
        self.id: int = chat_data['id']
        self.type: str = chat_data['type']
        self.title: str = chat_data['title']
        self.username: Optional[str] = chat_data.get('username', None)
        self.first_name: Optional[str] = chat_data.get('first_name', None)
        self.last_name: Optional[str] = chat_data.get('last_name', None)
        self.photo: Optional[ChatPhoto] = chat_data.get('photo', None)
        self.description: Optional[str] = chat_data.get('description', None)
        self.invite_link: Optional[str] = chat_data.get('invite_link', None)
        self.pinned_message: Optional[Message] = chat_data.get(
            'pinned_message', None)
        self.permissions: Optional[ChatPermissions] = chat_data.get(
            'permissions', None)
        self.slow_mode_delay: Optional[int] = chat_data.get(
            'slow_mode_delay', None)
        self.sticker_set_name: Optional[str] = chat_data.get(
            'sticker_set_name', None)
        self.can_set_sticker_set: Optional[bool] = chat_data.get(
            'can_set_sticker_set', None)
        self.linked_chat_id: Optional[int] = chat_data.get('linked_chat_id', None)
        self.location: Optional[ChatLocation] = chat_data.get('location', None)
