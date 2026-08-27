from dept import *
from utilities import *    
from emp import *
from tel import *

heading()
print("""                            
                            Login Screen
                          ================
""")
user_id=input("Enter User ID :")
found=False
with open("emp.txt","r") as file:
    for line in file:
        line=line.strip()
        emp_id=line.split("|")[0]
        if emp_id==user_id:
            found=True
            break
if found:
    while True:
        heading()
        print("""
                            Main Menu
                          ==============
            1.Department Maintainance
            2.Employee Maintainance
            3.Telephone Directory Maintainance
            4.Exit
        """)
        choice=int(input("Enter Your Choice: "))
        match choice:
            case 1:
                department_menu()
            case 2:
                emp_menu()
            case 3:
                tel_menu()
            case 4:
                break
            case _:
                print("Invalid Choice!")

else:
    print("Login Failed")