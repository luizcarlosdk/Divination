from fastapi import APIRouter
from project.ports.Router import Router
from project.main import create_answer

from project.core.ChatService import ChatService

class AnswerRouter(Router):
    def __init__(self,chat_service):
        self.chat_service = chat_service
    def create(self):

        router = APIRouter()

        @router.post("/v1/answer")
        def get_answer(user_question: str):
            answer = self.chat_service.get_answer(user_question)

            return answer