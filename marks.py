students = {"Aman":[85,90,78],"Riya":[92,88,95],"Zoya":[70,65,80]}
print(" ----Average & grade---- ")
for name,marks in students.items():
    avg = sum(marks)/len(marks)
    
    if  avg > 85:
        grade = "A"
    elif 70 < avg < 85:
        grade = "B"
    elif 50 < avg < 70:
        grade = "C"
    elif avg < 50:
        grade = "F"

    print(f"{name} {avg:.2f} {grade}")
topper_name = ""
highest_avg = -1
for name,marks in students.items():
    avg = sum(marks)/ len(marks)
    if avg > highest_avg:
        highest_avg = avg
        topper_name = name
print(f"Topper: {topper_name}")


while True:
    print("""----Menu----
    Add Student = 1
    View All = 2
    Show topper = 3
    Exit = 4""")
    a = int(input("Enter a number b/w 1 to 4 to select menu: "))
    if a == 1:
        name = input("Enter Student Name You Want to Add: ")
        if name in students:
            print("student already exists.")
            continue

        marks = []
        vlaid = True
        for i in range(1,4):
            mark = float(input(f"Enter marks {i}: "))
            if mark < 0 or mark > 100:
                print("Invalid mark,try again.")
                valid = False
                break
            marks.append(mark)

        if valid:
            students[name] = marks

    elif a == 2:
        for name, marks in students.item():
            avg = sum(marks) / len(marks)
            if avg >= 85:
                grade = "A" 
            elif avg >= 70:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            else:
                grade = "F"
            print(f"{name} {avg:.2f} {grade}") 

    elif a == 3:
        topper_name = ""
        highest_avg = -1
        for name, marks in students.items():
            avg = sum(marks) / len(marks)
            if avg > highest_avg:
                highest_avg = avg
                topper_name = name
        print(f"Topper: {topper_name}")

    elif a == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice , try again.")
          