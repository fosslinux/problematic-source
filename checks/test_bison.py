import os

from checks.bison import BisonChecker
from problem import Severity

class TestBisonChecker():
    checker = BisonChecker(deep=False)
    path = os.path.join("testdata", "bison")

    def _bad(self, file: str):
        problem = self.checker.execute(os.path.join(self.path, file))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert "Bison" in problem.desc

    def _warn(self, file: str):
        problem = self.checker.execute(os.path.join(self.path, file))
        assert problem != None
        assert problem.severity == Severity.WARN

    def _good(self, file: str):
        assert self.checker.execute(os.path.join(self.path, file)) == None

    def test_bad_c(self):
        self._bad("a.c")

    def test_hidden_bad_c(self):
        self._bad("b")

    def test_good_c(self):
        self._good("c.c")

    def test_bad_h(self):
        self._bad("d.h")

    def test_good_h(self):
        self._good("e.h")

    def test_warn_h(self):
        self._warn("a.h")

    def test_warn_y_tab_c(self):
        self._warn("y.tab.c")

    def test_warn_y_tab_h(self):
        self._warn("y.tab.h")

    def test_warn_y_c(self):
        self._warn("f.c")

    def test_warn_y_h(self):
        self._warn("f.h")
