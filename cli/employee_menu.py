from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB
from validation.email_validator import email_vali
from validation.pass_validator import password_vali
from getpass4 import getpass
from utils.pass_hash import password_hasher,check_password

#this object of employee repo
emp_db = EmployeeDB()
#this object of employee auth
emp_auth =EmployeeAuthentication(emp_db)


#this function for signup new employee
def employeeSignup():
    print('employee signup:')
    name = input('enter your name:')
    email = input('enter your email:')
    verify_email=emp_db.searchEmp(email)
    if verify_email is  None:
        if email_vali(email=email) is not None:
            password = getpass('enter your password:')
            confirm_pw=getpass('enter password again : ')
            if password==confirm_pw:
                if password_vali(password):
                    password = password_hasher(password)
                    emp_auth.createEmployee(name,email,password)
                else:
                    print('''
password is not valid 
password should  be minimum length of 5
password sholud contain uppercase character ex:A,S,D....
password sholud contain special character ex:@,#....
passwod should contain one digit ex:1 2 3....
''')
                    employeeSignup()
            else:
                print('password and conform password are not same')
                employeeSignup()    
        else:
            print('''
email id is not valid!!!!!!!
''')
            employeeSignup()
    else:
        print(f' account with this account Email id {email} is already exists so login')
        employeeLogin()
    
def employeeLogin():
    print('employee login')
    email = input('Enter your email:')
    password = getpass('enter your password:')
    hashed_pw = emp_auth.empLogin(email)
    if check_password(password,hashed_pw):
        print('login successfull!!!!')
    else:
        print('login failed')