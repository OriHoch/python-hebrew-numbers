# python-hebrew-numbers
python library for conversion of hebrew numbers (Gematria)

## Usage

### installation
```bash
$ git clone --recurse-submodules https://github.com/OriHoch/python-hebrew-numbers.git
$ cd python-hebrew-numbers
$ pip install .
```

### gematria_to_int
```bash
>>> from hebrew_numbers import gematria_to_int
>>> gematria_to_int(u'רח"צ')
298
```

### int_to_gematria
```bash
>>> from hebrew_numbers import int_to_gematria
>>> gematria_to_int(298)
u'רח״צ'
>>> gematria_to_int(298, gershayim=False)
u'רחצ'
```

## Features
* conversion from string of letters to an integer number
* conversion of integer to string (using [hebrew-special-numbers](https://github.com/chaimleib/hebrew-special-numbers))

## Contributing
See the [contribution guide](CONTRIBUTING.md)

## Background
* see https://github.com/hasadna/Open-Knesset/issues/169
