from openai import OpenAI
from openai.types.beta import Assistant
from config import Config


class AiProvider:
    def __init__(self):
        self.ai_client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def get_ai_client(self) -> OpenAI:
        return self.ai_client

    def get_ai_assistant(self) -> Assistant:
        return self.ai_client.beta.assistants.retrieve(Config.ASSISTANT_ID)


ai_provider = AiProvider()
