# bad_mason [![Version][version-badge]][version-link] ![MIT License][license-badge]
A small sample to demo what python can do

`bad_mason` is a a small sample to demo what python can do


### Demo


### Usage

```
usage: bad_mason [-h] [-g]

optional arguments:
  -h, --help         show this help message and exit
  -g --get           get some data like covid-19 (fake)
```

### Install

```
$ pip install bad_mason
```


### Pack it
```
pip3 install setuptools
pip3 install wheel

python3 setup.py sdist bdist_wheel
```


### Try to install locally
```
pip3 install dist/bad_mason-<ver>-py3-none-any.whl
```


### Upload to PyPI
```
pip3 install twine
twine upload dist/bad_mason-<ver>-py3-none-any.whl
```


### License

[MIT](https://github.com/Mason-Lin/bad_mason/blob/master/LICENSE)

[version-badge]:   https://img.shields.io/badge/version-0.1.5-brightgreen.svg
[version-link]:    https://pypi.python.org/pypi/bad_mason/
[license-badge]:   https://img.shields.io/github/license/Mason-Lin/bad_mason.svg
