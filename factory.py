class Piece:
    name = ''
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class Maison:
    chambre = None
    salon = None
    jardin = None

    @staticmethod
    def createAppartement():
        appartement = Maison()
        appartement.setChambre(Piece('chambre'))
        appartement.setSalon(Piece('salon'))
        return appartement
    
    @staticmethod
    def createVilla():
        villa = Maison()
        villa.setChambre(Piece('chambre'))
        villa.setSalon(Piece('salon'))
        villa.setJardin(Piece('jardin'))
        return villa
    
    @staticmethod
    def createVillaBis():
        villa = Maison.createAppartement()
        villa.setJardin(Piece('jardin'))
        return villa

    def getChambre(self):
        return self.chambre
    def getSalon(self):
        return self.salon
    def getJardin(self):
        return self.jardin

    def setChambre(self, chambre):
        self.chambre = chambre
    def setSalon(self, salon):
        self.salon = salon
    def setJardin(self, jardin):
        self.jardin = jardin

    def __repr__(self):
        str = ""
        if self.getChambre() != None :
            str = str + repr(self.getChambre()) + " "
        if self.getSalon() != None :
            str = str + repr(self.getSalon()) + " "
        if self.getJardin() != None :
            str = str + repr(self.getJardin()) + " "
        return str


print("appartement : ", Maison.createAppartement())
print("villa : ", Maison.createVilla())
print("villa bis : ", Maison.createVillaBis())

