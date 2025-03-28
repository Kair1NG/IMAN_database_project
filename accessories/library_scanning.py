# IMAN Libraray Program

import sys, os, subprocess, time

def Main_menu():
    os.system('cls' if os.name == 'nt' else 'clear') # Terminal Clear
    print("Library ACCESS")
    print("[1] Student\n[2] Administrator\n[0] Exit Program")
    
    # Error Handling
    try:
        choice_TYPE = int(input(">>: "))
    except ValueError:
        print("Error | Non Numerical Input")
        time.sleep(2)
        Main_menu()
    
    # ACCESS-Type Choices
    match choice_TYPE:
        case 0:
            sys.exit()
        case 1:
            subprocess.run(["python", "student_access.py"])
            return
        case 2:
            subprocess.run(["python", "admin_access.py"])
            return
        case _:
            print("Error | Invalid Choice")
            time.sleep(2)
            Main_menu()

def Is_Running(input):
        exit_code = '-exit'
        if input == exit_code:
            Main_menu()
            
if __name__ == "__main__":
    Main_menu()



# Prototype Code vvv

'''
student_login = {20943178:"2032-12-3", 204857463:"2025-11-44", 365737998:"2025-12-01"}
def scan_add(ID,date):
    global student_login
    student_login[ID] = date
    # student_login.update({ID:date})
    pass


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("LIBRARY MENU")
    print("[1] STUDENT\n[2] MANAGEMENT\n[3] EXIT")
    choice = int(input("CHOICE: "))

    match choice:
        case 1:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("STUDENT OPTION 1")
                print("SUBMENU\n[1] LOGIN \n[2] VIEW STUDENT ENTRY\n[3] PREVIOUS MENU")
                choice = int(input("CHOICE: "))
                match choice:
                    case 1:
                        studentID = int(input("STUDENT ID:"))
                        date = date.today()
                        scan_add(studentID,date)
                        #student_login.update({studentID:date})
                        input("Press any key to continue")
                        continue
                    case 2:
                        print("DISPLAY PREVIOUS ENTRY FROM DATABASE\n")
                        for keys,values in student_login.items():
                            print(f"STUDENT ID: {keys} logged in at {values}")
                        input("Press any key to continue")
                    case _:
                        print("RETURNING TO MAIN MENU...")
                        input("Press any key to continue")
                        break

        case _:
            print("EXITING")
            sys.exit()
'''