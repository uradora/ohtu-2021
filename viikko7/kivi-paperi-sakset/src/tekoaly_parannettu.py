# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = [None] * muistin_koko
        self._vapaa_muisti_indeksi = 0

    def aseta_siirto(self, siirto):
        # jos muisti täyttyy, unohdetaan viimeinen alkio
        if self._vapaa_muisti_indeksi == len(self._muisti):
            self._muisti[-1] = 0

            self._vapaa_muisti_indeksi -= 1

        self._muisti[self._vapaa_muisti_indeksi] = siirto
        self._vapaa_muisti_indeksi += 1

    def anna_siirto(self):
        if self._vapaa_muisti_indeksi < 2:
            return "k"

        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1]

        siirrot = {}

        for i in range(0, self._vapaa_muisti_indeksi - 1):
            if viimeisin_siirto == self._muisti[i]:
                siirrot[self._muisti[i + 1]] = siirrot.get(self._muisti[i + 1], 0)
                siirrot[self._muisti[i + 1]] += 1

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if siirrot.get("k", 0) > siirrot.get("p", 0) or siirrot.get("k", 0) > siirrot.get("s", 0):
            return "p"
        elif siirrot.get("p", 0) > siirrot.get("k", 0) or siirrot.get("p", 0) > siirrot.get("s", 0):
            return "s"
        else:
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
