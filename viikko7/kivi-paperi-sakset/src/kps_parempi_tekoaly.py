from tekoaly_parannettu import TekoalyParannettu
from kps import KPS

class KPSParempiTekoaly(KPS):
    def __init__(self, KPS):
        self._tekoaly = TekoalyParannettu(10)
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)

        print("Tietokoneen siirto: " + tokan_siirto)

        return tokan_siirto