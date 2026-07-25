import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT,marks INTEGER)''')

cursor.execute("INSERT INTO students (name, marks) VALUES ('Daneshwar', 95)")
conn.commit()

print("Student Data Added Successfully")
