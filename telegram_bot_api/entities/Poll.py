from .PollOption import PollOption
from .MessageEntity import MessageEntity
from typing import List, Dict


class Poll:
    def __init__(self, poll_data: Dict):
        self.id: str = poll_data.get('id', None)
        self.question: str = poll_data.get('question', None)
        self.options: List[PollOption] = poll_data.get('options', None)
        self.total_voter_count: int = poll_data.get('total_voter_count', None)
        self.is_closed: bool = poll_data.get('is_closed', None)
        self.is_anonymous: bool = poll_data.get('is_anonymous', None)
        self.type: str = poll_data.get('type', None)
        self.allows_multiple_answers: bool = poll_data.get(
            'allows_multiple_answers', None)
        self.correct_option_id: int = poll_data.get('correct_option_id', None)
        self.explanation: str = poll_data.get('explanation', None)
        self.explanation_entities: List[MessageEntity] = poll_data.get(
            'explanation_entities', None)
        self.open_period: int = poll_data.get('open_period', None)
        self.close_date: int = poll_data.get('close_date', None)
