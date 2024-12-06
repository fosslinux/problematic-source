import os

from checks.texi import TexiChecker
from problem import Severity

class TestTexiChecker():
    checker = TexiChecker(deep=True)
    path = os.path.join("testdata", "texi")

    def test_bad_info(self):
        problem = self.checker.execute(os.path.join(self.path, "x.info"))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert "makeinfo" in problem.desc

    def test_bad_html(self):
        problem = self.checker.execute(os.path.join(self.path, "x.html"))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert "texi2html" in problem.desc

    def test_good_info(self):
        assert self.checker.execute(os.path.join(self.path, "y.info")) == None

    def test_good_html(self):
        assert self.checker.execute(os.path.join(self.path, "y.html")) == None

    def test_heuristic_pdf(self):
        problem = self.checker.execute(os.path.join(self.path, "x.pdf"))
        assert problem != None
        assert problem.severity == Severity.WARN

    def test_heuristic_dvi(self):
        problem = self.checker.execute(os.path.join(self.path, "x.dvi"))
        assert problem != None
        assert problem.severity == Severity.WARN

    def test_heuristic_info(self):
        problem = self.checker.execute(os.path.join(self.path, "z.info"))
        assert problem != None
        assert problem.severity == Severity.WARN

    def test_mime1(self):
        problem = self.checker.execute(os.path.join(self.path, "hidden"))
        assert problem != None
        assert problem.severity == Severity.WARN

    def test_mime2(self):
        problem = self.checker.execute(os.path.join(self.path, "imnothere"))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert "makeinfo" in problem.desc

    def test_normal(self):
        assert self.checker.execute(os.path.join(self.path, "normal.txt")) == None
