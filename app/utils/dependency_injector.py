from app.providers.ai_client import ai_provider
from app.repository.ai_repository import AiRepository


class DependencyInjector:
    def __init__(self):
        self.services = {}

    def configure(self):
        ai_client = ai_provider.get_ai_client()
        ai_repository = AiRepository(ai_client, ai_assistant=ai_provider.get_ai_assistant())

        self.services["ai_repository"] = ai_repository

    def get(self, service_name):
        return self.services[service_name]


injector = DependencyInjector()
