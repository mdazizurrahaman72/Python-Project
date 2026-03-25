import datetime
import os

def create_note():
    print("\n📝 Cate New Note")
    print("-"*40)

    titel = input("Note titel: ")
    print("Write your note (press enter twice to save): ")

    contant = []
    empty_line = 0

    while empty_line < 2:
        line = input()
        if line == "":
            empty_line+=1
        else:
            empty_line = 0
            contant.append(line)

    file_name = titel.replace(" ","_")+".txt"

    with open(file_name,"w") as file:
        file.write(f"Titel : {file_name}\n")
        file.write(f"Date : {datetime.date.today()}\n") 
        file.write("-"*40+"\n")
        for line in contant:
            file.write(line+"\n")
    
    print(f"✅ Note saved as {file_name}")

def write_note():
    print("\n--------Write Note-------")
    file_name = input("Enter note filename (with.txt): ")

    if os.path.exists(file_name):
        print("Write your note (press enter twice to save): ")

        contant = []
        empty_line = 0

        while empty_line < 2:
            line = input()
            if line == "":
                empty_line+=1
            else:
                empty_line = 0
                contant.append(line)

        with open(file_name,"w") as file:
            for line in contant:
                file.write(line+"\n")

        print("✅ Write save note")
    else:
        print("❌ Note not found!")

def read_note():
    print("\n--------Read Note-------")
    file_name = input("Enter note filename (with.txt): ")

    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            contant = file.read()
            print("-"*40)
            print(contant)
            print("-"*40)
    else:
        print("❌ Note not found!")
            
def list_notes():
    print("\\n📚 Available Notes:")
    print("-" * 30)

    files = os.listdir(".")
    note_files = []

    for file in files:
        if file.endswith(".txt"):
            note_files.append(file)

    if len(note_files) == 0:
        print("No Notrs found!")
    else:
        for i,note in enumerate(note_files):
            print(f"{i}. {note}")

def quick_note():
    print("\n⚡ Quick Note")
    note = input("Enter quick note: ")

    today = datetime.date.today()

    with open("daily_note.txt","a") as file:
        file.write(f"{today} | {datetime.datetime.now().strftime('%H:%M')} | {note}\n")
    
    print("✅ Quick note saved!")

def view_quick_notes():
    print("\n📋 Quick Notes")
    print("-" * 50)

    if os.path.exists("daily_note.txt"):

        with open("daily_note.txt", "r") as file:
            notes = file.readlines()

        if len(notes) == 0:
            print("No quick notes yet!")
        else:
            for note in notes:
                print(note.strip())
    else:
        print("No quick notes file found!")

def note_app():
    print("\n📝 SIMPLE NOTE APP")
    print("=" * 40)

    operations = {
        '1':("Create Note",create_note),
        '2':("Write Note",write_note),
        '3':("Read Note",read_note),
        '4':("List All Notes",list_notes),
        '5':("Quick Note",quick_note),
        '6':("View Quick Notes",view_quick_notes)
    }

    while True:
        print("\n📋 MENU")

        for key,value in operations.items():
            print(f"{key}. {value[0]}")
        print("0. Exit")

        choice = input("\nChoose option (1-6): ")

        if choice == '0':
            print("\n👋 Goodbye!")
            break

        if choice in operations:
            name,funs = operations[choice]
            funs()
        else:
            print("❌ Please choose (0-6)")

if __name__ == "__main__":
    note_app()