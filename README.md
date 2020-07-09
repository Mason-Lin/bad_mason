# bad_mason [![Version][version-badge]][version-link] ![MIT License][license-badge]
A small sample to demo what python can do

`bad_mason` is a a small sample to demo what python can do

package


### Demo
```
CALL bad_mason -g
or
CALL python -m bad_mason -g

DEMO!! You have been hacked
=====5a8fWOxg/4=====
Also write a hacked file in .ssh
It could send it out to somewhere!!
b'<!doctype html><html'
```

### Usage

```
usage: bad_mason [-h] [-g]

optional arguments:
  -h, --help         show this help message and exit
  -g, --get          get some data like covid-19 (fake)

or as a Module:
  python -m bad_mason -g
```

### Install

```
$ pip install bad_mason
```

### what's in site-packages
```
    Directory: C:\Users\<user>\AppData\Local\Programs\Python\<pythonver>\Lib\site-packages\bad_mason

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---           7/10/2020  1:13 AM            374 __init__.py
-a---           7/10/2020  1:13 AM             30 __main__.py
-a---           7/10/2020  1:13 AM            552 covid19getter.py
-a---           7/10/2020  1:13 AM           1674 datahelper.zip
```

#### what else can we do?
- we could even change datahelper.zip to another name like `datahelper.dll` but it still can run by `python datahelper.dll`
- we could `echo datahelper.zip >> spam.txt` and `chmod +x spam.txt` then `./spam.txt`


### Pack it
```
python -m pip install setuptools
python -m pip install wheel
python -m zipfile -c datahelper.zip .\datahelper\__init__.py .\datahelper\__main__.py .\datahelper\datahelper.py
python setup.py sdist bdist_wheel
```


### Try to install locally
```
python -m pip install -U .\dist\bad_mason-1.0.1-py3-none-any.whl
```


### Upload to PyPI
```
python -m pip install twine
twine upload dist/bad_mason-1.0.1-py3-none-any.whl
```


### License

[MIT](https://github.com/Mason-Lin/bad_mason/blob/master/LICENSE)

[version-badge]:   https://img.shields.io/badge/version-1.0.1-brightgreen.svg
[version-link]:    https://pypi.python.org/pypi/bad_mason/
[license-badge]:   https://img.shields.io/github/license/Mason-Lin/bad_mason.svg
