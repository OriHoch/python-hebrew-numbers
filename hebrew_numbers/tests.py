# -*- coding: utf-8 -*-

import unittest
from . import gematria_to_int, int_to_gematria, gematria_ktana_to_int


class TestGematriaToInt(unittest.TestCase):

    def test(self):
        for heb, num in (
            (u'א', 1),
            (u'ב', 2),
            (u'אב', 3),
            (u'קצ"ח', 198),
            (u'אאא', 3),
        ):
            self.assertEqual(gematria_to_int(heb), num)

    def test_thousands(self):
        self.assertEqual(gematria_to_int(u'ה\'תשע"ז'), 5777)


class TestIntToGematria(unittest.TestCase):

    def test_with_gershayim(self):
        for heb, num in (
            (u'ב׳', 2),
            (u'קצ״ח', 198),
            (u'רח״צ', 298),
            (u'ט״ז', 16),
        ):
            self.assertEqual(int_to_gematria(num), heb)

    def test_no_gershayim(self):
        for heb, num in (
            (u'ב', 2),
            (u'קצח', 198),
            (u'רחצ', 298),
            (u'טז', 16),
        ):
            self.assertEqual(int_to_gematria(num, gershayim=False), heb)

class TestGematriaKtanaToInt(unittest.TestCase):

    def test_gematria_ktana(self):
        for heb, num in (
            (u'בן', 7),
            (u'נעמה', 3),
            (u'תשמ"ץ', 2),
            (u"איצקוביץ'", 3)
        ):
            self.assertEqual(gematria_ktana_to_int(heb), num)

if __name__ == '__main__':
    unittest.main()
