from highrise import BaseBot, SessionMetadata, User, Position
from highrise import __main__ as hr

class GuardBot(BaseBot):
    async def on_start(self, session: SessionMetadata) -> None:
        print("✅ Bot conectado en la sala")

    async def on_user_join(self, user: User, position: Position) -> None:
        await self.highrise.send_whisper(user.id, "¡Bienvenid@ a la sala!")

    async def on_chat(self, user: User, message: str) -> None:
        if message.strip().lower() == "!ping":
            await self.highrise.chat("pong")

if __name__ == "__main__":
    import os
    ROOM_ID = os.getenv("ROOM_ID")
    API_TOKEN = os.getenv("API_TOKEN")
    hr.main(GuardBot(), ROOM_ID, API_TOKEN)
