import openai

class TotemOracle:

    def __init__(self, openai_key, start_chat_log):
        self.openai_key = openai_key
        openai.api_key = self.openai_key
        self.completion = openai.ChatCompletion()
        self.start_chat_log = start_chat_log

    def ask(self, question, chat_log=None):
        chat_log = self.start_chat_log if chat_log is None else chat_log
        chat_log.append({'role': 'user', 'content': question})

        try:
            response = self.completion.create(model='gpt-4', messages=chat_log)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        answer = response.choices[0]['message']['content']
        chat_log += [{'role': 'assistant', 'content': answer}]

        return answer, chat_log
