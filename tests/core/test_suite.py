import unittest

from tests.core.image_comparison import image_comparison_test
from tests.core.screenshot import screenshot_test
from tests.core.resize import resize_test
# import sys


def suite():
    return unittest.TestSuite((
        unittest.makeSuite(image_comparison_test.ImageComparisonTestCase),
        unittest.makeSuite(screenshot_test.ScreenshotTestCase),
        unittest.makeSuite(resize_test.ResizeTestCase)
    ))


def main():
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    #sys.exit(not result.wasSuccessful())


if __name__ == "__main__":
    main()