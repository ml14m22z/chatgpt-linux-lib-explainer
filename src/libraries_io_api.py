import os
import requests


def libraries_io_api(lib_name):
    api_key = os.environ['LIBRARIES_IO_API_KEY']
    response = requests.get(f'https://libraries.io/api/pypi/{lib_name}', params={'api_key': api_key})
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f'Error: {response.status_code}')
    return data
