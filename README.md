# python-hebrew-numbers

python library for conversion of hebrew numbers (Gematria)

## Usage

### installation

```bash
pip install python-hebrew-numbers
```

### gematria_to_int

```python
from hebrew_numbers import gematria_to_int
gematria_to_int(u'רח"צ')
# 298
```

### int_to_gematria

```python
from hebrew_numbers import int_to_gematria
int_to_gematria(298)
# u'רח״צ'
int_to_gematria(298, gershayim=False)
# u'רחצ'
```

### gematria_ktana_to_int

```python
from hebrew_numbers import gematria_ktana_to_int
gematria_ktana_to_int('נחמה')
# 4
```


## Features

* conversion from string of letters to an integer number
* conversion of integer to string (using [hebrew-special-numbers](https://github.com/chaimleib/hebrew-special-numbers))


## Contributing

See the [contribution guide](CONTRIBUTING.md)

## Background

* see https://github.com/hasadna/Open-Knesset/issues/169
