# Dalí
Selenium-based tool for capturing and comparing screenshots.

### Requirements
```bash
$ apt-get install python-opencv python-numpy
$ pip install thrift==0.9.0 selenium==2.34.0
```

### Update python interface_implementation
Requires [Apache Thrift](http://thrift.apache.org/)
```bash
$ thrift -out common/core/interface_implementation --gen py:new_style common/config/dali.thrift
```

### Build and use of python bindings
https://github.com/2gis/dali/tree/master/py_bindings

### Directories explanation
+ common - common files with realization of thrift server, running core functions
    + config - thrift config for bindings generation
    + core - core functionality
+ py_bindings - python bindings for dali
+ tests - all the tests
    + core - core tests
    + py_bindings - python bindings tests


### Create bindings
Requires [Apache Thrift](http://thrift.apache.org/)

To update python (core) binding just run:
```bash
$ thrift -out common/core/interface_implementation/ --gen py common/config/dali.thrift
```

To create custom bindings you should execute the following command:
```bash
$ thrift -out {lang_code}_bindings/ --gen {lang_code} common/config/dali.thrift
```

where `{lang_code}` from table:

| lang_code | lang |
|------|-----------|
| csharp | C# |
| go | Go |
| java | Java |
| js | Javascript |
| perl | Perl |
| php | PHP |
| rb | Ruby |

For getting more information about supported languages just run:
```bash
$ thrift -help
```
