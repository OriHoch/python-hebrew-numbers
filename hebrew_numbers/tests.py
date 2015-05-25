# -*- coding: utf-8 -*-

import unittest
from . import gematria_to_int


class Test(unittest.TestCase):

    def test(self):
        for heb, num in (
            (u'א', 1),
            (u'ב', 2),
            (u'אב', 3),
            (u'קצ"ח', 198),
            (u'אאא', 3),
        ):
            self.assertEqual(gematria_to_int(heb), num)


if __name__ == '__main__':
    unittest.main()
