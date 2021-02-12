from .Location import Location
from typing import Dict, Optional


class Venue:
    def __init__(self, venue_data: Dict):
        self.location: Location = Location(venue_data['location'])
        self.title: str = venue_data['title']
        self.address: str = venue_data['address']
        self.foursquare_id: Optional[str] = venue_data.get('foursquare_id')
        self.foursquare_type: Optional[str] = venue_data.get('foursquare_type')
