import os
import re

from checks.base import Checker
from problem import Problem, Severity

class PodManChecker(Checker):
    def execute(self, file: str) -> Problem | None:
        if re.match(r".*\.(?:[1-9]|man)$", file) or self._text_deep(file):
            with open(file, "rb") as f:
                if b"Automatically generated by Pod::Man" in f.read():
                    return Problem(Severity.ERROR, "file generated by Perl's Pod::Man")
        return None