import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        self.varasto_mock = Mock()

        
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 24
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "kalja", 10)
            if tuote_id == 3:
                return Tuote(3, "leipä", 3)
                
        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_parametreilla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("meri", "12")

        self.pankki_mock.tilisiirto.assert_called_with("meri", 2, "12", ANY, 5)

    def test_kahden_eri_tuotteen_ostaminen_onnistuu(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("meri", "134")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)
        self.pankki_mock.tilisiirto.assert_called_with("meri", 2, "134", ANY, 15)

    def test_kahden_saman_tuotteen_ostaminen_onnistuu(self):

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("jokumuu", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("jokumuu", ANY, "54321", ANY, 20)

    def test_loppunutta_tuotetta_ei_veloiteta(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("jokumuu", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("jokumuu", ANY, "54321", ANY, 10)

    def test_korista_voi_poistaa_tuotteen_ja_varaston_saldo_kasvaa(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)

        self.varasto_mock.ota_varastosta.assert_called()

        self.kauppa.poista_korista(1)
        self.varasto_mock.palauta_varastoon.assert_called()


