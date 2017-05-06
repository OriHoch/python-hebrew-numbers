# -*- coding: utf-8 -*-

MAP = (
    (1, u'א'),
    (2, u'ב'),
    (3, u'ג'),
    (4, u'ד'),
    (5, u'ה'),
    (6, u'ו'),
    (7, u'ז'),
    (8, u'ח'),
    (9, u'ט'),
    (10, u'י'),
    (20, u'כ'),
    (30, u'ל'),
    (40, u'מ'),
    (50, u'נ'),
    (60, u'ס'),
    (70, u'ע'),
    (80, u'פ'),
    (90, u'צ'),
    (100, u'ק'),
    (200, u'ר'),
    (300, u'ש'),
    (400, u'ת'),
    (500, u'ך'),
    (600, u'ם'),
    (700, u'ן'),
    (800, u'ף'),
    (900, u'ץ')
)
MAP_DICT = {k: v for v, k in MAP}


def gematria_to_int(string):
    res = 0
    for char in string:
        if char in MAP_DICT:
            res += MAP_DICT[char]
    return res
