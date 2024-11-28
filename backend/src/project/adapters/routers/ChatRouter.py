from fastapi import APIRouter
from project.ports.routers.Router import Router
from project.adapters.routers.dto.chat_dto import (
    CreateChatResponse,
    ShowChatResponse,
    ListChatsResponse,
)
from project.adapters.database.ChatRepository import ChatRepository


class ChatRouter(Router):
    def __init__(self, chat_repository: ChatRepository):
        self.chat_repository = chat_repository

    def create(self):
        router = APIRouter()

        @router.post("/v1/chats")
        def create_chat() -> CreateChatResponse:
            new_chat_id = self.chat_repository.create()

            return CreateChatResponse.create(new_chat_id)

        @router.get("/v1/chats/:id")
        def show_chat(id: str) -> ShowChatResponse:
            history = self.chat_repository.get_history(id)
            return ShowChatResponse.create(history)

        @router.get("/v1/chats")
        def list_chats() -> ListChatsResponse:
            chats = self.chat_repository.get_all()

            return ListChatsResponse.create(chats)

        return router
