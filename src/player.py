"""Player state."""
from __future__ import annotations


class Player:
    def __init__(self, start_room: str = "altar_diego") -> None:
        self.position = start_room
        self.hp = 50
        self.max_hp = 50
        self.esp = 10
        self.nah = 10
        self.inventory: list[str] = []
        self.equipped_weapon: str | None = None
        self.picked_up: set[str] = set()
        self.defeated: set[str] = set()
        self.npc_spoken: set[str] = set()
        self.flags: set[str] = set()
        self.game_over = False

    def has_item(self, item_id: str) -> bool:
        return item_id in self.inventory

    def add_item(self, item_id: str) -> None:
        self.inventory.append(item_id)
        self.picked_up.add(item_id)

    def remove_item(self, item_id: str) -> None:
        if item_id in self.inventory:
            self.inventory.remove(item_id)

    def take_damage(self, dmg: int) -> None:
        self.hp = max(0, self.hp - dmg)
        if self.hp == 0:
            self.game_over = True

    def heal(self, amount: int) -> int:
        old = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        return self.hp - old
