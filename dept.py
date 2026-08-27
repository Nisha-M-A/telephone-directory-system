from utilities import *    
def department_menu():
    while True:
        heading()
        print("""
                        Department Maintainance
                      ===========================
            1. Add Department
            2. Print Department Details 
            3. Go To Main Menu
        """)
        choice=int(input("Enter Your Choice: "))
        match choice:
            case 1:
                add_dept()
            case 2:
                display_dept()
            case 3:
                return
            case _:
                print("Invalid Choice!")


def add_dept():
    heading()
    print("""
                            Add A Department 
                          =====================
        """)
    dept_name=input("Enter Department Name: ")
    if(len(dept_name)>15):
        print("Department Name Exceeds 15 Characters")
        return 
    exists=False
    code=1000
    with open("dept.txt", "r+") as file:
        for line in file:
            line=line.strip()
            if not line:
                continue
            code=int(line.split("|")[0])
            if(line.split("|")[1].lower()==dept_name.lower()):
                exists=True
                break
            code=code+1
                
        if(exists):
            print("Deparment Name Already Exists!")
            return
            
        file.write(f"{code}|{dept_name}\n")
        print("Department Code:", code)
        print("Department Added Successfully!")
        return


def display_dept():
    heading()
    print("""
                                List Of Departments 
                              ========================
            """)
    with open ("dept.txt", "r") as file:
        print("Department Code          Department Name")
        for line in file:
            line=line.strip()
            print(line.split("|")[0],"\t\t\t",line.split("|")[1])
    return




