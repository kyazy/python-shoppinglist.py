import sqlite3

# Verbindung zu sqlite-DB (falls nicht vorhanden ist, dann wird die erstellt.)
conn = sqlite3.connect('studenden.db')

# Erstellung von Cursor um sql-Befehl durchzuführen. 
cursor = conn.cursor()

# Erstellung von Tabellen in studenden.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    age INTEGER NOT NULL, 
    course VARCHAR(32) NOT NULL
    );
''')
# Erste Funktion hinzufügen (CREATE)
def add_student(name, age, course):
    cursor.execute('''
    INSERT INTO Students (name, age, course) VALUES (?, ?, ?)
    ''', (name, age, course))
    conn.commit()
    print(f"{name} wurde hinzugefügt")

# Erstellung von READ funktion
def show_students():
    cursor.execute('SELECT id, name FROM Students')
    students = cursor.fetchall()
    for name in students:
        print(name)

# Update function to update student data
def update_student(id, name, age, course):
    cursor.execute('''
    UPDATE Students SET name = ?, age = ?, course = ?
    WHERE id = ?               
    ''',(name, age, course, id))
    conn.commit()
    print(f"updated student with id {id}")

# Adding a delete function to delete a student

def delete_student(id):
    cursor.execute('''
    DELETE FROM Students WHERE id = ?                
    ''',(id,))
    conn.commit()
    print(f"Student has been deleted with id {id}")

# add_student('Abdullah', 150, 'TECHSTARTER')
# update_student(2, "Cansin", 34, "TECHSTARTER")
delete_student(2)
show_students()



