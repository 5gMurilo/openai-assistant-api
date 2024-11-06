from abc import ABC, abstractmethod


class AiRepositoryPort(ABC):
    @abstractmethod
    def answer_message(self, message: str):
        pass
