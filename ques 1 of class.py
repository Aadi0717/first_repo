class animals:
    pass   


class pets(animals):
    pass

class dog(pets): 
    @staticmethod
    def barks():
        print("BOW BOW!!")
        
d = dog()
d.barks()
        