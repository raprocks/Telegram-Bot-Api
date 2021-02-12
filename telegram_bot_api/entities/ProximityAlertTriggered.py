from typing import Dict
from .User import User


class ProximityAlertTriggered:
    def __init__(self, proximity_data: Dict):
        self.traveler: User = User(proximity_data['traveler'])
        self.watcher: User = User(proximity_data['watcher'])
        self.distance: int = proximity_data['distance']
