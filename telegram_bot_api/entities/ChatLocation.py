from typing import Dict
from .Location import Location


class ChatLocation:
    def __init__(self, location_data: Dict):
        self.location: Location = Location(location_data.get('location', {}))
        self.address: str = location_data.get('address', '')
