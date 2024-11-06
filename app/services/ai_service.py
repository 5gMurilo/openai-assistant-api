from app.repository.ai_repository import AiRepository


class AiService:
    def __init__(self, ai_repository: AiRepository):
        self.ai_repository = ai_repository

    def answer_message(self, message: str):
        return self.ai_repository.answer_message(message)
