import magic

from checks.base import Checker
from problem import Problem, Severity
from util import walk_directory

class GnulibChecker(Checker):
    CULPRITS = [
        "text/x-m4",
        "text/x-makefile"
    ]

    IDENTIFIER = "# Generated by gnulib-tool." 

    def _check_file(self, file) -> bool:
        with open(file, "rb") as suspect:
            # this is ok even though we are in binary mode, as its encoding in all major encodings remains UTF-8 encoding
            return self.IDENTIFIER.encode("utf-8") in suspect.read()

    def execute(self, directory: str) -> Problem | None:
        problem = Problem(Severity.ERROR, "gnulib imported with gnulib-tool")

        files = walk_directory(directory)
        for file in files:
            mime = magic.from_file(file, mime=True)
            if mime in self.CULPRITS and self._check_file(file):
                return problem

        if self.deep:
            for file in files:
                if self._check_file(file):
                    return problem

        return None
