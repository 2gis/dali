#! /usr/bin/env python
__author__ = 'i.pavlov'

import subprocess
import os
import unittest

from tests.config import Config

os.environ['PYTHONPATH'] = os.path.dirname(os.path.abspath(__file__))

nc = subprocess.call(['nc', '-z', Config.server, Config.port])
if nc:
    exit(nc)

from tests.core import test_suite as core_test_suite
from tests.python_bindings import test_suite as python_bindings_test_suite

suite = unittest.TestSuite((
    core_test_suite.suite(),
    python_bindings_test_suite.suite()
))
unittest.TextTestRunner(verbosity=2).run(suite)



