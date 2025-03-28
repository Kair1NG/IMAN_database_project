# Admin ACCESS Panel

import os, time
import library_scanning as LS
import connect_database as CD

def main():
    print("PLACEHOLDER Admin")
    
    os.system('cls' if os.name == 'nt' else 'clear') # Terminal Clear
    print("Admin Controls")
    print("[1] Display LOGs\n[2] Frequency Analysis\n[3] Place Student Violation\n[0] Return to Main Menu")
    
    # Error Handling
    try:
        choice_ADMIN = int(input(">>: "))
    except ValueError:
        print("Error | Non Numerical Input")
        time.sleep(2)
        main()
    
    # Admin Controls
    match choice_ADMIN:
        case 0:
            LS.Main_menu()
            return
        case 1:
            CD.Display_TABLE_Students()
            input("Press any key to continue.")
            main()
            return
        case 2:
            CD.Frequency_Analysis()
            input("Press any key to continue.")
            main()
            return
        case 3:
            CD.Violations()
            input("Press any key to continue.")
            main()
            return
            
    
if __name__ == "__main__":
    main()