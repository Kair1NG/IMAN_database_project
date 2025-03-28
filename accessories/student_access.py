# Student ACCESS Panel

import library_scanning as LS
import os, time, sqlite3
from datetime import date

dates = date.today()


def main():
    
    # Connect to database
    connect = sqlite3.connect("Library.db")
    cursor = connect.cursor()
    
    # Initialized Variables
    global dates

    while True: 
        # Student ACCESS Interface
        os.system('cls' if os.name == 'nt' else 'clear') # Terminal Clear
        print("Please Type your Student ID")
        Get_ID = input(": ") # <--- Input Here
        LS.Is_Running(Get_ID) # Loop breaker

        # Error Handling 
        lenght_variable = list(Get_ID)
        if len(lenght_variable) > 8 or len(lenght_variable) <= 1:
            print("Error | Improper StudentID Format")
            time.sleep(2)
            continue
        try:
            int(Get_ID)
        except ValueError:
            print("Error | Non Numerical Input")
            time.sleep(2)
            continue
        
        # Database Student LOG input
        cursor.execute("SELECT * FROM Student_INFO WHERE student_id = ?", (int(Get_ID),))
        student_Exists = cursor.fetchone()

        if student_Exists:
            cursor.execute("INSERT INTO Students_LOGGED (student_id, student_name, department_name, date_today) VALUES (?, ?, ?, ?);", (student_Exists[0], student_Exists[1], student_Exists[2], dates))
            connect.commit()
            print(f"Student {Get_ID} logged successfully!")
            time.sleep(1)
        else:
            print("Error | Student ID not found.")
            time.sleep(2)


if __name__ == "__main__":
    main()