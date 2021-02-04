class User:
    def __init__(self, user_data):
        self.id: int = user_data['id']
        self.is_bot: bool = user_data['is_bot']
        self.first_name: str = user_data['first_name']
        self.last_name: str = user_data.get('last_name', None)
        self.username: str = user_data.get('username', None)
        self.language_code: str = user_data.get('language_code', None)
        self.can_join_groups: bool = user_data.get('can_join_groups', None)
        self.can_read_all_group_messages: bool = user_data.get(
            'can_read_all_group_messages', None)
        self.supports_inline_queries: bool = user_data.get(
            'supports_inline_queries', None)
