from fastapi import APIRouter
from project.ports.Router import Router
from project.core.ChatService import ChatService
from project.adapters.answer_dto import (
    AnswerRequest,
    AnswerResponse,
    ChangeTemplate,
)
from project.adapters.chat_dto import (
    CreateChatResponse,
    ShowChatResponse,
    ListChatsResponse,
)
from project.adapters.ChatRepository import ChatRepository


class AnswerRouter(Router):
    def __init__(
        self, chat_service: ChatService, chat_repository: ChatRepository
    ):
        self.chat_service = chat_service
        self.chat_repository = chat_repository

    def create(self):
        router = APIRouter()

        @router.post("/v1/context")
        def change_template(template: ChangeTemplate):
            self.chat_service.answer_template.change_template(
                template.new_template
            )
            return template.new_template

        @router.post("/v1/answer")
        def get_answer(request: AnswerRequest) -> AnswerResponse:
            answer = self.chat_service.get_answer(
                query=request.user_question, chat_id=request.chat_id
            )
            return AnswerResponse.create_answer(answer)

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
