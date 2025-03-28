import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from accessories import library_scanning as LS

def main():
    LS.Main_menu()
    pass

if __name__ == "__main__":
    main()
