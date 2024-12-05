import os

from checks.autogen import AutogenChecker
from problem import Severity

class TestAutogenChecker():
    checker = AutogenChecker(deep=False)
    path = os.path.join("testdata", "autogen")

    def _bad(self, file: str):
        problem = self.checker.execute(os.path.join(self.path, file))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert "autogen" in problem.desc

    def _ok(self, file: str):
        assert self.checker.execute(os.path.join(self.path, file)) == None

    def test_bad1(self):
        self._bad("Makefile.in.in")

    def test_bad2(self):
        self._bad("bad.c")

    def test_good1(self):
        self._ok("innocent.c")

    def test_good2(self):
        self._ok("configure")
