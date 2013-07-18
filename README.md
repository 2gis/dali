# Dalí
Selenium-based tool for capturing and comparing screenshots.

### Requirements
```bash
$ apt-get install python-opencv python-numpy
$ pip install selenium
```

### Create custom bindings
Requires [Apache Thrift](http://thrift.apache.org/).
```bash
$ thrift -out bindings/py --gen py config/dali.thrift
```
