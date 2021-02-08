from typing import Dict


class BotCommand:
    def __init__(self, command_data: Dict):
        self.command: str = command_data['command']
        self.description: str = command_data['description']
