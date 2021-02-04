from typing import Dict


class ChatPhoto:
    def __init__(self, chatphoto_data: Dict):
        self.small_file_id = chatphoto_data['small_file_id']
        self.big_file_id = chatphoto_data['big_file_id']
        self.small_file_unique_id = chatphoto_data['small_file_unique_id']
        self.big_file_unique_id = chatphoto_data['big_file_unique_id']
