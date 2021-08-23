n=int(input("Enter the number of student data to be stored: "))
student_info = dict()
for a in range(0,n):
    x = input("Enter the name of the student: ")
    roll_number=int(input("Enter the roll number of the student: "))
    age=int(input("Enter the age of the student: "))
    blood_type=input("Enter the blood type of the student: ")
    phone_number=int(input("Enter the phone number of the student: "))
    grade = input("Enter the grade of the student: ")
    student_info [x]={'roll_number':roll_number,'age':age,'blood type':blood_type, 'phone_number':phone_number, 'grade':grade}
    print()
print(student_info)

s= input("enter the name to be searched: ") #searching funtion
print(student_info.get(s))
