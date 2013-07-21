# Dalí
Selenium-based tool for capturing and comparing screenshots.

### Requirements
```bash
$ apt-get install python-opencv python-numpy
$ pip install thrift==0.9.0 selenium==2.33.0
```

### Create custom bindings
Requires [Apache Thrift](http://thrift.apache.org/).
```bash
$ thrift -out bindings/py --gen py config/dali.thrift
```
