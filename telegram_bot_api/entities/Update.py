from .Message import Message
from .Poll import Poll
from .PollAnswer import PollAnswer
from .InlineQuery import InlineQuery
from .CallbackQuery import CallbackQuery
from .ShippingQuery import ShippingQuery
from .PreCheckoutQuery import PreCheckoutQuery
from typing import Optional


class Update:
    def __init__(self, data):
        self.update_id: int = data['update_id']
        self.message: Optional[Message] = data.get('message', None)
        self.edited_message: Optional[Message] = data.get(
            'edited_message', None)
        self.channel_post: Optional[Message] = data.get('channel_post', None)
        self.edited_channel_post: Optional[Message] = data.get(
            'edited_channel_post', None)
        self.inline_query: Optional[InlineQuery] = data.get(
            'inline_query', None)
        self.callback_query: Optional[CallbackQuery] = data.get(
            'callback_query', None)
        self.shipping_query: Optional[ShippingQuery] = data.get(
            'shipping_query', None)
        self.pre_checkout_query: Optional[PreCheckoutQuery] = data.get(
            'pre_checkout_query', None)
        self.poll: Optional[Poll] = data.get('poll', None)
        self.poll_answer: Optional[PollAnswer] = data.get('poll_answer', None)
