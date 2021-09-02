n= int(input("enter the number of students"))
student_info = dict() #empty dictionry
for a in range(0,n):
    x=input("Enter the name of the student: ")
    roll_number=int(input("Enter the roll number of the student: "))
    age=int(input("Enter the age of the student: "))
    blood_type=input("Enter the blood type of the student: ")
    phone_number=int(input("Enter the phone number of the student: "))
    grade = input("Enter the grade of the student: ")
    student_info [x]={'roll_number':roll_number,'age':age,'blood type':blood_type, 'phone_number':phone_number, 'grade':grade}
    print()
print(student_info)
print()
#searching funtion
s1=input("do you wanna seartch a dictionry: Y/N")
if 'Y' == s1:
    s= input("enter the name to be searched: ")
    print(student_info.get(s))
print()
    #update the dict
apt= input("do you wanna update the dictionary: (Y/N)")

if 'Y' == apt:
    update_name = input("enter the name of the student to update")
    d=input("enter the key")
    d1=input("enter the value")
    student_info1=dict()
    student_info1[update_name] = {d: d1}
    student_info.update(student_info1)
    print(student_info)
else:
    print()
print()

del_1 = input("enter the name to be deleted: ")
del2= student_info.pop(del_1)
print(del2)