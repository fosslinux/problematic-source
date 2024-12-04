import os

from checks.mime import MimeChecker
from problem import Severity

class TestMimeChecker():
    checker = MimeChecker(deep=True)
    path = os.path.join("testdata", "mime")

    def test_ok(self):
        assert self.checker.execute(os.path.join(self.path, "ok")) == None

    def test_bad(self):
        problem = self.checker.execute(os.path.join(self.path, "bad"))
        assert problem != None
        assert problem.severity == Severity.ERROR

    def test_warn(self):
        problem = self.checker.execute(os.path.join(self.path, "warn"))
        assert problem != None
        assert problem.severity == Severity.WARN
