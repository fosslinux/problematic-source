import magic
import os

from checks.base import Checker
from problem import Problem, Severity

class BisonChecker(Checker):
    MAGIC = 0xB130

    def _test_c(self, file: str) -> Problem | None:
        with open(file, "rb") as f:
            if b"A Bison parser, made from" in f.read():
                return Problem(Severity.ERROR, "generated by Bison", file, self.MAGIC)

    def _test_h(self, file: str) -> Problem | None:
        with open(file, "rb") as f:
            if b"#ifndef BISON_" in f.read():
                return Problem(Severity.ERROR, "generated by Bison", file, self.MAGIC)

    def execute(self, file: str) -> Problem | None:
        mime = magic.from_file(file, mime=True)
        
        # Explicit checks
        if file.endswith(".c") or mime == "text/x-c" or self._text_deep(file):
            problem = self._test_c(file)
            if problem:
                return problem

        if file.endswith(".h") or self._text_deep(file):
            problem = self._test_h(file)
            if problem:
                return problem
            else:
                c_file = file.removesuffix(".h") + ".c"
                if os.path.isfile(c_file) and self._test_c(c_file):
                    return Problem(Severity.WARN, "corresponding file {c_file} is Bison-generated", file, self.MAGIC)

        basename = os.path.basename(file)
        if basename == "y.tab.c" or basename == "y.tab.h":
            return Problem(Severity.WARN, "common name for Bison generated files", file, self.MAGIC)

        extension = None
        if file.endswith(".c"):
            extension = ".c"
        elif file.endswith(".h"):
            extension = ".h"
        if extension and (bison := os.path.isfile(file.removesuffix(extension) + ".y")):
            return Problem(Severity.WARN, f"may be generated from {bison} using bison", file, self.MAGIC)
