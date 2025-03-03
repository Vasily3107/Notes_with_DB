from Note import Note
import pyodbc

class NoteHandler:
    def __init__(self, server, database, table):
        self.__server   = server
        self.__database = database
        self.__table    = table
        self.__dsn      = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.__server};DATABASE={self.__database};Trusted_Connection=yes;'


    def get_notes(self) -> list[Note]:
        try:
            conn = pyodbc.connect(self.__dsn)
            cursor = conn.cursor()

            cursor.execute(f"SELECT * FROM {self.__table}")
            rows = cursor.fetchall()

            notes = []
            for row in rows:
                notes.append(Note(*row))

            cursor.close()
            conn.close()
            return notes

        except:
            return None


    def get_note_names(self) -> list[str]:
        return list(map(lambda i: i.name, self.get_notes()))


    def add_note(self, note: Note) -> str:
        try:
            conn = pyodbc.connect(self.__dsn)
            cursor = conn.cursor()

            if note.name in self.get_note_names():
                return f"Name \"{note.name}\" is already taken"

            insert_query = f"INSERT INTO {self.__table} ([name], [text]) VALUES (?, ?)"
            values = (note.name, note.text)

            cursor.execute(insert_query, values)
            conn.commit()

            cursor.close()
            conn.close()
            return "Note was added successfully"

        except Exception as e:
            return f"ADD NOTE ERROR: {e}"


    def del_note(self, note_name: str) -> str:
        try:
            if note_name not in self.get_note_names():
                return f"Note with name \"{note_name}\" wasn't found"

            conn = pyodbc.connect(self.__dsn)
            cursor = conn.cursor()

            delete_query = f"DELETE FROM {self.__table} WHERE [name] = ?"

            cursor.execute(delete_query, (note_name,))
            conn.commit()

            cursor.close()
            conn.close()
            return "Note was deleted successfully"

        except Exception as e:
            return f"DEL NOTE ERROR: {e}"
