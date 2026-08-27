from utilities import *

def emp_menu():
    while True:
        heading()
        print("""
                        Employee Maintaince Menu
                      =============================
            1. Add Employee
            2. Print Employee Details 
            3. Go To Main Menu
        """)
        choice=int(input("Enter Your Choice: "))
        match choice:
            case 1:
                add_emp()
            case 2:
                display_emp()
            case 3:
                return
            case _:
                print("Invalid Choice!")

def add_emp():
    heading()
    print("""
                                Add A Employee 
                              ==================
            """)
    emp_name=input("Enter Employee Name: ")
    if(len(emp_name)==0 or len(emp_name)>25):
        print("Employee Name Exceeds 25 Characters")
        return 
    code=1000
    with open("emp.txt", "r") as file:
        for line in file:
            line=line.strip()
            if not line:
                continue
            code=int(line.split("|")[0])
            code=code+1
    print("Employee ID is: ",code)
    dept_code=int(input("Enter Department code: "))
    dept_name=""
    code_check=False
    with open("dept.txt","r") as dept_file:
        for line in dept_file:
            line=line.strip()
            if dept_code==int(line.split("|")[0]):
                code_check=True
                dept_name=line.split("|")[1]
                break
    if code_check==False:
        print("Invalid Department Code Entered")
        return
    print("Department name:",dept_name)
    loc=input("Enter Location: ")
    if(len(loc)>5):
        print("the location exceeds 5 characters")
        return
    with open ("emp.txt", "a") as file:
        file.write(f"{code}|{emp_name}|{dept_code}|{dept_name}|{loc}\n")
        print("Employee Added Successfully!")
        return

        

def display_emp():
    #print("Yet to do!")
    heading()
    print("""
                                List Of Employees 
                              =====================
            """)
    with open ("emp.txt", "r") as file:
        print(f"{'Employee ID':<15}"
        f"{'Employee Name':<20}"
        f"{'Department Code':<20}"
        f"{'Department Name':<25}"
        f"{'Location':<15}")
        for line in file:
            line=line.strip()
            print(f"{line.split('|')[0]:<15}"
            f"{line.split('|')[1]:<20}"
            f"{line.split('|')[2]:<20}"
            f"{line.split('|')[3]:<25}"
            f"{line.split('|')[4]:<15}")
    return