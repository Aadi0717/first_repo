class employee:
    
    language = "python"     # this is class attribute
    salary = 1200
    
    def getinfo(self):
        print(f"the language is  {self.language}. the salary is {self.salary}")
        
    def greet(self):
        print("good morning")
        
harry = employee()
harry.getinfo()
harry.greet()