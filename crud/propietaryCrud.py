from models import propietary as Propietary

class propietaryCrud:

    def __init__(self):
        self.propietaries = []
    

    def createPropietary(self, document, name , lastName, email, phone):
        propietary = Propietary(document, name , lastName, email, phone)
        self.propietaries.append(propietary)
        return propietary
    
    def searchPropietaryByDocument(self, document):
        for propietary in self.propietaries:
            if propietary.document == document:
                return True
            else:
                return False
        return None