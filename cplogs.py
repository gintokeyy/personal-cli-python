import datetime

def loadcp(filename = "cp.txt"):
    try : 
        file = open(filename, "r")
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines
    except FileNotFoundError:
        return[]
    
def savecp(logs, filename = "cp.txt"):
    file = open(filename, "w")
    for log in logs:
        file.write(log+ "\n")
        
def viewcp(logs):   
    if not logs : 
        print("There are no logs yet")
    else : 
        for log in logs:
            print(f"{log}")

def addcp(logs):
    try : 
        number = int(input("How many problems did you sovle today? "))
        date = datetime.date.today().isoformat()     
        logs.append(f"{date}. {number} problems ")
    except ValueError:
        print("Invalid Input")
        
def cpmenu():
    
    logs = loadcp()
    
    while True:
        print("-------- COMPETITIVE PROGRAMMING LOGGER --------")  
        print("             #1. View Logs                  ")         
        print("             #2. Add Today's Progress       ")   
        print("             #3. Back to Dashboard          ")   
        choice = int(input("Enter your choice : "))
        
        try : 
            if choice == 1:
                viewcp(logs)
            elif choice == 2:
                addcp(logs)
            elif choice == 3 :
                print("Returning to Dashboard")
                savecp(logs)
                break
            else : 
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
            

    