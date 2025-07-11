def load(filename="tasks.txt"):
    try:
        file = open(filename, "r")
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines
    except FileNotFoundError:
        return []

def save(tasks, filename="tasks.txt"):
    file = open(filename, "w")
    for task in tasks:
        file.write(task + '\n')
    file.close()

def show(tasks):
    if not tasks:
        print("There are no tasks")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add(tasks):
    task = input("Enter the task you want to be added: ")
    tasks.append(task)

def remove(tasks):
    show(tasks)
    try:
        index = int(input("Enter the number of the task you wish to be removed: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed the task: {removed}")
        else:
            print("Invalid Choice")
    except ValueError:
        print("Please enter a valid number.")

def todomenu():
    tasks = load()
    while True:
        print("\n----- TO-DO LIST -----")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit to Dashboard")
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
        elif choice == 4:
            save(tasks)
            print("Returning to Dashboard\n")
            break
        else:
            print("Invalid Choice\n")
