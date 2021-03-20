# (c) KJR/WT

import p01BreitingYannic as p01
import unittest


class Prak01Unit(unittest.TestCase):
    def testAufgabe1(self):
        if p01.text[0][:4]=='FEST':
            print("\nSchiller-Test zu Aufgabe 1")
            self.assertEqual(p01.zwischencode, "NRNEHEUDAS")
            self.assertEqual(p01.code_wort, "REEDS")
        else:
            print("\nTest zu Aufgabe 1")
            self.assertEqual(p01.zwischencode, "DASPOFTERL")
            self.assertEqual(p01.code_wort, "APFEL")

    def testAufgabe2(self):
        print("\nTest zu Aufgabe 2")
        self.assertEqual(p01.botschaft1, "RTFVQXSSE")
        self.assertEqual(p01.code1, "X")
        self.assertEqual(p01.botschaft_val1,
                         [17, 19, 5, 21, 16, 23, 18, 18, 4])
        self.assertEqual(p01.result_val1, [6, 4, 18, 2, 7, 0, 5, 5, 19])
        self.assertEqual(p01.result1, "GESCHAFFT")

    def testAufgabe3(self):
        if p01.text[0][:4]=='FEST':
            print("\nSchiller-Test zu Aufgabe 3")
            self.assertEqual(p01.botschaft, "SEW^Y[ELMBPEQBV")
            self.assertEqual(p01.code_wort, "REEDS")
            self.assertEqual(p01.botschaft_val, [18, 4, 22, 29, 24, 26, 4, 11, 12, 1, 15, 4, 16, 1, 21])
            self.assertEqual(p01.result_val,
                             [3, 0, 18, 30, 10, 11, 0, 15, 15, 19, 30, 0, 20, 2, 7])
            self.assertEqual(p01.result, "DAS_KLAPPT_AUCH")
        else:
            print("\nTest zu Aufgabe 3")
            self.assertEqual(p01.botschaft, "SLCVZCILAG")
            self.assertEqual(p01.code_wort, "APFEL")
            self.assertEqual(p01.botschaft_val,
                             [18, 11, 2, 21, 25, 2, 8, 11, 0, 6])
            self.assertEqual(p01.result_val, [18, 4, 7, 17, 18, 2, 7, 14, 4, 13])
            self.assertEqual(p01.result, "SEHRSCHOEN")


if __name__ == "__main__":
    unittest.main()
