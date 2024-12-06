import os
import magic
import re

from checks.base import Checker
from problem import Problem, Severity

class Help2manChecker(Checker):
    def execute(self, file: str) -> Problem | None:
        if re.match(r".*\.[1-9]$", file) or self._text_deep(file):
            with open(file, "rb") as f:
                if b"generated by help2man" in f.read():
                    return Problem(Severity.ERROR, "file generated by help2man")
        return None
