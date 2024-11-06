import time

from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values(".env")

client = OpenAI(api_key=config["OPENAI_KEY"])

assistant = client.beta.assistants.retrieve(config['ASSISTANT_ID'])

def wait_on_run(run, thread):
    while run.status == 'queued' or run.status == 'in_progress':
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.3)
    return run


def answer_messages(message):
    try:
        thread = client.beta.threads.create()
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=message
        )
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id,
        )

        wait_on_run(run, thread)

        messages = client.beta.threads.messages.list(thread_id=thread.id, order="asc", after=message.id)

        return messages
    except Exception as e:
        print(e)


firstAnswer = answer_messages("Olá")
print(firstAnswer)
