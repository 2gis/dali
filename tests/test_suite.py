__author__ = 'i.pavlov'

import unittest

from tests.image_comparison import image_comparison_test
from tests.screenshot import screenshot_test
import sys


def suite():
    return unittest.TestSuite((
        unittest.makeSuite(image_comparison_test.ImageComparisonTestCase),
        unittest.makeSuite(screenshot_test.ScreenshotTestCase),
    ))


def main():
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    sys.exit(not result.wasSuccessful())


if __name__ == "__main__":
    main()