from chatgpt_api import ChatGPTAPI
from linux_lib_explainer import LinuxLibExplainer

def main():
    # Get the name of the Linux shared library to explain
    lib_name = input("Enter the name of the Linux shared library to explain: ")
    
    # Create an instance of LinuxLibExplainer
    linux_lib_explainer = LinuxLibExplainer(lib_name)

    # Get the explanation of the Linux shared library
    function_list = linux_lib_explainer.get_function_list()
    explanation = linux_lib_explainer.explain_function(function_list[0])

    # Create an instance of ChatGPTAPI
    chatgpt_api = ChatGPTAPI()

    # Use ChatGPTAPI to generate a more user-friendly explanation
    user_friendly_explanation = chatgpt_api.generate_explanation(explanation)

    # Print the user-friendly explanation
    print(user_friendly_explanation)

if __name__ == "__main__":
    main()