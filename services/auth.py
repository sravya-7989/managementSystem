#  module for login signup for employee and admin


class AdminAuthentication:
    def adminLogin(self):
        pass
    
class EmployeeAuthentication:
        def __init__(self,db):
            self.db =db
            
            
        def createEmployee(self,e_name,e_email,password):
            self.e_name = e_name
            self.e_mail =e_email
            self.password =password
            self.db.createEMP(self.e_name,self.e_mail,self.password)
            
        def empLogin(self,email):
            return self.db.searchEmp(email)