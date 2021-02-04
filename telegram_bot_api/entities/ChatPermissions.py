from typing import Dict, Optional


class ChatPermissions:
    def __init__(self, permission_data: Dict):
        self.can_send_messages = permission_data.get('can_send_messages', None)
        self.can_send_media_messages: Optional[bool] = permission_data.get(
            'can_send_media_messages', None)
        self.can_send_polls: Optional[bool] = permission_data.get(
            'can_send_polls', None)
        self.can_send_other_messages: Optional[bool] = permission_data.get(
            'can_send_other_messages', None)
        self.can_add_web_page_previews: Optional[bool] = permission_data.get(
            'can_add_web_page_previews', None)
        self.can_change_info: Optional[bool] = permission_data.get(
            'can_change_info', None)
        self.can_invite_users: Optional[bool] = permission_data.get(
            'can_invite_users', None)
        self.can_pin_messages: Optional[bool] = permission_data.get(
            'can_pin_messages', None)
