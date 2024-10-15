from fastapi import APIRouter
from project.ports.Router import Router

from project.core.ChatService import ChatService

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class AnswerRouter(Router):
    def __init__(self, chat_service: ChatService):
        self.chat_service = chat_service

    def create(self):
        router = APIRouter()

        @router.post("/v1/answer")
        def get_answer(request: AnswerRequest) -> AnswerResponse:
            answer = self.chat_service.get_answer(query=request.user_question)

            return AnswerResponse.create_answer(answer)

        return router


class RouteExchange(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class AnswerRequest(RouteExchange):
    user_question: str


class AnswerResponse(RouteExchange):
    project_answer: str

    @classmethod
    def create_answer(self, answer: str):
        return AnswerResponse(project_answer=answer)
