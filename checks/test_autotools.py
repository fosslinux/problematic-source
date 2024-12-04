import os

from checks.autotools import AutotoolsChecker
from problem import Problem, Severity

class TestAutotoolsChecker():
    checker = AutotoolsChecker(deep=False)
    path = os.path.join("testdata", "autotools")

    def test_automake_bad(self):
        problem = self.checker.execute(os.path.join(self.path, "Makefile.bad.in"))
        assert problem.severity == Severity.ERROR
        assert "automake" in problem.desc

    def test_automake_good(self):
        assert self.checker.execute(os.path.join(self.path, "Makefile.in")) == None

    def test_autoconf_bad(self):
        problem = self.checker.execute(os.path.join(self.path, "configure"))
        assert problem.severity == Severity.ERROR
        assert "autoconf" in problem.desc

    def test_autoconf_good(self):
        assert self.checker.execute(os.path.join(self.path, "a", "configure")) == None

    def test_aclocal_bad(self):
        problem = self.checker.execute(os.path.join(self.path, "a", "aclocal.m4"))
        assert problem.severity == Severity.ERROR
        assert "aclocal" in problem.desc

    def test_aclocal_good(self):
        assert self.checker.execute(os.path.join(self.path, "aclocal.m4")) == None

    def test_autoheader(self):
        problem = self.checker.execute(os.path.join(self.path, "config.h.in"))
        assert problem.severity == Severity.WARN
        assert "autoheader" in problem.desc

    def test_ok(self):
        assert self.checker.execute(os.path.join(self.path, "allgood")) == None
