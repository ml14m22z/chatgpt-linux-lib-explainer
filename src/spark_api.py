import configparser
import SparkApi

text =[]

# length = 0

def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text

class SparkAPI:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('.config', encoding='utf-8')

        #以下密钥信息从控制台获取
        self.appid = config.get('iflytek', 'appid')     #填写控制台中获取的 APPID 信息
        self.api_secret = config.get('iflytek', 'api_secret')   #填写控制台中获取的 APISecret 信息
        self.api_key = config.get('iflytek', 'api_key')    #填写控制台中获取的 APIKey 信息

        #用于配置大模型版本，默认“general/generalv2/generalv3”
        self.domain = config.get('iflytek', 'domain')   # v3.0版本

        #云端环境的服务地址
        self.Spark_url = config.get('iflytek', 'Spark_url')  # v3.0环境的地址

    def generate_response(self, prompt):
        try:
            text.clear
            Input = prompt
            question = checklen(getText("user",Input))
            SparkApi.answer =""
            SparkApi.main(self.appid,self.api_key,self.api_secret,self.Spark_url,self.domain,question)
            getText("assistant",SparkApi.answer)
            return text[-1]["content"]
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":
    spark_api = SparkAPI()
    prompt = input("Enter your prompt: ") or "This is a test prompt."
    response = spark_api.generate_response(prompt)
    print(response)
