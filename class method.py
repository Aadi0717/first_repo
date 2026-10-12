class employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")
    
e = employee()
e.a = 45

e.show()  

# show the class attribute not insatance attribute      