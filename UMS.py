import sqlite3

# Create a connection to the Database

conn = sqlite3.connect('class_lists.db')

# Create a cursor 
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE IF NOT EXISTS students (
    first_name text,
    last_name text,
    age integer,
    email text,
    course text
    )""")

c.execute("UPDATE Students SET age = :age",
{"age":"age"})

# To drop(delete a table)
# c. execute(""""DROP TABLE students""")

# Inserting a single value
c.execute("INSERT INTO students VALUES ('Nimah', 'Masuud', 18, 'nimahmasuud@gmail.com', 'Geophysics' )")

# Inserting multiples values at once
all_students = [
                  ('Rofiat', 'Masuud', 19, 'rofiatmasuud@gmail.com', 'Biology Education'),
                  ('Ihuoma', 'Gold', 20, 'ihuomagold@gmail.com', 'Electrical Engineering'),
                  ('Suliyat', 'Dauda', 21, 'suliyatdauda@gmail.com', 'Economic'),
                  ('Benjamin', 'Adewusi', 22, 'bennite@gmail.com', 'Geology' )
                ]

# To Query the database
c.execute("SELECT * FROM students")
lists = c.fetchall()

# print("first_name", "\t\t", "last_name", "\t\t", "age", "\t\t", "email", "\t\t", "course")
# print ("----------------------------------------------------------------------------------")
for item in lists:
    print(item[0], " ", item[1], "\t\t", item[2], "\t\t", item[3], "\t\t", item[4])

print("Command Executed successfully.....")

# Commit the database
conn.commit()

# Close the connection
conn.close()