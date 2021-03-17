from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovellus, lue_syote):
        self._lue_syote = lue_syote
        self._sovellus = sovellus
        self._edellinen = 0
    
    def suorita(self):
        arvo = self._lue_syote()
        self._edellinen = self._sovellus.tulos
        self._sovellus.plus(int(arvo)) 

    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen)

class Erotus:
    def __init__(self, sovellus, lue_syote):
        self._lue_syote = lue_syote
        self._sovellus = sovellus
        self._edellinen = 0

    def suorita(self):
        arvo = self._lue_syote()
        self._edellinen = self._sovellus.tulos
        self._sovellus.miinus(int(arvo))

    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen)

class Nollaus:
    def __init__(self, sovellus, lue_syote):
        self._lue_syote = lue_syote
        self._sovellus = sovellus
        self._edellinen = 0
    
    def suorita(self):
        self._edellinen = self._sovellus.tulos
        self._sovellus.nollaa()  

    def kumoa(self):
        self._sovellus.aseta_arvo(self._edellinen)

class Kumoa:
    def __init__(self, sovellus, hae_edellinen):
        self._sovellus = sovellus
        self._hae_edellinen = hae_edellinen
    
    def suorita(self):
        komento = self._hae_edellinen()
        komento.kumoa()

class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self._edellinen_komento = None
        
        self._komennot = {
            Komento.SUMMA: Summa(sovellus, self._lue_syote),
            Komento.EROTUS: Erotus(sovellus, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovellus, self._lue_syote),
            Komento.KUMOA: Kumoa(sovellus, self._hae_edellinen)
        }

    def _hae_edellinen(self):
        return self._edellinen_komento
    
    def _lue_syote(self):
        return self._syote_kentta.get()

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._edellinen_komento = komento_olio

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)
