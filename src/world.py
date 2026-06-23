"""World loader."""
from content.world_data import ROOMS, CHALLENGES


class World:
    def __init__(self) -> None:
        self.rooms = ROOMS
        self.challenges = CHALLENGES

    def get_room(self, room_id: str) -> dict:
        return self.rooms.get(room_id, {})

    def get_challenge(self, challenge_id: str) -> dict:
        return self.challenges.get(challenge_id, {})
