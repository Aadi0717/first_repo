class employee:
    
    language = "python"     # this is class attribute
    salary = 1200
    
    def getinfo(self):
        print(f"the language is  {self.language}. the salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("good morning")
        
harry = employee()
harry.greet()
harry.getinfo()
