import os

from checks.help2man import Help2manChecker
from checks.man import ManCheckerTester

class TestHelp2manChecker(ManCheckerTester):
    checker = Help2manChecker(deep=False)
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdata", "help2man")
    NAME = "help2man"
