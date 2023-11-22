import sys
import json
import os
from spark_api import SparkAPI
from linux_lib_explainer import LinuxLibExplainer

def main():
    # Check if the input file argument is provided
    if len(sys.argv) < 2:
        print("Please provide the input file as an argument.")
        return

    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        binaries = json.load(f)

    libs = dict()
    for binary in binaries:
        for dep in binary['deps']:
            dep_path = dep['dep']
            dep_name = os.path.basename(dep_path)
            libs[dep_name] = None
    
    # Create an instance of SparkAPI
    spark_api = SparkAPI()

    for lib in libs:
        print(lib)
        prompt = f'Explain the lib in English in one sentence: {lib}'
        print(prompt)
        res = spark_api.generate_response(prompt)
        print(res)
        libs[lib] = res
    
    # Save libs in JSON file
    with open('libs.json', 'w') as f:
        json.dump(libs, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()