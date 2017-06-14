# -*- coding: utf-8 -*-
import yaml
from os import path
import io

PROJ_PATH = path.sep.join(__file__.split(path.sep)[:-2])
DATA_PATH = path.join(PROJ_PATH, 'hebrew-special-numbers', 'styles', 'default.yml')
specialnumbers = yaml.safe_load(io.open(DATA_PATH, encoding='utf8'))


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
MAP_DICT = dict([(k, v) for v, k in MAP])
GERESH = set(("'", '׳'))


def gematria_to_int(string):
    res = 0
    for i, char in enumerate(string):
        if char in GERESH and i < len(string)-1:
            res *= 1000
        if char in MAP_DICT:
            res += MAP_DICT[char]
    return res


# adapted from hebrew-special-numbers documentation
def int_to_gematria(num, gershayim=True):
    """convert integers between 1 an 999 to Hebrew numerals.

           - set gershayim flag to False to ommit gershayim
    """
    # 1. Lookup in specials
    if num in specialnumbers['specials']:
        retval = specialnumbers['specials'][num]
        return _add_gershayim(retval) if gershayim else retval

    # 2. Generate numeral normally
    parts = []
    rest = str(num)
    while rest:
        digit = int(rest[0])
        rest = rest[1:]
        if digit == 0:
            continue
        power = 10 ** len(rest)
        parts.append(specialnumbers['numerals'][power * digit])
    retval = ''.join(parts)
    # 3. Add gershayim
    return _add_gershayim(retval) if gershayim else retval


def _add_gershayim(s):
    if len(s) == 1:
        s += specialnumbers['separators']['geresh']
    else:
        s = ''.join([
            s[:-1],
            specialnumbers['separators']['gershayim'],
            s[-1:]
        ])
    return s
