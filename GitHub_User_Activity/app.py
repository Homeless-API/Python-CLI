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

def read_data():
    data_path = os.path.join(parent_path, 'data.json')
    with open(data_path, 'r') as f:
        data = json.load(f)
        return data
    
data = read_data()
    
print("\n")
print("What would you like to fetch: ")
print("*"*30)
print("1. Commits")
print("2. Pull requests")
print("3. Issues")
print("4. All")
print("5. Exit")
print("*"*30)
print("\n")
task_picked = input("pick a number with the corresponding task: ")

if task_picked == "1":
    for type in data:
        if type['type'] == 'PushEvent':
            print(type['payload']['commits'])
elif task_picked == "2":
    for type in data:
        if type['type'] == 'PullRequestEvent':
            print(type['payload']['pull_request'])
elif task_picked == "3":
    for type in data:
        if type['type'] == 'IssuesEvent':
            print(type['payload']['issue'])
elif task_picked == "4":
    for type in data:
        print(type['type'])
elif task_picked == "5":
    quit
