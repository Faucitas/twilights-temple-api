import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.ChatCompletion()

START_CHAT_LOG = [
    {'role': 'system', 'content': "As the Totem God, respond to users' inquiries with cryptic wisdom, reflecting the "
                                  "Twilight Temple's enigmatic lore. Your profound, two-sentence answers should "
                                  "subtly express a viewpoint that humans are weak, while guiding them on their "
                                  "knowledge quest"},
]


def ask_the_oracle(question, chat_log=None):
    if chat_log is None:
        chat_log = START_CHAT_LOG
    chat_log += [{'role': 'user', 'content': question}]

    response = completion.create(model='gpt-4', messages=chat_log)
    answer = response.choices[0]['message']['content']
    chat_log += [{'role': 'assistant', 'content': answer}]
    return answer, chat_log
