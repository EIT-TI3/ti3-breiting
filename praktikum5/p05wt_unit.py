# (c) KJR

import unittest
import location
import koordinate
import math


class Prak02Unit(unittest.TestCase):
    def testAufgabe1(self):
        print("Test zu Aufgabe 1 (Klasse LocationAt)")
        la = location.LocationAt('test03WS18.csv')

        # Attribut entries
        entries = la._entries
        self.assertTrue(type(entries) == list)
        self.assertEqual(len(entries), 63)
        self.assertTupleEqual(entries[0], (74.0, -1284.0, 76.0, 16764.0))
        self.assertTupleEqual(entries[-1], (62252.0, -1384.0, 432.0, 16496.0))

        # Methode __str__()
        erg_str = str(la)
        """
        erg_soll = ("Eintraege\n  74.0: x:-1284.0 y:   76.0 z: 16764.0\n"
                    + "1077.0: x:-1276.0 y:  116.0 z: 16684.0\n"
                    + "2080.0: x:-980.0 y: 2288.0 z: 16824.0\n"
                    + "3083.0: x:-1492.0 y: 5300.0 z: 15864.0\n"
                    + "4086.0: x:-1780.0 y: 7176.0 z: 15100.0\n"
                    + "5089.0: x:-712.0 y: 9436.0 z: 13400.0\n"
                    + "6092.0: x:-832.0 y: 12480.0 z: 11368.0\n"
                    + "7094.0: x:-488.0 y: 13164.0 z: 10248.0\n"
                    + "8097.0: x:-1116.0 y: 11624.0 z: 11992.0\n"
                    + "9100.0: x:-1340.0 y: 9092.0 z: 13900.0\n"
                    + "10103.0: x:-1528.0 y: 4708.0 z: 16020.0\n"
                    + "11106.0: x:-1444.0 y: 2640.0 z: 16472.0\n"
                    + "12109.0: x:-1460.0 y:   16.0 z: 16652.0\n"
                    + "13112.0: x:-2100.0 y:  216.0 z: 16888.0\n"
                    + "14114.0: x:-1100.0 y:  568.0 z: 16680.0\n"
                    + "15117.0: x:-816.0 y: -2992.0 z: 16496.0\n"
                    + "16120.0: x:-824.0 y: -5720.0 z: 15792.0\n"
                    + "17123.0: x:-760.0 y: -9192.0 z: 13684.0\n"
                    + "18126.0: x:-912.0 y: -11908.0 z: 11628.0\n"
                    + "19129.0: x:-812.0 y: -13068.0 z: 10292.0\n"
                    + "20132.0: x:-744.0 y: -10900.0 z: 12028.0\n"
                    + "21134.0: x:-772.0 y: -7036.0 z: 14956.0\n"
                    + "22137.0: x:-984.0 y: -4084.0 z: 16040.0\n"
                    + "23140.0: x:-1068.0 y: -2288.0 z: 16396.0\n"
                    + "24143.0: x:-1184.0 y: -928.0 z: 16724.0\n"
                    + "25146.0: x:-1172.0 y: -364.0 z: 16704.0\n"
                    + "26149.0: x:-2212.0 y:  -20.0 z: 16664.0\n"
                    + "27152.0: x:-5372.0 y: -152.0 z: 15852.0\n"
                    + "28154.0: x:-7832.0 y:   32.0 z: 14636.0\n"
                    + "29157.0: x:-10068.0 y:  -88.0 z: 13288.0\n"
                    + "30160.0: x:-12436.0 y:  -88.0 z: 11248.0\n"
                    + "31163.0: x:-11972.0 y:  -64.0 z: 11408.0\n"
                    + "32166.0: x:-7960.0 y: -152.0 z: 14696.0\n"
                    + "33169.0: x:-3064.0 y:  -84.0 z: 16408.0\n"
                    + "34172.0: x:-1104.0 y:  264.0 z: 16760.0\n"
                    + "35174.0: x:1868.0 y:  536.0 z: 16884.0\n"
                    + "36177.0: x:5724.0 y:  712.0 z: 15756.0\n"
                    + "37180.0: x:8396.0 y: 1000.0 z: 14452.0\n"
                    + "38183.0: x:10372.0 y: 1188.0 z: 13132.0\n"
                    + "39186.0: x:12088.0 y:  856.0 z: 11604.0\n"
                    + "40189.0: x:12060.0 y:  936.0 z: 11500.0\n"
                    + "41192.0: x:7440.0 y:  576.0 z: 15068.0\n"
                    + "42194.0: x:3720.0 y:   48.0 z: 16300.0\n"
                    + "43197.0: x:-1032.0 y:  -16.0 z: 16840.0\n"
                    + "44200.0: x:-1188.0 y:   44.0 z: 16744.0\n"
                    + "45203.0: x:-480.0 y: -124.0 z: 16540.0\n"
                    + "46206.0: x:-2176.0 y:  508.0 z: 16364.0\n"
                    + "47209.0: x:-1912.0 y: -2152.0 z: 16928.0\n"
                    + "48212.0: x:-4752.0 y: -5912.0 z: 15212.0\n"
                    + "49214.0: x:-10144.0 y: -5224.0 z: 12144.0\n"
                    + "50217.0: x:-12004.0 y: -2912.0 z: 10888.0\n"
                    + "51220.0: x:-11328.0 y:  628.0 z: 12236.0\n"
                    + "52223.0: x:-8332.0 y: 3188.0 z: 14420.0\n"
                    + "53226.0: x:-4252.0 y: 3708.0 z: 15748.0\n"
                    + "54229.0: x: 536.0 y: 4012.0 z: 16032.0\n"
                    + "55231.0: x:4716.0 y: 1700.0 z: 15948.0\n"
                    + "56234.0: x:8220.0 y: -1864.0 z: 14528.0\n"
                    + "57237.0: x:6252.0 y: -5672.0 z: 14576.0\n"
                    + "58240.0: x:2420.0 y: -6120.0 z: 15264.0\n"
                    + "59243.0: x:-596.0 y: -4840.0 z: 16244.0\n"
                    + "60246.0: x:-1632.0 y: -808.0 z: 16412.0\n"
                    + "61249.0: x:-1660.0 y: -324.0 z: 16964.0\n"
                    + "62252.0: x:-1384.0 y:  432.0 z: 16496.0\n" )
        """
        erg_first2_lines = erg_str[0:48]
        erg_last_line = erg_str[-1:-40:-1]
        self.assertTrue(self, "Eintraege\n" in erg_first2_lines)
        self.assertTrue(self, "74.0:" in erg_first2_lines)
        self.assertTrue(self, "x:" in erg_first2_lines)
        self.assertTrue(self, "-1284.0:" in erg_first2_lines)
        self.assertTrue(self, "y:" in erg_first2_lines)
        self.assertTrue(self, "76.0" in erg_first2_lines)
        self.assertTrue(self, "z:" in erg_first2_lines)
        self.assertTrue(self, "16764.0\n" in erg_first2_lines)

        self.assertTrue(self, "62252.0:" in erg_last_line)
        self.assertTrue(self, "x:" in erg_last_line)
        self.assertTrue(self, "-1384.0" in erg_last_line)
        self.assertTrue(self, "y:" in erg_last_line)
        self.assertTrue(self, "432.0" in erg_last_line)
        self.assertTrue(self, "z:" in erg_last_line)
        self.assertTrue(self, "16496.0\n" in erg_last_line)

        # Methode last_stimestamp()
        last_t = la.last_timestamp()
        self.assertEqual(last_t, 62252.0)

        # Methode search_entry()
        entry = la._LocationAt__search_entry(74.0-20.0)
        self.assertTupleEqual(entry, (0.0, 0.0, 0.0))
        entry = la._LocationAt__search_entry(62252.0 + 20.0)
        self.assertIsNone(entry)
        entry = la._LocationAt__search_entry(4100)
        self.assertTupleEqual(entry, (-1780.0, 7176.0, 15100.0))

        # Methode get_roll()
        print(la._LocationAt__search_entry(9100.0))
        rot_y = la.get_roll(9100.0)
        self.assertAlmostEqual(abs(rot_y), 0.09610589145044778)

        # Methode get_nick()
        rot_x = la.get_nick(9100.0)
        self.assertAlmostEqual(abs(rot_x), 0.5771356841985327)

    def testAufgabe21(self):
        print("Test zu Aufgabe 2.1 (Klasse Koord2D)")
        k1_2d = koordinate.Koord2D(1.23, 4.56)

        # Test der privaten Attribute
        self.assertEqual(k1_2d._Koord2D__x, 1.23)
        self.assertEqual(k1_2d._Koord2D__y, 4.56)

        # Test der Properties
        self.assertEqual(k1_2d.x, 1.23)
        self.assertEqual(k1_2d.y, 4.56)

        # Test von __str__()
        erg_str = str(k1_2d)
        self.assertEqual(erg_str, "(1.23;4.56)")

    def testAufgabe22(self):
        print("Test zu Aufgabe 2.2 (Klasse Koord3D)")
        k1_3d = koordinate.Koord3D(3, 4, -1.5)

        # Test der Vererbung
        k1_3d_class = type(k1_3d)
        self.assertTrue(koordinate.Koord2D in k1_3d_class.__bases__)

        # Test der Attribute
        self.assertEqual(k1_3d._Koord3D__z, -1.5)
        # koord3d_attribute = k1_3d_class.__dict__.keys()
        # wegen Property nicht erfuellt
        # self.assertFalse("z" in koord3d_attribute)

        # Test der Property
        self.assertEqual(k1_3d.z, -1.5)

        # Test der __str__() Methode
        erg_str = str(k1_3d)
        self.assertEqual(erg_str, "(3.00;4.00;-1.50)")

        # Test rotate_z()
        k2_3d = k1_3d.rotate_z(math.pi/2)
        self.assertAlmostEqual(k2_3d.x, -4.00)
        self.assertAlmostEqual(k2_3d.y, 3.00)
        self.assertAlmostEqual(k2_3d.z, -1.50)

        # Test rotate_x()
        k3_3d = k1_3d.rotate_x(math.pi/2)
        self.assertAlmostEqual(k3_3d.x, 3.00)
        self.assertAlmostEqual(k3_3d.y, 1.50)
        self.assertAlmostEqual(k3_3d.z, 4.00)

    def testAufgabe23(self):
        print("Test zu Aufgabe 2.3 (Klasse Kabinett)")

        # Test der Vererbung
        k0_kabinett = koordinate.Kabinett(1.2, 3.4, 5.6)
        k0_kabinett_class = type(k0_kabinett)
        self.assertTrue(koordinate.Koord2D in k0_kabinett_class.__bases__)
        self.assertTrue(koordinate.Koord3D not in k0_kabinett_class.__bases__)

        # Test der Klassen-Variablen
        self.assertEqual(koordinate.Kabinett._Kabinett__Zscale, 0.5)
        self.assertAlmostEqual(koordinate.Kabinett._Kabinett__Angle, math.pi/4)

        # Test der Attribute
        self.assertEqual(k0_kabinett._Koord2D__x, 1.2)
        self.assertEqual(k0_kabinett._Koord2D__y, 3.4)
        self.assertEqual(k0_kabinett._Kabinett__z, 5.6)

        # Test der __str__() Methode
        erg_str = str(k0_kabinett)
        self.assertEqual(erg_str, "(-0.78;1.42)")

        # Test der Default-Parameter im Konstruktor
        k0_kabinett = koordinate.Kabinett(1.2)
        self.assertEqual(k0_kabinett._Koord2D__x, 1.2)
        self.assertEqual(k0_kabinett._Koord2D__y, 0.0)
        self.assertEqual(k0_kabinett._Kabinett__z, 0.0)
        erg_str = str(k0_kabinett)
        self.assertEqual(erg_str, "(1.20;0.00)")

        # Test Konstruktor mit Koord2D Objekt
        k1_2d = koordinate.Koord2D(3, 4)
        k1_kabinett = koordinate.Kabinett(k1_2d)
        self.assertEqual(k1_kabinett._Koord2D__x, 3.0)
        self.assertEqual(k1_kabinett._Koord2D__y, 4.0)
        self.assertEqual(k1_kabinett._Kabinett__z, 0.0)
        erg_str = str(k1_kabinett)
        self.assertEqual(erg_str, "(3.00;4.00)")

        # Test Konstruktor mit Koord3D Objekt
        k2_3d = koordinate.Koord3D(3, 5, 1)
        k2_kabinett = koordinate.Kabinett(k2_3d)
        self.assertEqual(k2_kabinett._Koord2D__x, 3.0)
        self.assertEqual(k2_kabinett._Koord2D__y, 5.0)
        self.assertEqual(k2_kabinett._Kabinett__z, 1.0)
        erg_str = str(k2_kabinett)
        self.assertEqual(erg_str, "(2.65;4.65)")

        # Test Konstruktor mit Kabinett-Objekt
        k3_kabinett = koordinate.Kabinett(k2_kabinett)
        self.assertAlmostEqual(k3_kabinett._Koord2D__x, 2.646446609406726)
        self.assertAlmostEqual(k3_kabinett._Koord2D__y, 4.646446609406726)
        self.assertEqual(k3_kabinett._Kabinett__z, 0.0)
        erg_str = str(k3_kabinett)
        self.assertEqual(erg_str, "(2.65;4.65)")

        # Test Konstruktor mit Koord2D-Objekt puls Wert fuer z
        k4_kabinett = koordinate.Kabinett(k1_2d, z_=1.5)
        self.assertEqual(k4_kabinett._Koord2D__x, 3.0)
        self.assertEqual(k4_kabinett._Koord2D__y, 4.0)
        self.assertEqual(k4_kabinett._Kabinett__z, 1.5)
        erg_str = str(k4_kabinett)
        self.assertEqual(erg_str, "(2.47;3.47)")


if __name__ == "__main__":
    unittest.main()
