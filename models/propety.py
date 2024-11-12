class propiety:
    def __init__(self, crop , castralRegister , municipality):
        self.crop = crop
        self.castralRegister = castralRegister
        self.municipality = municipality
    
    @property
    def crop(self):
        return self._crop
    
    @crop.setter
    def crop(self, crop):
        self._crop = crop
    
    @property
    def castralRegister(self):
        return self._castralRegister
    
    @castralRegister.setter
    def castralRegister(self, castralRegister):
        self._castralRegister = castralRegister
    
    @property
    def municipality(self):
        return self._municipality
    
    @municipality.setter
    def municipality(self, municipality):
        self._municipality = municipality

