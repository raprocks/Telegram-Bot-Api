from typing import Dict, Optional

class Contact:
    def __init__(self, contact_data: Dict):
        self.phone_number: str = contact_data['phone_number']
        self.first_name: str = contact_data['first_name']
        self.last_name: Optional[str] = contact_data.get('last_name')
        self.user_id: Optional[int] = contact_data.get('user_id')
        self.vcard: Optional[str] = contact_data.get('vcard')
