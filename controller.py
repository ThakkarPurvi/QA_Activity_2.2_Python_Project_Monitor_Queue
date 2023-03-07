
import sys
from app import home, top20, jobid


def execute_app():

    print("Python Project Index, what would you like to do? "
          "\n1. View home page"
          "\n2. View the latest 20 trigger in Monitor database"
          "\n3. View trigger using job id")

    running = True

    while running:
        opt = int(input("Please choose a number (1-3): "))
        if opt == 1:
            print(home())
        elif opt == 2:
            print(top20())
        elif opt == 3:
            print(jobid())
        else:
            print("Incorrect choice.. try again..")
        end_choice = input("\nDo you want to query more data Y / N: ")
        if end_choice.upper() == "N":
            sys.exit(f"THANK YOU")


execute_app()