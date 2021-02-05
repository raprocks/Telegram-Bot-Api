from typing import Dict


class PollOption:
    def __init__(self, poll_option_data: Dict):
        self.text: str = poll_option_data.get('text')
        self.voter_count: int = poll_option_data.get('voter_count')
