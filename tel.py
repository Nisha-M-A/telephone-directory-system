from utilities import *

def tel_menu():
    while True:
        heading()
        print("""
                        Telephone Directory Maintaince Menu
                       ======================================
            1. Add Telephone Number
            2.Telephone Enquire 
            3. Go To Main Menu
        """)
        choice=int(input("Enter Your Choice: "))
        match choice:
            case 1:
                add_tel()
            case 2:
                enquire_menu()
            case 3:
                return
            case _:
                print("Invalid Choice!")

def add_tel():
    heading()
    print("""
                                    Add A Telephone number 
                                  ===========================
                """)
    emp_id=input("Enter Employee ID: ")
    dept_id=0
    loc=""
    name=""
    with open ("emp.txt", "r") as file:
        for line in file:
            line=line.strip()
            if not line: 
                continue
            if(line.split("|")[0]==emp_id):
                dept_id=int(line.split("|")[2])
                loc=line.split("|")[4]
                name=line.split("|")[1]
                break
    if dept_id==0:
        print("The Employee Doesn't Exists")
        return
    with open ("tel.txt","r+") as file:
        code=1
        for line in file:
            line=line.strip()
            if(line.split("|")[3]==str(dept_id)):
                code=code+1
        tel = str(dept_id) + f"{code:03d}"
        file.write(f"{tel}|{emp_id}|{name}|{dept_id}|{loc}\n")
    print("Location:",loc,"\nDepartment ID:",dept_id,"\nTelephone Number Allocated:",tel)


def enquire_menu():
    while True:
        heading()
        print("""
                            Telephone Enquiry Menu
                          ==========================
            1.Enquiry On Employee Name
            2.Enquiry On Telephone Number
            3.Go Back To Telephone Directory Maintaince
        """)
        choice=int(input("Enter Your Choice: "))
        match choice:
            case 1:
                enq_name()
            case 2:
                enq_tel()
            case 3:
                break
            case _:
                print("Invalid Choice!")    

def enq_name():
    heading()
    print("""
                                Telephone Number Enquire By Name 
                              ====================================
    """)
    a=[]
    exists=False
    emp_name=input("Enter Employee Name: ")
    with open("tel.txt", "r") as tel_file:      
        for tel_line in tel_file:
            tel_line=tel_line.strip()
            if(tel_line.split("|")[2].lower()==emp_name.lower()):
                exists=True
                d={}
                d["Name"]=emp_name.title()
                d["Location"]=tel_line.split("|")[4]
                d["DeptID"]=tel_line.split("|")[3]
                d["TelNumber"]=tel_line.split("|")[0]
                a.append(d)
    if not exists:
        print("Employee Name Doesn't Exist!")
        return
    print(f"{'Name':<20}{'Location':<15}{'DeptID':<25}{'TelNumber':<12}")
    for employee in a:
        print(f"{employee['Name']:<20}"
          f"{employee['Location']:<15}"
          f"{employee['DeptID']:<25}"
          f"{employee['TelNumber']:<12}")
    
            

def enq_tel():
    heading()
    print("""
                                    Telephone Number Enquire
                                  ============================
    """)
    tel=int(input("Enter Telephone Number: "))
    exists=False
    dept_id=0
    d={}
    with open ("tel.txt", "r") as file:
        for line in file:
            line=line.strip()
            if(int(line.split("|")[0])==tel):
                d["name"]=line.split("|")[2]
                d["loc"]=line.split("|")[4]
                dept_id=int(line.split("|")[3])
                exists=True
                break
    if not exists:
        print("Invalid Telephone Number")
        return
    with open ("dept.txt","r") as file:
        for line in file:
            line=line.strip()
            if(int(line.split("|")[0])==dept_id):
                d["deptid"]=line.split("|")[1]
                break
    print("Employee Name:",d['name'],"\nLocation:",d['loc'],"\nDepartment Name:",d['deptid'])
    return

