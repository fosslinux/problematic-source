import os

from checks.help2man import Help2manChecker
from checks.man import ManCheckerTester

class TestHelp2manChecker(ManCheckerTester):
    checker = Help2manChecker(deep=False)
    path = os.path.join("testdata", "help2man")
    NAME = "help2man"
