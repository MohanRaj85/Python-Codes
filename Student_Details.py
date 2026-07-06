import sqlite3

# Database Connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    email TEXT UNIQUE
)
""")
conn.commit()


def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    email = input("Enter Email: ")

    try:
        cursor.execute(
            "INSERT INTO students(name, age, course, email) VALUES(?,?,?,?)",
            (name, age, course, email)
        )
        conn.commit()
        print("Student Added Successfully!")
    except sqlite3.IntegrityError:
        print("Email already exists!")


def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if records:
        print("\n--- Student Records ---")
        for row in records:
            print(row)
    else:
        print("No records found.")


def search_student():
    student_id = input("Enter Student ID: ")

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    record = cursor.fetchone()

    if record:
        print(record)
    else:
        print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to Update: ")

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    record = cursor.fetchone()

    if not record:
        print("Student not found.")
        return

    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    course = input("Enter New Course: ")
    email = input("Enter New Email: ")

    try:
        cursor.execute("""
        UPDATE students
        SET name=?, age=?, course=?, email=?
        WHERE id=?
        """, (name, age, course, email, student_id))

        conn.commit()
        print("Student Updated Successfully!")
    except sqlite3.IntegrityError:
        print("Email already exists!")


def delete_student():
    student_id = input("Enter Student ID to Delete: ")

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student not found.")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")

conn.close()