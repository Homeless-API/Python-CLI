from pathlib import Path
import requests 
import json
import os

current_path = Path(__file__)
parent_path = current_path.parent

print("_"* 50)
username = input("Provide your github username: ")

GIT_API = f'https://api.github.com/users/{username}/events'

response = requests.get(GIT_API)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


def write_data(response):
    data_path = os.path.join(parent_path, 'data.json')

    print("data path: ", data_path)

    with open(data_path, 'w') as f:
        json.dump(response.json(), f, indent=4)

write_data(response)

'''def read_data():
    data_path = os.path.join(parent_path, 'data')
    with open('data.json', 'r') as f:
        data = json.load(f)
        return data'''
    

print("What would you like to fetch: ")
print("1. Commits")
print("2. Pull requests")
print("3. Issues")
print("4. All")
task_picked = input("pick a number with the corresponding task: ")

