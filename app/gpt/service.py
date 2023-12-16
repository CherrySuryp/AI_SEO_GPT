import openai
from app.config import Config

config = Config()


class ChatGPT:
    """
    Работа с ChatGPT
    """

    def __init__(self, model: str = config.GPT_MODEL, openai_key: str = config.OPENAI_KEY):
        self.model = model
        openai.api_key = openai_key

    def send_request(self, prompt: str) -> str:
        """
        Отправляет запрос в ChatGPT и возвращает ответ
        :return:
        """
        return (
            openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
            .choices[0]
            .message.content
        )
