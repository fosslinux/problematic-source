import os
import magic
import re

from checks.base import Checker
from problem import Problem, Severity
from util import get_mime

class ManChecker(Checker):
    def execute(self, file: str) -> Problem | None:
        if get_mime(file) == "text/troff" or re.match(r".*\.(?:[1-9]|man)$", file) or self._text_deep(file):
            with open(file, "rb") as f:
                if self.MATCH in f.read():
                    return Problem(Severity.ERROR, self.ERROR, file, self.MAGIC)
        return None

class ManCheckerTester():
    def _ok(self, file: str):
        assert self.checker.execute(os.path.join(self.path, file)) == None

    def _bad(self, file: str):
        problem = self.checker.execute(os.path.join(self.path, file))
        assert problem != None
        assert problem.severity == Severity.ERROR
        assert self.NAME in problem.desc

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
