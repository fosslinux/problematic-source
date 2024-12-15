import os

from checks.po4a import Po4aChecker
from checks.man import ManCheckerTester

class TestPo4aChecker(ManCheckerTester):
    checker = Po4aChecker(deep=False)
    path = os.path.join("testdata", "po4a")
    NAME = "po4a"
