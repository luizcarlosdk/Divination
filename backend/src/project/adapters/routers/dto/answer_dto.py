from project.adapters.routers.route_exchange import RouteExchange


class AnswerRequest(RouteExchange):
    user_question: str
    chat_id: str


class AnswerResponse(RouteExchange):
    project_answer: str

    @classmethod
    def create_answer(self, answer: str):
        return AnswerResponse(project_answer=answer)


class ChangeTemplate(RouteExchange):
    new_template: str
