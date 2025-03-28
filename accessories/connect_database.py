# Database Controls

import sqlite3, time
import library_scanning as LS

# Displaying of Tables

# Display Students_LOGGED
def Display_TABLE_Students():
    # Connect to DB
    connect = sqlite3.connect("Library.db")
    cursor = connect.cursor()
    
    
    cursor.execute("SELECT * FROM Students_LOGGED")
    print('-----------------------------------------------------------------------------------------------------------------')
    print('|   LOG ID   | Student ID |          Student Name          |        Department         |   Date Logged   | LOV |')
    print('-----------------------------------------------------------------------------------------------------------------')
    
    rows = cursor.fetchall()
    for row in rows:
        print(f"| {row[0]:^9}  | {row[1]:^10} | {row[2]:^30} | {row[3]:^25} | {row[4]:^15} | {row[5]:^3} |")
    print('-----------------------------------------------------------------------------------------------------------------')
    pass

# Display Frequency of Visit
def Frequency_Analysis():
    # Connect to DB
    connect = sqlite3.connect("Library.db")
    cursor = connect.cursor()
    
    # Couting the LOGs of {student_id}
    cursor.execute("SELECT student_id, count(*) FROM Students_LOGGED GROUP BY student_id;")
    print('-----------------------------------')
    print('| Student ID | Frequency of Visit |')
    print('-----------------------------------')
    
    rows = cursor.fetchall()
    for row in rows:
        print(f"| {row[0]:^10} |  {row[1]:^15}   |")
    print('-----------------------------------')
    pass

# Update Student Record
def Violations():
    # Connect to DB
    connect = sqlite3.connect("Library.db")
    cursor = connect.cursor()
    print('When did the violation happen?') # Tracing when the violation happened.
    
    # Error Handling
    try:
        Get_LOG = int(input('Enter a Log ID >>: '))
        LS.Is_Running(Get_LOG)
    except ValueError:
        print('Error | Non Numerical Input')
        time.sleep(2)
        Violations()
    
    print('How severe was the violation?') # Applying the severity
    
    # Error Handling
    try:
        Get_LOV = int(input('Enter a Log ID >>: '))
        LS.Is_Running(Get_LOG)
    except ValueError:
        print('Error | Non Numerical Input')
        time.sleep(2)
        Violations()
    
    cursor.execute('UPDATE Students_LOGGED SET did_violate = ? WHERE log_id = ?', (Get_LOV, Get_LOG) ) # setting of these new values.
    connect.commit()
    pass