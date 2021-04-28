from kps import KPS
# luokka perii luokan KPS
class KPSPelaajaVsPelaaja(KPS):
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto