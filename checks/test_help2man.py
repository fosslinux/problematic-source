import os

from checks.help2man import Help2manChecker
from problem import Severity

class TestHelp2manChecker():
    checker = Help2manChecker(deep=False)
    path = os.path.join("testdata", "help2man")

    def _ok(self, file: str):
        assert self.checker.execute(os.path.join(self.path, file)) == None

    def _bad(self, file: str):
        problem = self.checker.execute(os.path.join(self.path, file))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert "help2man" in problem.desc

    def test_bad1(self):
        self._bad("bad.1")

    def test_bad2(self):
        self._bad("bad.8")

    def test_good1(self):
        self._ok("good.3")

    def test_noop(self):
        self._ok("random.txt")
