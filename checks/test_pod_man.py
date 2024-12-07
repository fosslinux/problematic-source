import os

from checks.pod_man import PodManChecker
from problem import Severity

class TestPodManChecker():
    checker = PodManChecker(deep=False)
    path = os.path.join("testdata", "pod_man")

    def _ok(self, file: str):
        assert self.checker.execute(os.path.join(self.path, file)) == None

    def _bad(self, file: str):
        problem = self.checker.execute(os.path.join(self.path, file))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert "Pod::Man" in problem.desc

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
