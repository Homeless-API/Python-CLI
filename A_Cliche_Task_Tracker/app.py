import os
import json
import uuid
from datetime import datetime
from pathlib import Path

current_path = Path(__file__)
parent_path = current_path.parent
print("parent_path: "+ str(parent_path))




data_path = os.path.join(parent_path, 'tasks_db.json')
if not os.path.exists(data_path):
    with open(data_path, 'w') as f:
        json.dump([], f)  # Initialize with an empty list

def write_data(task):
    data_path = os.path.join(parent_path, 'tasks_db.json')

    with open(data_path, 'w') as f:
        json.dump(task, f, indent=4)

def read_tasks():
    """Reads the task list from JSON, ensuring it's not empty."""
    data_path = os.path.join(parent_path, 'tasks_db.json')
    if os.stat(data_path).st_size == 0:  # Check if file is empty
        return []
    
    with open(data_path, 'r') as f:
        return json.load(f)


def Add_tasks():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    tasks = read_tasks()

    new_task = {
        'id': str(uuid.uuid4()),
        'description': input("\nGive a short description of the task: "),
        'status':  "todo"  ,
        'created_at': formatted_time,
        'updated_at': 'none'
    }

    tasks.append(new_task)

    write_data(tasks)
    print("task has been added successfully!!")

def Update_tasks():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    tasks = read_tasks()
    
    for task in tasks:
        print('\n----------------------------------------')
        Task_ID = input('enter the ID of the task you want to modify: ')
        print('----------------------------------------\n')
        for task in tasks:
            if task['id'] == Task_ID:
                print("1: in progress")
                print("2: compelted")
                status_change = input("Pick the number of the respective you want to change the status too: ")
                if status_change == "1":
                    new_status = 'in progress'
                    task['status'] = new_status

                    task['updated_at'] = formatted_time
                    write_data(tasks)
                    print("task has been updated successfully!!")
                    break
                else:
                    new_status = 'completed'
                    task['status'] = new_status

                    task['updated_at'] = formatted_time
                    write_data(tasks)
                    print("task has been updated successfully!!")
                    break

        
        break


def veiw_tasks():
    tasks = read_tasks()
    
    if tasks == []:
        print("\n\n|___________________|")
        print("| no tasks saved!!  |")
        print("|___________________|\n\n")
    else:
        for task in tasks:
            print('\n\n_________________________________________________________________________________________________________')
            print('| ' + task['id'] + ' | ' +  task['description'] + '       | ' + task['status'] + '       | ' + task['created_at'] + '       | ' + task['updated_at'] + '|') 
            print('---------------------------------------------------------------------------------------------------\n\n')

def Delete_tasks():
    tasks = read_tasks()

    
    print("1. Delete a task")
    print("2. Delete all tasks")
    print('----------------------------------------\n')
    Delete_choice = input('pick what you want to delete with its corresponding number: ')

    if Delete_choice == "1":
        Task_ID = input('enter the ID of the task you want to delete: ')
        for task in tasks:
            if task['id'] == Task_ID:
                tasks.remove(task)
                write_data(tasks)
                print("task has been deleted successfully!!")
    else:
        for task in tasks:
            write_data([])
            print("all tasks have been deleted successfully!!")
            
            

    
    

def Task_Tracker():
    while True:
        print("\nTask Tracker Menu:")
        print("\n|-----------------|")
        print('|  1. Veiw task   |')
        print("|-----------------|")
        print('|  2. Add task    |')
        print("|-----------------|")
        print('|  3. Update task |')
        print("|-----------------|")
        print('|  4. Delete task |')
        print("|-----------------|")
        print('|  5. Exit        |')
        print("|-----------------|")

        choice = input('\n -Choose the task you want to excute \n -Using a corresponding number: ')

        if choice == '1':
            veiw_tasks()

        elif choice == '2':
            Add_tasks()
            continue

        elif choice == '3':
            Update_tasks()
            continue

        elif choice == '4':
            Delete_tasks()
            continue

        elif choice == '5':
            break

        else:
            print('Invalid choice')
            continue


Task_Tracker()
