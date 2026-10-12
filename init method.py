class employee:
    
    language = "python"     # this is class attribute
    salary = 1200
    
    def __init__(self): # dunderr method run automatically)
        print("i am a creating a object")
            
    def getinfo(self):
        print(f"the language is  {self.language}. the salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("good morning")
        
harry = employee()
harry.name = "harry hari"
print(harry.name ,harry.salary)
