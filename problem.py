import enum
import hashlib
import os
from util import Colors
from collections.abc import Callable

class Severity(enum.Enum):
    FATAL = 1
    ERROR = 2
    WARN = 3
    UNSUPPORTED = 4

class Problem():
    def __init__(self, severity: Severity, desc: str, filename: str, magic: int):
        self.severity = severity
        self.desc = desc
        self.file = filename
        self.explanation = None
        self._magic = magic

    @property
    def hash(self):
        return self.hash_filed(self.file)

    def hash_filed(self, file: str):
        return hashlib.md5((file + str(self._magic)).encode("utf-8")).hexdigest()

    def __eq__(self, other):
        if not isinstance(other, Problem):
            return NotImplemented
        return self.severity == other.severity and self.desc == other.desc
    
    def strip_prefix(self, directory: str):
        if self.file:
            self.file = os.path.relpath(self.file, start=directory)

    def match_report(self, report, replacer: Callable[[str], str] | None = None):
        for explanation in report:
            for problem in explanation["problems"]:
                file = self.file
                if replacer:
                    file = replacer(file)
                if problem["hash"] == self.hash_filed(file):
                    self.explanation = explanation
                    return

    def json(self):
        return {
            "file": self.file,
            "hash": self.hash,
            "message": self.desc,
            "severity": self.severity.name,
        }
    
    def _str_type(self, color: str, icon: str):
        return f"{color}{icon} {self.file}{": " if self.file else ""}{self.desc}{Colors.RESET}"

    def __str__(self):
        FATAL_COLOR = Colors.BRIGHT_RED
        ERROR_COLOR = Colors.RED
        WARN_COLOR = Colors.YELLOW
        UNSUPPORTED_COLOR = Colors.GRAY

        match self.severity:
            case Severity.FATAL:
                return self._str_type(FATAL_COLOR, "\u2620")
            case Severity.ERROR:
                return self._str_type(ERROR_COLOR, "\u2bbe")
            case Severity.WARN:
                return self._str_type(WARN_COLOR, "\u26a0")
            case Severity.UNSUPPORTED:
                return self._str_type(UNSUPPORTED_COLOR, "?")
