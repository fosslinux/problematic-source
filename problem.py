import enum
import hashlib
from util import Colors

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
        self.hash = hashlib.md5((filename + str(magic)).encode("utf-8")).hexdigest()

    def __eq__(self, other):
        if not isinstance(other, Problem):
            return NotImplemented
        return self.severity == other.severity and self.desc == other.desc

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
