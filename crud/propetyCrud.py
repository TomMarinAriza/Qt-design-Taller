from models import propety as Propety

class propetyCrud:
    def __init__(self):
        self.propeties = []
    
    def createPropety(self, crop , castralRegister , municipality):
        propety = Propety(crop , castralRegister , municipality)
        self.propeties.append(propety)
        return propety
