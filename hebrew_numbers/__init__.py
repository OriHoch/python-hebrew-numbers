# -*- coding: utf-8 -*-
from os import path
import io
import yaml

PROJ_PATH = path.sep.join(__file__.split(path.sep)[:-2])
DATA_PATH = path.join(
    PROJ_PATH, 'hebrew-special-numbers-default.yml')
specialnumbers = yaml.safe_load(io.open(DATA_PATH, encoding='utf8'))


MAP_DICT = {u'א': [1, 1],
            u'ב': [2, 2],
            u'ג': [3, 3],
            u'ד': [4, 4],
            u'ה': [5, 5],
            u'ו': [6, 6],
            u'ז': [7, 7],
            u'ח': [8, 8],
            u'ט': [9, 9],
            u'י': [10, 1],
            u'כ': [20, 2],
            u'ל': [30, 3],
            u'מ': [40, 4],
            u'נ': [50, 5],
            u'ס': [60, 6],
            u'ע': [70, 7],
            u'פ': [80, 8],
            u'צ': [90, 9],
            u'ק': [100, 1],
            u'ר': [200, 2],
            u'ש': [300, 3],
            u'ת': [400, 4],
            u'ך': [20, 2],
            u'ם': [40, 4],
            u'ן': [50, 5],
            u'ף': [80, 8],
            u'ץ': [90, 9]}

GERESH = set(("'", '׳'))


def gematria_ktana_to_int(name):
    sum = 0
    for char in name:
        if char in ['"', "'"]:
            continue
        sum += MAP_DICT[char][1]
    sum = str(sum) 
    return int(sum[0]) + int(sum[1]) if len(sum) >= 2 else int(sum)


def gematria_to_int(string):
    res = 0
    for i, char in enumerate(string):
        if char in GERESH and i < len(string)-1:
            res *= 1000
        if char in MAP_DICT:
            res += MAP_DICT[char][0]
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
