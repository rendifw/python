# Bikin program untuk masukkan data student(name, NIM, major, class) dan score mereka 


major_list = ["Information Systems", "Computer Science", "Data Science", "Accounting", "Finance", "Taxation"]
students = []

while True:
    print("""Student Menu:
    1. Add student
    2. View students
    3. View student by id
    4. View student by slicing
    5. Update student data
    6. Delete student""")

    menu_input = input("Select menu >> ")
    while menu_input.isalpha() or int(menu_input) < 1 or int(menu_input) > 6:
        menu_input = input("Choose menu from 1 - 6 >> ")
    
    menu_input = int(menu_input)

    if menu_input == 1:
        student_name = input("Add a student name: ")
        while not student_name.istitle():
            print("Invalid name, please write in title case")
            student_name = input("Add a student name (title case): ")
        
        student_nim = input(f"\nAdd {student_name}'s NIM: ")
        while not student_nim.isdigit() or len(student_nim) != 10:
            print("Invalid NIM, it should be 10 digits")
            student_nim = input(f"Add {student_name}'s NIM (10 digits): ")
        student_nim = int(student_nim)

        student_major = input(f"\nAdd {student_name}'s major: ")
        while student_major not in major_list:
            print("Invalid major, it should be from the list of majors")
            print(f"List of majors: {major_list}")
            student_major = input(f"Add {student_name}'s major: ")

        student_class = input(f"\nAdd {student_name}'s class: ")
        while len(student_class) != 4:
            print("Invalid class, it should consist of four characters!")
            student_class = input(f"Add {student_name}'s class (4 characters): ")

        while True:
            try:
                student_gpa = float(input(f"\n1Add {student_name}'s GPA: "))
                if student_gpa < 0 or student_gpa > 4:
                    raise ValueError
                break
            except ValueError:
                print("Invalid GPA, it should be a number from 0 - 4!")

        new_student = {
            "Name": student_name,
            "NIM": student_nim,
            "Major": student_major,
            "Class": student_class,
            "GPA": student_gpa
        }

        students.append(new_student)
        print("\nNew Student", student_name, "Added Successfully!\n")

    elif menu_input == 2:
        for i, student in enumerate(students):
            print("=" * 25)
            print(f"""Student No.{i + 1}
Name\t:\t{student["Name"]}
NIM\t:\t{student["NIM"]}
Major\t:\t{student["Major"]}
Class\t:\t{student["Class"]}
GPA\t:\t{student["GPA"]}
""")
    elif menu_input == 3:
        if len(students) == 0:
            print("No students found")
        view_id = int(input(f"View student by number [1 - {len(students)}]: "))
        while True:
            if view_id <= len(students) and view_id >= 1:
                print("=" * 25)
                print(f"""Student No.{view_id}
Name\t:\t{students[view_id - 1]["Name"]}
NIM\t:\t{students[view_id - 1]["NIM"]}
Major\t:\t{students[view_id - 1]["Major"]}
Class\t:\t{students[view_id - 1]["Class"]}
GPA\t:\t{students[view_id - 1]["GPA"]}
""")
                break
            else:
                print(f"Invalid input, must be a number from 1 - {len(students)}")
                view_id = int(input(f"View student by number [1 - {len(students)}]: "))

    elif menu_input == 4:
        if len(students) == 0:
            print("No students found")
        view_id1 = int(input(f"View student by number [1 - {len(students)}]: "))
        view_id2 = int(input(f"View student by number [{view_id1} - {len(students)}]: "))

        for student in students[view_id1 : view_id2]:
            print(f"""Student No.{i + 1}
Name\t:\t{student["Name"]}
NIM\t:\t{student["NIM"]}
Major\t:\t{student["Major"]}
Class\t:\t{student["Class"]}
GPA\t:\t{student["GPA"]}
""")

    elif menu_input == 5:
        if len(students) == 0:
            print("No students to update!")
        
    elif menu_input == 6:
        if len(students) == 0:
            print("No students to delete!")
        


# Use for key, value in dict.items(): next time instead of printing one by one