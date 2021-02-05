from .PollOption import PollOption
from .MessageEntity import MessageEntity
from typing import Optional, List, Dict

'''

Field	Type	Description
id	String	Unique poll identifier
question	String	Poll question, 1-300 characters
options	Array of PollOption	List of poll options
total_voter_count	Integer	Total number of users that voted in the poll
is_closed	Boolean	True, if the poll is closed
is_anonymous	Boolean	True, if the poll is anonymous
type	String	Poll type, currently can be “regular” or “quiz”
allows_multiple_answers	Boolean	True, if the poll allows multiple answers
correct_option_id	Integer	Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
explanation	String	Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
explanation_entities	Array of MessageEntity	Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
open_period	Integer	Optional. Amount of time in seconds the poll will be active after creation
close_date	Integer	Optional. Point in time (Unix timestamp) when the poll will be automatically closed
'''

class Poll:
    def __init__(self, poll_data: Dict):
        self.id: str
        self.question: str
        self.options: List[PollOption]
        self.total_voter_count: int
        self.is_closed: bool
        self.is_anonymous: bool
        self.type: str
        self.allows_multiple_answers: bool
        self.correct_option_id: int
        self.explanation: str
        self.explanation_entities: List[MessageEntity]
        self.open_period: int
        self.close_date: int
