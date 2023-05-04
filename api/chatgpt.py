import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = "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"

## https://platform.openai.com/docs/models/model-endpoint-compatibility
## text-davinci-003, text-davinci-002, text-curie-001, text-babbage-001, text-ada-001

class ChatGPT:
    def __init__(self):
        self.model = os.getenv("OPENAI_MODEL", default = "text-davinci-002")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 240))

    def get_response(self, text):

        response = openai.Completion.create(
            model=self.model,
            prompt=text,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens
        )
        print('[response]', response)

        return response['choices'][0]['text'].strip()

    def get_models(self):
        return openai.Model.list()
