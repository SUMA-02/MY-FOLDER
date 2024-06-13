emp_details={}
prjt_dtls={}
prjt_members={}
def gen_emp_id():
    return random.randint(1000,9999)
def gen_prjt_id():
    return random.randint(10000,99999)
def create():
    prjt_id=gen_prjt_id()
    print("Project ID: ",prjt_id)
    pjt_nm=input("Enter_Project_Name : ")
    total_mmbrs=int(input("Enter_Total_Members : "))
    Dura=int(input("Enter_Total_Duration in hours : "))
    prjt_info={'prjt_nm':pjt_nm,'ttl_mems':total_mmbrs,'dur':Dura}
    prjt_dtls[prjt_id]=prjt_info
    prjt_emp={}
    for i in range(total_mmbrs):
        emp_id=gen_emp_id()
        print("Employee ID: ",emp_id)
        nm=input("Enter_Employee_Name : ")
        em_age=int(input("Enter_Employee_Age : "))
        mail_id=input("Enter_Employee_Email_Id : ")
        ph_no=input("Enter_Employee_Phone_Number : ")
        emp_info={'empid':emp_id,'name':nm,'age':em_age,'mail':mail_id,'pno':ph_no,'salary':0}
        emp_details[emp_id]=emp_info   
        prjt_emp[emp_id]=emp_info
    prjt_members[prjt_id]=prjt_emp
def individual_display():
    print("1.Display employee 2.Display project")
    ch=int(input("Enter your choice : "))
    if(ch==1):
        if(len(emp_details)==0):
                print("---No Employees Register---")
        else:
            emp_id=int(input("Enter employee id : "))
            print("----------------------------------------------------------------------------------------")
            print("|Name\t\tAge\t\tE-mail\t\t\tPhone_No\t\tSalary|")
            print("----------------------------------------------------------------------------------------")
            if emp_id in emp_details:
                print("%s\t\t%d\t\t%s\t\t%s\t\t%d"%(emp_details[emp_id]['name'],emp_details[emp_id]['age'],emp_details[emp_id]['mail'],emp_details[emp_id]['pno'],emp_details[emp_id]['salary']))
            else:
                print("Invalid empolyee id")
    elif(ch==2):
        if(len(prjt_dtls)==0):
                print("No project Register")
        else:
            prjt_id=int(input("enter project id : "))
            print("--------------------------------------------------------------------------------")
            print("|Project_Name\t\tTotal_Members\t\tProject_Duration|")
            print("--------------------------------------------------------------------------------")
            if prjt_id in prjt_dtls:
                print("%s\t\t\t%d\t\t\t%d"%(prjt_dtls[prjt_id]['prjt_nm'],prjt_dtls[prjt_id]['ttl_mems'],prjt_dtls[prjt_id]['dur']))
            else:
                print("invalid prjt id")
def display():
    print("1.display employee 2.display project")
    ch=int(input("enter your choice : "))
    if(ch==1):
        if(len(emp_details)==0):
                print("No Employees Register")
        else:
            print("----------------------------------------------------------------------------------------")
            print("|Name\t\tAge\t\tE-mail\t\t\tPhone_No\t\tSalary|")
            print("----------------------------------------------------------------------------------------")
            for i in emp_details:
                print("%s\t\t%d\t\t%s\t\t%s\t\t%d"%(emp_details[i]['name'],emp_details[i]['age'],emp_details[i]['mail'],emp_details[i]['pno'],emp_details[i]['salary']))
    elif(ch==2):
        if(len(prjt_dtls)==0):
                print("No project Register")
        else:
            print("--------------------------------------------------------------------------------")
            print("|Project_Name\t\tTotal_Members\t\tProject_Duration|")
            print("--------------------------------------------------------------------------------")
            for i in prjt_dtls:
                print("%s\t\t%d\t\t\t%d"%(prjt_dtls[i]['prjt_nm'],prjt_dtls[i]['ttl_mems'],prjt_dtls[i]['dur']))

def update():
    print("1.update employee 2.update project")
    ch=int(input("enter your choice : "))
    if(ch==1):
        if(len(emp_details)==0):
                print("No Employees Register")
        else:
            emp_id=int(input("enter emp id : "))
            key=input("enter key to change(name/age/mail/pno)")
            if emp_id in emp_details:
                for i in emp_details[emp_id].keys():
                    if i==key:
                        new_value=input(f"enter new {key}")
                        if new_value.isdigit():
                            new_value=int(new_value)
                            emp_details[emp_id][key]=new_value
                        else:
                            emp_details[emp_id][key]=new_value
            else:
                print("Empoloyee id did not Find")
    elif(ch==2):
        if(len(prjt_dtls)==0):
                print("No Projects Register")
        else:
            prjt_id=int(input("enter project id : "))
            key=input("enter key to change(prjt_nm/ttl_mems/dur)")
            if prjt_id in prjt_dtls:
                for i in prjt_dtls[prjt_id].keys():
                    if i==key:
                        new_value=input(f"enter new {key}")
                        if new_value.isdigit():
                            prjt_dtls[prjt_id][key]=new_value
                        else:
                            prjt_dtls[prjt_id][key]=new_value
            else:
                print("Project Id not Found")
                  
def delete():
    if(len(emp_details)==0):
            print("No Employees Register")
    else:
        em_id=int(input("Enter employee id : "))
        if em_id in emp_details:
            emp_details.pop(em_id)
            print("employee details deleted successfully")

def calculate_billable_hours():
    emp_id = int(input("enter emp id: "))
    prjt_id = int(input("enter project id: "))
    
    if emp_id in emp_details and prjt_id in prjt_dtls:
        login = float(input("enter log_in time: "))
        logout = float(input("enter log_out time: "))
        total_hrs = logout - login
        extra_hrs = total_hrs - 6
        
        if total_hrs == 6:
            price = total_hrs * 100
        elif total_hrs <= 5:
            price = total_hrs * 80
        else:
            price = 6 * 100 + extra_hrs * 200

        prjt_hrs = prjt_dtls[prjt_id]['dur']
        if prjt_hrs > total_hrs:
            remaining_hrs = prjt_hrs - total_hrs
        else:
            0
        emp_details[emp_id]['salary'] += price
        emp_details[emp_id]['remaining'] = remaining_hrs

        
        if prjt_id in prjt_members and emp_id in prjt_members[prjt_id]:
            if 'total_hours' not in prjt_members[prjt_id][emp_id]:
                prjt_members[prjt_id][emp_id]['total_hours'] = 0  
            prjt_members[prjt_id][emp_id]['total_hours'] += total_hrs
            prjt_members[prjt_id][emp_id]['remaining'] = remaining_hrs
            
            prjt_dtls[prjt_id]['dur'] = remaining_hrs
        else:
            print("Project or employee not found in prjt_members.")

        print("Total hours worked:", emp_details[emp_id]['total_hours'])
        print("Remaining hours for the project:", prjt_dtls[prjt_id]['dur'])
def generate_time_summary_report():
    project_id = int(input("Enter project id : "))
    a=0
    for i in prjt_members[project_id].keys():
        a=int(i)
        break
    
    if project_id in prjt_members:
        project_employees = prjt_members[project_id]

        print(f"Employee Details for Project ID: {project_id}")
        print("----------------------------------------------------------------------------------------")
        print("|Name\t\tAge\t\tE-mail\t\t\tPhone_No\t\t\tSalary |")
        print("----------------------------------------------------------------------------------------")
        for emp_id, emp_info in project_employees.items():
            print(f"{emp_info['name']}\t\t{emp_info['age']}\t\t{emp_info['mail']}\t\t{emp_info['pno']}\t\t{emp_info['salary']}")
    else:
        print("Project ID not found.")
    print("**********")
    print("*Remaining_Hours : ",prjt_dtls[project_id]['dur']," *")
    print("**********")


while True:
    print('1.create 2.display 3.update 4.delete 5.calculate_billable_hrs 6.generate_time_summary_report 7.individual_display')
    ch=int(input("enter choice:"))
    if(ch==1):
        create()
    elif(ch==2):
        display()
    elif(ch==3):
        update()
    elif(ch==4):
        delete()
    elif(ch==5):
        calculate_billable_hours() 
    elif(ch==6):
        generate_time_summary_report()
    elif(ch==7):
        individual_display()
    elif(ch==8):
        break