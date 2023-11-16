import unittest
from src.chatgpt_api import ChatGPTAPI

class TestChatGPTAPI(unittest.TestCase):
    def setUp(self):
        self.chatgpt_api = ChatGPTAPI()

    def test_get_response(self):
        question = "What is Linux?"
        response = self.chatgpt_api.get_response(question)
        self.assertIsNotNone(response)

    def test_get_response_empty_question(self):
        question = ""
        with self.assertRaises(ValueError):
            self.chatgpt_api.get_response(question)

if __name__ == '__main__':
    unittest.main()