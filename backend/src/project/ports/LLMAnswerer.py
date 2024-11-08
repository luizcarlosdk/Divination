from abc import ABC, abstractmethod


class LLMAnswerer(ABC):
    @abstractmethod
    def get_answer(
        self,
        chat_id,
        query,
        context,
        chat,
        template,
        history_template,
        Settings,
    ):
        pass
