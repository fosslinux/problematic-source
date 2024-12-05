import os
import magic

from checks.base import Checker
from problem import Problem, Severity

class AutotoolsChecker(Checker):
    def _check_string(self, file: str, match: str) -> bool:
        with open(file, "rb") as suspect:
            return match.encode("utf-8") in suspect.read()

    def execute(self, file: str) -> Problem | None:
        basename = os.path.basename(file)
        dodeep = self.deep and magic.from_file(file, mime=True).startswith("text/")
        if basename.startswith("Makefile") or dodeep:
            if self._check_string(file, "generated by automake"):
                return Problem(Severity.ERROR, "file generated by automake")
        if basename == "configure" or dodeep:
            if self._check_string(file, "Generated by GNU Autoconf"):
                return Problem(Severity.ERROR, "file generated by autoconf")
        if basename == "aclocal.m4" or dodeep:
            if self._check_string(file, "generated automatically by aclocal"):
                return Problem(Severity.ERROR, "file generated by aclocal")
        if basename == "config.h.in":
            return Problem(Severity.WARN, "file probably generated by autoheader")
        return None
