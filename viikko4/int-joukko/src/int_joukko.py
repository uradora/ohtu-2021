KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None or not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None or not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == self.kapasiteetti:
                self.kasvata()
            return True

        return False

    def kasvata(self):
        self.kapasiteetti = self.alkioiden_lkm + self.kasvatuskoko
        uusi_jono = [0] * (self.kapasiteetti)
        self.kopioi_taulukko(self.ljono, uusi_jono)
        self.ljono = uusi_jono

    def poista(self, n):
        for i in range(0, self.alkioiden_lkm):
            if self.ljono[i] == n:

                uusi_jono = [0] * (self.kapasiteetti)
                self.kopioi_taulukko((self.ljono[:i] + self.ljono[i+1:]), uusi_jono)
                self.ljono = uusi_jono
                self.alkioiden_lkm -= 1
                
                return True
        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return list(self.ljono[0:self.alkioiden_lkm])

    @staticmethod
    def yhdiste(a, b):
        yhdistys = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, (len(a_taulu) + len(b_taulu))):
            if (i >= len(a_taulu)):
                yhdistys.lisaa(b_taulu[i-(len(a_taulu))])
            else:
                yhdistys.lisaa(a_taulu[i])

        return yhdistys

    @staticmethod
    def leikkaus(a, b):
        leikattu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if (a_taulu[i] == b_taulu[j]):
                    leikattu.lisaa(a_taulu[i])

        return leikattu

    @staticmethod
    def erotus(a, b):
        erotettu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotettu.lisaa(a_taulu[i])
            for j in range(0, len(b_taulu)):
                if (a_taulu[i] == b_taulu[j]):
                    erotettu.poista(b_taulu[j])

        return erotettu

    def __str__(self):
        tuotos = "{"
        for i in range(0, self.alkioiden_lkm):
            tuotos += str(self.ljono[i])
            if i != self.alkioiden_lkm - 1:
                tuotos += ", "
        tuotos += "}"
        return tuotos
