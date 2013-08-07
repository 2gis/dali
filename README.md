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


### To create bindings for language {lang}
Requires [Apache Thrift](http://thrift.apache.org/).
```bash
$ thrift -out {lang}_bindings/ --gen {lang} common/config/dali.thrift
```
