from project.ports.database.Repository import Repository
import uuid
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory


class ChatRepository(Repository):
    def __init__(self):
        self.chats = {}

    def create(self):
        randomId = str(uuid.uuid4())
        self.chats[randomId] = ChatMessageHistory()

        return randomId

    def get_history(self, id) -> BaseChatMessageHistory:
        if id not in self.chats:
            self.chats[id] = ChatMessageHistory()

        return self.chats[id]

    def get_all(self):
        return self.chats
