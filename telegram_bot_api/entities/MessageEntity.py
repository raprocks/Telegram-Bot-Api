from typing import Dict, Optional
from .User import User


class MessageEntity:
    def __init__(self, entity_data: Dict):
        self.entity_type: str = entity_data.get('type', '')
        self.offset: int = entity_data['offset']
        self.length: int = entity_data['length']
        self.url: Optional[str] = entity_data.get('url')
        self.user: Optional[User] = entity_data.get('user', None)
        self.language: Optional[str] = entity_data.get('language')
