import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        
    def test_lisays_liikaa_tavaraa(self):
    	self.varasto.lisaa_varastoon(12)
    	
    	self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
    	
    	
    def test_otetaan_liikaa_tavaraa(self):
    	self.varasto.lisaa_varastoon(5)
    	
    	saatu_maara = self.varasto.ota_varastosta(7)
    	
    	self.assertAlmostEqual(saatu_maara, 5)
    	
    def test_ottaminen_varasto_tyhjentyy(self):
    	self.varasto.lisaa_varastoon(5)
    	
    	self.varasto.ota_varastosta(7)
    	
    	self.assertAlmostEqual(self.varasto.saldo, 0)
    	
    def test_lisays_negatiivinen_maara(self):
    	self.varasto.lisaa_varastoon(4)
    	
    	self.varasto.lisaa_varastoon(-2)
    	
    	self.assertAlmostEqual(self.varasto.saldo, 4)
    	
    def test_ottaminen_negatiivinen_maara(self):
    	self.varasto.lisaa_varastoon(4)
    	
    	self.varasto.ota_varastosta(-5)
    	
    	self.assertAlmostEqual(self.varasto.saldo, 4)
   
    def test_tyhja_varasto(self):
    	varasto = Varasto(0)
    	
    	self.assertAlmostEqual(varasto.saldo, 0)
    	
    def test_lisays_lisaa_kun_saldo_on_taynna(self):
    	self.varasto.lisaa_varastoon(10)
    	
    	self.varasto.lisaa_varastoon(5)
    	
    	self.assertAlmostEqual(self.varasto.saldo, 10)

