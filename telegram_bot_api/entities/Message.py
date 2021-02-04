from Chat import Chat, Dict
from User import User
from typing import Optional, List


class Message:
    def __init__(self, message_data: Dict):
        self.message_id: int = message_data['message_id']
        self.recieved_from: str = message_data['from']
        self.date: int = message_data['date']
        self.chat: Chat = message_data['chat']
        self.forwarded: Optional[bool] = message_data.get('forwarded', None)
        self.forward_from_chat: Optional[Chat] = message_data.get(
            'forward_from_chat', None)
        self.forward_from_message_id: Optional[int] = message_data.get(
            'forward_from_message_id', None)
        self.forward_signature: Optional[str] = message_data.get(
            'forward_signature', None)
        self.forward_sender_name: Optional[str] = message_data.get(
            'forward_sender_name', None)
        self.forward_date: Optional[int] = message_data.get(
            'forward_date', None)
        self.reply_to_message: Optional[str] = message_data.get(
            'reply_to_message', None)
        self.via_bot: Optional[User] = message_data.get('via_bot', None)
        self.edit_date: Optional[int] = message_data.get('edit_date', None)
        self.media_group_id: Optional[str] = message_data.get(
            'media_group_id', None)
        self.author_signature: Optional[str] = message_data.get(
            'author_signature', None)
        self.text: Optional[str] = message_data.get('text', None)
        self.entities: Optional[List[MessageEntity]
                                ] = message_data.get('entities', None)
        self.animation: Optional[Animation] = message_data.get(
            'animation', None)
        self.audio: Optional[Audio] = message_data.get('audio', None)
        self.document: Optional[Document] = message_data.get('document', None)
        self.photo: Optional[List[PhotoSize]] = message_data.get('photo', None)
        self.sticker: Optional[Sticker] = message_data.get('sticker', None)
        self.video: Optional[Video] = message_data.get('video', None)
        self.video_note: Optional[VideoNote] = message_data.get(
            'video_note', None)
        self.voice: Optional[Voice] = message_data.get('voice', None)
        self.caption: Optional[str] = message_data.get('caption', None)
        self.caption_entities: Optional[List[MessageEntity]] = message_data.get(
            'caption_entities', None)
        self.contact: Optional[Contact] = message_data.get('contact', None)
        self.dice: Optional[Dice] = message_data.get('dice', None)
        self.game: Optional[Game] = message_data.get('game', None)
        self.poll: Optional[Poll] = message_data.get('poll', None)
        self.venue: Optional[Venue] = message_data.get('venue', None)
        self.location: Optional[Location] = message_data.get('location', None)
        self.new_chat_members: Optional[List[User]] = message_data.get(
            'new_chat_members', None)
        self.left_chat_member: Optional[User] = message_data.get(
            'left_chat_member', None)
        self.new_chat_title: Optional[str] = message_data.get(
            'new_chat_title', None)
        self.new_chat_photo: Optional[List[PhotoSize]
                                      ] = message_data.get('new_chat_photo', None)
        self.delete_chat_photo: Optional[bool] = message_data.get(
            'delete_chat_photo', None)
        self.group_chat_created: Optional[bool] = message_data.get(
            'group_chat_created', None)
        self.supergroup_chat_created: Optional[bool] = message_data.get(
            'supergroup_chat_created', None)
        self.channel_chat_created: Optional[bool] = message_data.get(
            'channel_chat_created', None)
        self.migrate_to_chat_id: Optional[int] = message_data.get(
            'migrate_to_chat_id', None)
        self.migrate_from_chat_id: Optional[int] = message_data.get(
            'migrate_from_chat_id', None)
        self.pinned_message: Optional[Message] = message_data.get(
            'pinned_message', None)
        self.invoice: Optional[Invoice] = message_data.get('invoice', None)
        self.successful_payment: Optional[SuccessfulPayment] = message_data.get(
            'successful_payment', None)
        self.connected_website: Optional[str] = message_data.get(
            'connected_website', None)
        self.passport_data: Optional[PassportData] = message_data.get(
            'passport_data', None)
        self.reply_markup: Optional[InlineKeyboardMarkup] = message_data.get(
            'InlineKeyboardMarkup')
