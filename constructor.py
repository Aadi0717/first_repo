class employee:
    
    language = "python"     # this is class attribute
    salary = 1200
    
    def __init__(self , name, salary , language):# dunderr method run automatically)
        self.name = name
        self.salary = salary
        self.language = language
        
        print("i am a creating a object")
            
    def getinfo(self):
        print(f"the language is  {self.language}. the salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("good morning")
        
harry = employee("harry hari", 1200, "javascript")
print(harry.name ,harry.salary, harry.language)
