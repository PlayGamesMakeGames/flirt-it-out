import uuid
from .common import PacketAgent, Message
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .room import Room
else:
    Room = None

class User(PacketAgent):
    def __init__(self, name: str) -> None:
        super(User, self).__init__(uuid.uuid1())

        self.name = name
        self.handlers = {
            "msg": self.handle_msg
        }

    async def handle_msg(self, room: Room, packet):
        msg = Message(
            sender=self,
            content=packet.payload["content"]
        )
        print(f"message from {self.name}: {msg.content}")
        await room.pending_messages.put(msg)