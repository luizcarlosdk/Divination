from fastapi import APIRouter
from project.ports.Router import Router
from project.core.ChatService import ChatService
from project.adapters.answer_dto import (
    AnswerRequest,
    AnswerResponse,
    ChangeTemplate,
)


class AnswerRouter(Router):
    def __init__(self, chat_service: ChatService):
        self.chat_service = chat_service

    def create(self):
        router = APIRouter()

        @router.post("/v1/context")
        def change_template(template: ChangeTemplate):
            self.chat_service.answer_template.changeTemplate(
                template.new_template
            )
            return template.new_template

        @router.post("/v1/answer")
        def get_answer(request: AnswerRequest) -> AnswerResponse:
            answer = self.chat_service.get_answer(query=request.user_question)

            return AnswerResponse.create_answer(answer)

        return router
