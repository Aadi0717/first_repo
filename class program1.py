class programmer:
    company = "microsoft"
    def __init__(self,name,salary,pin) :
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = programmer("Aaditya", 1200, 485001)
print(p.name, p.salary, p.pin, p.company)
     
a=programmer("Aanya", 1300, 485004)
print(a.name, a.salary, a.pin, a.company)