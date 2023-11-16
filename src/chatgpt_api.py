import openai

class ChatGPTAPI:
    def __init__(self, api_key):
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
    api_key = input("Enter your OpenAI API key: ")
    chatgpt_api = ChatGPTAPI(api_key)
    prompt = "This is a test prompt."
    response = chatgpt_api.generate_response(prompt)
    print(response)
