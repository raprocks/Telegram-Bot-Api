from typing import Dict, Optional

class Dice:
    def __init__(self, dice_data: Dict):
        self.emoji: str = dice_data['emoji']
        self.value: int = dice_data['value']
