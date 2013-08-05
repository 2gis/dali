# Dalí
Selenium-based tool for capturing and comparing screenshots.

### Requirements
```bash
$ apt-get install python-opencv python-numpy
$ pip install thrift==0.9.0 selenium==2.33.0
```

### Update python bindings
Requires [Apache Thrift](http://thrift.apache.org/).
```bash
$ thrift -out common/core/interface_implementation --gen py:new_style common/config/dali.thrift
```
