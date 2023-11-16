import os
import openai

class ChatGPTAPI:
    def __init__(self, api_key=os.environ['OPENAI_API_KEY']):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_response(self, prompt, max_tokens=100):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=max_tokens
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":
    # import os
    # os.environ['http_proxy'] = 'http://proxy-server:port'
    # os.environ['https_proxy'] = 'https://proxy-server:port'
    chatgpt_api = ChatGPTAPI()
    prompt = input("Enter your prompt: ") or "This is a test prompt."
    response = chatgpt_api.generate_response(prompt)
    print(response)
