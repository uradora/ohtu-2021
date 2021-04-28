
# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirto(self, ekan_siirto, tokan_siirto):
        if self._eka_voittaa(ekan_siirto, tokan_siirto) == "eka":
            self.ekan_pisteet += 1
        elif self._eka_voittaa(ekan_siirto, tokan_siirto) == "tasapeli":
            self.tasapelit += 1
        else:
            self.tokan_pisteet += 1

    def __str__(self):
        return f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}\nTasapelit: {self.tasapelit}"

    def _eka_voittaa(self, eka, toka):
        if eka == "k" and toka == "s":
            return "eka"
        elif eka == "s" and toka == "p":
            return "eka"
        elif eka == "p" and toka == "k":
            return "eka"
        elif eka == toka:
            return "tasapeli"

        return "toka"
