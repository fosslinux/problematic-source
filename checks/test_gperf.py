import os

from checks.gperf import GperfChecker
from problem import Severity

class TestGperfChecker():
    checker = GperfChecker(deep=False)
    path = os.path.join("testdata", "gperf")

    def test_bad(self):
        problem = self.checker.execute(os.path.join(self.path, "a.h"))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert "gperf" in problem.desc

    def test_good(self):
        assert self.checker.execute(os.path.join(self.path, "b.h")) == None

    def test_good2(self):
        assert self.checker.execute(os.path.join(self.path, "nothing.txt")) == None

    def test_heuristic_c(self):
        problem = self.checker.execute(os.path.join(self.path, "c.c"))
        assert problem != None
        assert problem.severity == Severity.WARN

    def test_heuristic_h(self):
        problem = self.checker.execute(os.path.join(self.path, "c.h"))
        assert problem != None
        assert problem.severity == Severity.WARN
