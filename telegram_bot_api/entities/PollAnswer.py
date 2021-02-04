from .User import User
from typing import Dict


class PollAnswer:
    def __init__(self, poll_data: Dict):
        self.poll_id = poll_data.get('poll_id', None)
        self.user: User = poll_data.get('user', None)
        self.option_ids: tuple[int, ...] = poll_data.get('option_ids', None)
