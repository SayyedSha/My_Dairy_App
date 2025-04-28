import os
from datetime import datetime

DIARY_FILE = "diary.txt"

def write_entry():
    entry = input("\nWhat's on your mind today?\n")
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    with open(DIARY_FILE, "a") as file:
        file.write(f"{timestamp}\n{entry}\n{'-'*40}\n")
    print("\n✅ Entry saved successfully!\n")

def view_entries():
    if not os.path.exists(DIARY_FILE):
        print("\nNo entries found yet. Start writing your first one!\n")
        return
    
    print("\n📖 Your Diary Entries:\n")
    with open(DIARY_FILE, "r") as file:
        print(file.read())

def main():
    while True:
        print("\nMini Diary App")
        print("1. Write a new entry")
        print("2. View past entries")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("\n👋 Goodbye! Keep writing!")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
