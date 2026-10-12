class employee:
    company = "ITC"
    name = "aaditya"
    def show(self):
        print(f"the name of the company is {self.name} and the company is {self.company}")
        
        
class coder:
    language = "python"
    def printlanguage(self):
        print(f"out of all language here is your language {self.language}")
      
class programmer(employee, coder):
    company = "ITC INFOTECH"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good {self.language}language")   

a = employee()
b = programmer()

b.show()
b.printlanguage()
b.showlanguage()