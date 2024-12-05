import os

from checks.comments import CommentsChecker 
from problem import Severity

class TestCommentsChecker():
    checker = CommentsChecker(deep=True)
    path = os.path.join("testdata", "comments")

    def _bad(self, file: str):
        problem = self.checker.execute(os.path.join(self.path, file))
        assert problem != None
        assert problem.severity == Severity.WARN

    def _ok(self, file: str):
        assert self.checker.execute(os.path.join(self.path, file)) == None

    def test_bad1(self):
        self._bad("a.c")

    def test_bad2(self):
        self._bad("b.sh")

    def test_bad3(self):
        self._bad("e")

    def test_ok1(self):
        self._ok("c.c")

    def test_ok2(self):
        self._ok("d.txt")
