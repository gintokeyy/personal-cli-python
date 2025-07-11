from todo import todomenu

from goals import goalsmenu 
    
from cplogs import cpmenu

def main():
    while True :
        print("-------- PERSONAL DASHBOARD --------")
        print("         #1. TO-DO LIST             ")
        print("         #2. DAILY GOALS            ")
        print("         #3. CP TRACKER             ")
        print("         #4. EXIT                   ")
        
        choice = int(input("Enter your choice : "))
        
        if (choice == 1):
            todomenu()
        elif (choice == 2):
            goalsmenu()
        elif (choice == 3):
            cpmenu()
        elif(choice == 4):
            print("Goodbye ")
            break
        else :
            print("Invalid Choice")

if __name__ == "__main__":
    main()  