def check_if_file_is_empty(file_path):
    with open(file_path, "r") as f:
        return f.read(1) == ""

class Student:
    def __init__(self, id, name, surname, group, faculty, status):
        self.id = id
        self.name = name
        self.surname = surname
        self.group = group
        self.faculty = faculty
        self.status = status

    def __str__(self):
        return f"{self.id}, {self.name}, {self.surname}, {self.group}, {self.faculty}, {self.status}"

class Catalog:
    def __init__(self):
        self.catalog = []
        self.graduated_students = []
        self.session = 1  # Instance variable

    def check_if_faculty_exists(self, faculty):
        while True:
            if faculty in faculties:
                return faculty
            else:
                faculty = input("This faculty doesn't exist, please choose another: ")

    def load_students(self):
        if not check_if_file_is_empty("catalog.txt"):
            with open("catalog.txt", "r") as f:
                for line in f:
                    data = line.strip().split(", ")
                    if len(data) == 6:
                        student = Student(data[0], data[1], data[2], data[3], data[4], data[5])
                        self.catalog.append(student)

    def load_graduated_students(self):
        if not check_if_file_is_empty("graduated.txt"):
            with open("graduated.txt", "r") as f:
                for line in f:
                    data = line.strip().split(", ")
                    if len(data) == 6:
                        student = Student(data[0], data[1], data[2], data[3], data[4], data[5])
                        self.graduated_students.append(student)

    def enroll(self):
        id = input("Student ID: ")
        if any(student.id == id for student in self.catalog):
            print("A student with this ID already exists. Try a different ID.")
            return

        name = input("Student name: ")
        surname = input("Student surname: ")
        group = input("Student group: ")
        faculty = input("Faculty: ")
        faculty = self.check_if_faculty_exists(faculty)
        status = "not graduated"

        new_student = Student(id, name, surname, group, faculty, status)
        self.catalog.append(new_student)

        with open("catalog.txt", "a") as f:
            f.write(str(new_student) + "\n")

    def display_data(self):
        if not self.catalog:
            print("There are no non-graduated students.")
            return
        for i, student in enumerate(self.catalog):
            print(f"{i+1}) ID: {student.id}, Name: {student.name}, Surname: {student.surname}, Group: {student.group}, Faculty: {student.faculty}, Graduated: {student.status}")

    def graduate_student(self):
        id = input("Enter student ID: ")
        for student in self.catalog:
            if id == student.id:
                student.status = "graduated"
                self.graduated_students.append(student)
                with open("graduated.txt", "a") as f:
                    f.write(str(student) + "\n")

                self.catalog.remove(student)
                self.update_catalog_file()
                print(f"Student {student.name} {student.surname} has graduated.")
                return
        print("Student with this ID was not found.")

    def update_catalog_file(self):
        with open("catalog.txt", "w") as f:
            for student in self.catalog:
                f.write(str(student) + "\n")

    def display_graduated_students(self):
        if not self.graduated_students:
            print("There are no graduated students.")
            return
        for i, student in enumerate(self.graduated_students):
            print(f"{i+1}) ID: {student.id}, Name: {student.name}, Surname: {student.surname}, Group: {student.group}, Faculty: {student.faculty}, Graduated: {student.status}")

    def check_if_student_is_in_faculty(self):
        id = input("Enter student ID: ")
        faculty = input("Enter faculty: ")

        for student in self.catalog:
            if id == student.id and faculty == student.faculty:
                print(f"Student {student.name}, {student.surname} is part of the {faculty} faculty.")
                return
        print(f"Student with ID {id} does NOT belong to the {faculty} faculty.")

def see_faculties():
    if not faculties:
        print("There are no faculties.")
    else:
        print("Available faculties:")
        for faculty in faculties:
            print(faculty)

def add_new_faculty():
    new_faculty = input("Name the new faculty: ")
    faculties.append(new_faculty)
    with open('faculties.txt', 'a') as f:
        f.write(new_faculty + '\n')
    print(f"The faculty '{new_faculty}' has been added.")

def remove_faculty():
    faculty_to_remove = input("Enter the name of the faculty to remove: ")
    if faculty_to_remove in faculties:
        faculties.remove(faculty_to_remove)
        with open('faculties.txt', 'w') as f:
            for faculty in faculties:
                f.write(faculty + '\n')
        print(f"The faculty '{faculty_to_remove}' has been removed.")
    else:
        print(f"The faculty '{faculty_to_remove}' does not exist in the list.")

def create_account():
    print("Account Creation System\n")
    while True:
        login = input("Enter login: ")
        if login == "":
            print("You need to enter a valid login.")
            continue

        psw = input("Enter password: ")
        if psw == "":
            print("You need to enter a valid password.")
            continue

        with open("log.txt", "a") as f:
            f.write(login + "\n")
            f.write(psw + "\n")
        print("Account successfully created!")
        break

def check_if_account_was_already_created():
    with open("log.txt", "r") as f:
        return f.read(1) == ""

is_log = False
not_already_logged = check_if_account_was_already_created()

if not_already_logged:
    create_account()
    is_log = True
else:
    print("Login to the management system\n")
    login = input("Enter login: ")
    psw = input("Enter password: ")

    with open("log.txt", "r") as f:
        f_login = f.readline().strip()
        f_psw = f.readline().strip()

    if login == f_login and psw == f_psw:
        print("Login successful!")
        is_log = True
    else:
        print("Incorrect login or password!")
        is_log = False

if is_log:
    with open('faculties.txt', 'r') as f:
        faculties = f.readlines()
    faculties = [line.strip() for line in faculties]

    catalog = Catalog()
    instance = 1
    catalog.load_students()
    catalog.load_graduated_students()

    grad_instance = 1
    while True:
        print("\nChoose an option from the menu:")
        print("1) Enroll a new student")
        print("2) View non-graduated students")
        print("3) Graduate a student")
        print("4) Display graduated students")
        print("5) Check if a student belongs to a specific faculty")
        print("6) View faculties")
        print("7) Add a new faculty")
        print("8) Remove a specific faculty")
        print("9) Exit")

        option = int(input())

        if option == 1:
            catalog.enroll()
            instance += 1
        elif option == 2:
            catalog.display_data()
        elif option == 3:
            catalog.graduate_student()
            grad_instance += 1
        elif option == 4:
            catalog.display_graduated_students()
        elif option == 5:
            catalog.check_if_student_is_in_faculty()
        elif option == 6:
            see_faculties()
        elif option == 7:
            add_new_faculty()
        elif option == 8:
            remove_faculty()
        elif option == 9:
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
