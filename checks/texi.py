import os

from checks.base import Checker
from problem import Problem, Severity
from util import get_mime

class TexiChecker(Checker):
    MAGIC = 0x7E81

    def _noop(self, file: str) -> None:
        return None

    def _info(self, file: str) -> Problem | None:
        with open(file, "rb") as f:
            if b"produced by makeinfo" in f.read():
                return Problem(Severity.ERROR, "generated by makeinfo", file, self.MAGIC)
        return None

    def _html(self, file: str) -> Problem | None:
        with open(file, "rb") as f:
            data = f.read()
            if b"Created " in data and b"by texi2html" in data:
                return Problem(Severity.ERROR, "generated by texi2html", file, self.MAGIC)
        return None

    EXTENSIONS = {
        ".dvi": ("application/x-dvi", _noop),
        ".info": (None, _info),
        ".pdf": ("application/pdf", _noop),
        ".html": ("text/html", _html)
    }

    def execute(self, file: str) -> Problem | None:
        for extension, val in self.EXTENSIONS.items():
            mime, checker = val
            if file.endswith(extension) or (mime and get_mime(file) == mime):
                problem = checker(self, file)
                if problem:
                    return problem
                if file.endswith(extension):
                    texi = file.removesuffix(extension) + ".texi"
                    if os.path.isfile(texi):
                        return Problem(Severity.WARN, f"likely generated from {texi}", file, self.MAGIC)
                elif not file.endswith(".texi"):
                    for check in os.listdir(os.path.dirname(file)):
                        if check.endswith(".texi"):
                            return Problem(Severity.WARN, f"may be generated from {check}", file, self.MAGIC)

        if self.deep:
            for _, checker in self.EXTENSIONS.values():
                problem = checker(self, file)
                if problem:
                    return problem

        return None
