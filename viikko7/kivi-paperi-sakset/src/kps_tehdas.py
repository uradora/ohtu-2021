from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps import KPS

def luo_peli(peli):
    if peli == "PelaajaVSPelaaja":
        peli = KPSPelaajaVsPelaaja()
    elif peli == "Tekoaly":
        peli = KPSTekoaly()
    else:
        peli = KPSParempiTekoaly()
    print(
        "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
    )
    peli.pelaa()