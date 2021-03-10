import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)

    print(joukko.to_int_list())

    joukko2 = IntJoukko(2,2)
    print(joukko2.kapasiteetti)
    joukko2.lisaa(2)
    joukko2.lisaa(1)
    print(joukko2.kapasiteetti)
    print(joukko2.lisaa(2))

    print(joukko2.kapasiteetti)
    print(joukko2.to_int_list())

    joukko2.lisaa(4)
    joukko2.lisaa(3)

    print(joukko2.to_int_list())
    print(joukko2.kapasiteetti)

    joukko2.poista(3)
    print(joukko2.to_int_list())


if __name__ == "__main__":
    main()
