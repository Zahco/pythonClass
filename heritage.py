class Piece:
    name = ''
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class Maison:
    chambre = None
    salon = None

    def __init__(self):
        self.setChambre(Piece('chambre'))
        self.setSalon(Piece('salon'))

    def getChambre(self):
        return self.chambre
    def getSalon(self):
        return self.salon

    def setChambre(self, chambre):
        self.chambre = chambre
    def setSalon(self, salon):
        self.salon = salon

    def __repr__(self):
        str = ""
        if self.getChambre() != None :
            str = str + repr(self.getChambre()) + " "
        if self.getSalon() != None :
            str = str + repr(self.getSalon()) + " "
        return str

class Villa(Maison):
    jardin = None

    def __init__(self):
        super().__init__()
        self.setJardin(Piece('jardin'))
    
    def getJardin(self):
        return self.jardin
    def setJardin(self, jardin):
        self.jardin = jardin

    def __repr__(self):
        str = Maison.__repr__(self)
        if self.getJardin() != None :
            str = str + repr(self.getJardin()) + " "
        return str

appartement = Maison()
print("appartement : ", appartement)
villa = Villa()
print("villa : ", villa)


