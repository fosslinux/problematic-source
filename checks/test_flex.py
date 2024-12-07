import os

from checks.flex import FlexChecker
from problem import Severity

class TestFlexChecker():
    checker = FlexChecker(deep=False)
    path = os.path.join("testdata", "flex")

    def test_bad(self):
        problem = self.checker.execute(os.path.join(self.path, "a.c"))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert "flex" in problem.desc

    def test_good_c(self):
        assert self.checker.execute(os.path.join(self.path, "b.c")) == None

    def test_good(self):
        assert self.checker.execute(os.path.join(self.path, "nothing.txt")) == None

    def test_heuristic_l(self):
        problem = self.checker.execute(os.path.join(self.path, "d.c"))
        assert problem != None
        assert problem.severity == Severity.WARN

    def test_heuristic_lex_yy_c(self):
        problem = self.checker.execute(os.path.join(self.path, "lex.yy.c"))
        assert problem != None
        assert problem.severity == Severity.WARN

