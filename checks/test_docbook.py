import os

from checks.docbook import DocbookChecker
from problem import Severity

class TestDocbookChecker():
    checker = DocbookChecker(deep=False)
    path = os.path.join("testdata", "docbook")

    def _ok(self, file: str):
        assert self.checker.execute(os.path.join(self.path, file)) == None

    def _bad(self, file: str):
        problem = self.checker.execute(os.path.join(self.path, file))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert "DocBook" in problem.desc

    def test_bad1(self):
        self._bad("bad.1")

    def test_bad2(self):
        self._bad("bad.8")

    def test_bad3(self):
        self._bad("bad.man")

    def test_good1(self):
        self._ok("good.3")

    def test_noop(self):
        self._ok("random.txt")
