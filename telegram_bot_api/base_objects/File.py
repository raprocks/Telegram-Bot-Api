from typing import Dict


class File:
    def __init__(self, file_data: Dict):
        self.file_id: str = file_data['file_id']
        self.file_unique_id: str = file_data['file_unique_id']
