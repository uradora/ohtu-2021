from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self):
        self._tekoaly = Tekoaly()
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()

        print("Tietokoneen siirto: " + tokan_siirto)

        return tokan_siirto