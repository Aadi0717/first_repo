class employee:
    
    language = "python"     # this is class attribute
    salary = 1200
    
    
aadi = employee()
aadi.name = "Aaditya jain"      # this is instance attribute
print(aadi.name, aadi.salary, aadi.language)

aanya = employee()
aanya.name = "Aanya tamrakar"       # this is instance attribute
print(aanya.name, aanya.salary, aanya.language)
    
# here name is instance attribute and language and salary is class attribute
# as they directly belong to class