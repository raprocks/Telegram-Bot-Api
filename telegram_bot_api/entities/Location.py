from typing import Optional, Dict


class Location:
    def __init__(self, location_data: Dict):
        self.longitude: float = location_data['longitude']
        self.latitude: float = location_data['latitude']
        self.horizontal_accuracy: Optional[float] = location_data.get(
            'horizontal_accuracy')
        self.live_period: Optional[int] = location_data.get('live_period')
        self.heading: Optional[int] = location_data.get('heading')
        self.proximity_alert_radius: Optional[int] = location_data.get(
            'proximity_alert_radius')
