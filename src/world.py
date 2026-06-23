"""World loader."""
from content.world_data import ROOMS


class World:
    def __init__(self) -> None:
        self.rooms = ROOMS

    def get_room(self, room_id: str) -> dict:
        return self.rooms.get(room_id, {})
