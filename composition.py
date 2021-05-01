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

appartement = Maison()
appartement.setChambre(Piece('chambre'))
appartement.setSalon(Piece('salon'))
print("appartement : ", appartement)

villa = Maison()
villa.setChambre(Piece('chambre'))
villa.setSalon(Piece('salon'))
villa.setJardin(Piece('jardin'))
print("villa : ", villa)

