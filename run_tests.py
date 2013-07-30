#! /usr/bin/env python
__author__ = 'i.pavlov'

from tests.config import Config
import subprocess
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

nc = subprocess.call(['nc', '-z', Config.server, '4444'])
if nc:
    exit(nc)

from tests.test_suite import main
main()