class employee:
    company = "ITC"
    salary = 1200
    def show(self):
        print(f"the name of the comp-any is {self.company} and the salary is {self.salary}")
        
        
class programmer(employee):
    company = "ITC INFOTECH"
    # language = "py"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good {self.language}language")


a = employee()
b = programmer()

print(a.company , b.company)
print(a.salary , b.salary)
# print(b.language)
               