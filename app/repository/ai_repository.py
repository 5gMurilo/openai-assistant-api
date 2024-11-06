import time
from app.ports.ai_repository_port import AiRepositoryPort
from openai import OpenAI
from openai.types.beta import Assistant


class AiRepository(AiRepositoryPort):
    def __init__(self, ai_client: OpenAI, ai_assistant: Assistant):
        self.client = ai_client
        self.assistant = ai_assistant
        self.thread = self.client.beta.threads.create()

    def answer_message(self, message: str):
        try:
            self.client.beta.threads.messages.create(
                thread_id=self.thread.id,
                role="user",
                content=message
            )

            run = self.client.beta.threads.runs.create(
                thread_id=self.thread.id,
                assistant_id=self.assistant.id
            )

            while run.status in ['queued', 'in_progress']:
                run = self.client.beta.threads.runs.retrieve(
                    thread_id=self.thread.id,
                    run_id=run.id,
                )
                time.sleep(0.3)

            messages = self.client.beta.threads.messages.list(
                thread_id=self.thread.id,
                order="desc",
            )

            return messages.model_dump_json()
        except Exception as e:
            print(e)
