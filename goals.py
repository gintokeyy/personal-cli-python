def load(filename = "goals.txt"):
    try: 
        file = open(filename, "r")
        lines =  [lines.strip() for lines in file.readlines()]
        file.close()
        return lines
    except FileNotFoundError:
        return []
    
def save(goals, filename = "goals.txt"):
    file = open(filename, "w")
    for goal in goals:
        file.write(goal+"\n")
    file.close()

def show(goals):
    if not goals :
        print("There are no goals")
    else:
        for i, goal in enumerate(goals, 1):
            print(f"{i}. {goal}")
            
def add(goals):
    goal = input("Enter the goal : ")
    goals.append(goal)
    
def remove(goals):
    try :
        index = int(input("Enter the goal you want to be removed : ")) - 1
        if 0<= index < len(goals):
            removed = goals.pop(index)
            print(f"Remove task : {removed}")
        else : 
            print("Invalid Choice")
    except ValueError:
        print("Please enter a valid number")
        
def goalsmenu():
    goals = load()
    while True:
        print("\n----- GOAL MENU -----")
        print("1. View Goals")
        print("2. Add Goal")
        print("3. Remove Goal")
        print("4. Exit to Dashboard")
        print("\n")

        try: 
            choice = int(input("Enter the number of what you wish to do: "))
        except ValueError:
            print("Enter a valid nhoice")
            continue        

        if choice == 1:
            show(goals)
        elif choice == 2:
            add(goals)
        elif choice == 3:
            remove(goals)
        elif choice == 4:
            save(goals)
            print("Returning to Dashboard\n")
            break
        else:
            print("Invalid Choice\n")


    
    
    
