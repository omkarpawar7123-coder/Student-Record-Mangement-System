students = {}

while True:
    print("\n1.Add 2.View 3.Edit 4.Delete 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        roll = input("Roll: ")
        name = input("Name: ")
        age = input("Age: ")
        marks = input("Marks: ")
        subject = input("Subject: ")

        students[roll] = [name, age, marks, subject]

    elif ch == "2":
        print(students)

    elif ch == "3":
        roll = input("Roll: ")
        if roll in students:
            students[roll] = input("Name: "), input("Age: "), input("Marks: "), input("Subject: ")

    elif ch == "4":
        roll = input("Roll: ")
        students.pop(roll, None)

    elif ch == "5":
        break