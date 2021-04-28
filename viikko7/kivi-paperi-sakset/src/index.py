from kps import KPS
from kps_tehdas import luo_peli


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            Kps = KPS()
            luo_peli("PelaajaVSPelaaja")
        elif vastaus.endswith("b"):
            Kps = KPS()
            luo_peli("Tekoaly")
        elif vastaus.endswith("c"):
            Kps = KPS()
            luo_peli("ParannettuTekoaly")
        else:
            break



if __name__ == "__main__":
    main()
