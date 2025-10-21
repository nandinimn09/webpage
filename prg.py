import mysql.connector

# connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # change if needed
    password="root",  # replace with your MySQL password
    database="student_db"
)

cursor = conn.cursor()

# function to insert new student
def add_student(name, age, course):
    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)
    cursor.execute(query, values)
    conn.commit()
    print("✅ Student added successfully!")

# function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# function to update a student’s info
def update_student(student_id, name):
    query = "UPDATE students SET name = %s WHERE id = %s"
    values = (name, student_id)
    cursor.execute(query, values)
    conn.commit()
    print("✅ Student updated successfully!")

# function to delete a student
def delete_student(student_id):
    query = "DELETE FROM students WHERE id = %s"
    value = (student_id,)
    cursor.execute(query, value)
    conn.commit()
    print("✅ Student deleted successfully!")

# menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        add_student(name, age, course)

    elif choice == '2':
        view_students()

    elif choice == '3':
        sid = int(input("Enter student ID: "))
        new_name = input("Enter new name: ")
        update_student(sid, new_name)

    elif choice == '4':
        sid = int(input("Enter student ID to delete: "))
        delete_student(sid)

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")

# close connection
conn.close()
