# Dalí
Selenium-based tool for capturing and comparing screenshots.

### Requirements
```bash
$ apt-get install python-opencv python-numpy
$ pip install thrift==0.9.0 selenium==2.33.0
```

### Update python interface_implementation
Requires [Apache Thrift](http://thrift.apache.org/).
```bash
$ thrift -out common/core/interface_implementation --gen py:new_style common/config/dali.thrift
```

### Build and use of python bindings
https://github.com/2gis/dali/tree/master/pybindings

### Directories explanation
+ common - common files with realization of thrift server, running core functions
    + config - thrift config for bindings generation
    + core - core functionality
+ pybindings - python bindings for dali
+ tests - all the tests
    + core - core tests
    + py_bindings - python bindings tests


### To create your own bindings on `language`
Requires [Apache Thrift](http://thrift.apache.org/).
```bash
$ thrift -out `language`bindings/ --gen `language`:new_style common/config/dali.thrift
```