import os

from checks.gnulib import GnulibChecker
from problem import Severity

class TestGnulibChecker():
    checker = GnulibChecker(deep=True)
    path = os.path.join("testdata", "gnulib")

    def test_bad(self):
        problem = self.checker.execute(os.path.join(self.path, "bad"))
        assert problem != None
        assert problem.severity == Severity.ERROR

    def test_bad_deep(self):
        problem = self.checker.execute(os.path.join(self.path, "bad_deep"))
        assert problem != None
        assert problem.severity == Severity.ERROR

    def test_ok(self):
        assert self.checker.execute(os.path.join(self.path, "ok")) == None
