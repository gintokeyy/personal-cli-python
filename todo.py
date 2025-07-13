import json
import os
from datetime import datetime


def load(filename="tasks.json"):
    try:
        file = open(filename, "r")
        tasks = json.load(file)
        file.close()
        return tasks
    except json.JSONDecodeError:
        return []

def save(tasks, filename="tasks.json"):
    file = open(filename, "w")
    json.dump(tasks,file, indent =3)
    file.close()

def show(tasks):
    if not tasks:
        print("There are no tasks")
    else : 
        priorityorder = {"High" : 1, "Medium" : 2, "Low" : 3, "Default" : 4}
        sortedTasks = sorted(tasks, key= lambda t : priorityorder.get(t['priority'], 5))

        for i, task in enumerate(sortedTasks, 1):
            print(f"{i}. {task['task']}")
            print(f"   Priority : {task['priority']}")
            print(f"   Added at : {task['created']}")

def titles(tasks):
    for i, task in enumerate(tasks, 1) : 
        print(f"{i}. {task['task']}")

def add(tasks):
    name = input("Enter the task you want to be added: ").strip()
    print("Select priority of your task : (High/Medium/Low)")
    priority = input("Enter Priority : ").capitalize()

    if priority not in ["High", "Medium", "Low"] : 
        print("invalid priority selected. priority set to 'Default'")
        priority = "Default"

    task = {
        "task" : name, 
        "priority" : priority,
        "created" : datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    print(f"Task '{name}' added with priority : {priority}")

def remove(tasks):
    global lastdeleted
    if not tasks:
        print("No tasks.")
        return 
    

    titles(tasks)

    try:
        index = int(input("Enter the number of the task you wish to be removed: ")) - 1
        if 0 <= index < len(tasks):
            
            lastdeleted = tasks.pop(index)
            print(f"Removed the task: {lastdeleted['task']}")
            save(tasks)
        else:
            print("Invalid Choice")
    except ValueError:
        print("Please enter a valid number.")

def undo(tasks):
    global lastdeleted
    if lastdeleted:
        tasks.append(lastdeleted)
        save(tasks)
        print(f"Restored : {lastdeleted['task']}")
        lastdeleted = None

def filter(tasks):
    priority = input("Enter the priority to filter by : (High/Medium/Low) : ").capitalize()
    if priority not in ["High", "Medium", "Low"] : 
        print("invalid priority selected. Returning to menu")
        return
        
    filtered = [task for task in tasks if task['priority']== priority ]

    if not filtered :
        print(f"There were no tasks with the priority {priority} ") 
    else :
        print(f" The tasks with priority '{priority}' are : ")
        for i, task in enumerate(filtered, 1) :
            print(f"{i}. {task['task']}")
            print(f"   Created @ : {task['created']}")

def todomenu():
    tasks = load()
    while True:
        print("\n----- TO-DO LIST -----")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Undo Deletion")
        print("5. Filter by Priority")
        print("6. Exit to Dashboard")
        print("\n")

        try: 
            choice = int(input("Enter the number of what you wish to do: "))
        except ValueError:
            print("Enter a valid nhoice")
            continue        

        if choice == 1:
            show(tasks)
        elif choice == 2:
            add(tasks)
        elif choice == 3:
            remove(tasks)
        elif choice ==4 :
            undo(tasks)
        elif choice == 5 :
            filter(tasks)
        elif choice == 6:
            save(tasks)
            print("Returning to Dashboard\n")
            break
        else:
            print("Invalid Choice\n")

