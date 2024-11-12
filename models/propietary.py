
class propietary:
    def __init__(self, document, name , lastName, email, phone):
        self.document = document
        self.name = name
        self.lastName = lastName
        self.email = email
        self.phone = phone
    
    @property
    def document(self):
        return self._document
    
    @document.setter
    def document(self, document):
        self._document = document

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def lastName(self):
        return self._lastName
    
    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        self._phone = phone