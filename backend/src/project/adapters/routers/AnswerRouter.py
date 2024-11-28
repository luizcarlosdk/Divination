from fastapi import APIRouter
from project.ports.routers.Router import Router
from project.core.ChatService import ChatService
from project.adapters.routers.dto.answer_dto import (
    AnswerRequest,
    AnswerResponse,
    ChangeTemplate,
)
from project.adapters.database.ChatRepository import ChatRepository


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

        return router
