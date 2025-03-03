from Note import Note
from NoteHandler import NoteHandler

server = 'localhost\SQLEXPRESS'
database = 'test_db'
table = 'notes'

nh = NoteHandler(server, database, table)

from os import system
def cls(): system("cls")
def wait(): input("\nPress \"Enter\" to continue...")

while True:
    cls()
    print("Main menu: \n")

    print("1 - View all notes")
    print("2 - Add note")
    print("3 - Delete note")
    print("4 - Exit \n")

    match input("Enter choice: "):
        case "1":
            cls()
            print("Notes:")
            for i in nh.get_notes(): print(i)
            wait()


        case "2":
            cls()
            print("Adding note: \n")

            name = input("Enter note name: ")
            text = input("     Enter text: ")

            cls()
            print(nh.add_note(Note(name, text)))
            wait()


        case "3":
            cls()
            print("Deleting note: \n")

            name = input("Enter note name: ")

            cls()
            print(nh.del_note(name))
            wait()


        case "4": break
        case   _: pass
