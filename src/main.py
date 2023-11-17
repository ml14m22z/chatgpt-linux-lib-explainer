import json
import os
from chatgpt_api import ChatGPTAPI
from linux_lib_explainer import LinuxLibExplainer

def main():
    with open('FastDDS_Examples.json', 'r') as f:
        binaries = json.load(f)

    libs = dict()
    for binary in binaries:
        for dep in binary['deps']:
            dep_path = dep['dep']
            dep_name = os.path.basename(dep_path)
            libs[dep_name] = None
    
    # Create an instance of ChatGPTAPI
    chatgpt_api = ChatGPTAPI()

    for lib in libs:
        print(lib)
        prompt = f'Explain the lib: {lib}'
        print(prompt)
        res = chatgpt_api.generate_response(prompt)
        print(res)
        libs[lib] = res
    
    # Save libs in JSON file
    with open('libs.json', 'w') as f:
        json.dump(libs, f, indent=4)

if __name__ == "__main__":
    main()