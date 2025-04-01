from pathlib import Path
import requests 
import json
import os

current_path = Path(__file__)
parent_path = current_path.parent

n = 10

print("\n" + "="*30)
print("✨ GITHUB USER ACTIVITY ✨".center(30))
print("="*30 + "\n")

# Upper part of the diamond
for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i)

# Lower part of the diamond
for i in range(n - 2, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)

print("\n" + "="*30)
print("🔹 GitHub Username 🔹".center(30))
print("="*30)

username = input("\n📌 Provide your GitHub username: ")
print(f"\n✅ Username '{username}' received successfully! 🚀\n")


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
    
while True:
    print("\n" + "="*40)
    print("🔍 GitHub Data Fetcher 🔍".center(40))
    print("="*40)

    print("\n📌 What would you like to fetch?")
    print("-" * 40)
    print(" 1️⃣  Commits")
    print(" 2️⃣  Pull Requests")
    print(" 3️⃣  Issues")
    print(" 4️⃣  All")
    print(" 5️⃣  🚪 Exit")
    print("-" * 40)

    task_picked = input("\n👉 Pick a number (1-5): ")
    print("\n✅ You selected option:", task_picked)


    if task_picked == "1":
        for event in data:
            if event['type'] == 'PushEvent':
                for commit in event['payload']['commits']:
                    author = commit['author']
                    message = commit['message']
                    URL = commit['url']
                    public = event['public']

                    print("\n" + "="*50)
                    print(f"📌  Commit by:   {author['name']}")
                    print(f"📧  Email:      {author['email']}")
                    print("-"*50)
                    print(f"📢  Public:    {public}")
                    print(f"📝  Commit Message: {message}")
                    print(f"🔗  URL:        {URL}")
                    print("="*50 + "\n")
        
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
        break
