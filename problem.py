import enum

class Severity(enum.Enum):
    FATAL = 1
    ERROR = 2
    WARN = 3
    UNSUPPORTED = 4

class Problem():
    def __init__(self, severity: Severity, desc: str):
        self.severity = severity
        self.desc = desc

    def __eq__(self, other):
        if not isinstance(other, Problem):
            return NotImplemented
        return self.severity == other.severity and self.desc == other.desc
    
    def _print_type(self, color: str, icon: str, file: str):
        RESET_COLOR = "\033[0m"
        print(f"{color}{icon} {file}: {self.desc}{RESET_COLOR}")

    def print(self, file: str):
        FATAL_COLOR = "\033[91m"
        ERROR_COLOR = "\033[41m"
        WARN_COLOR = "\033[33m"
        UNSUPPORTED_COLOR = "\033[90m"

        match self.severity:
            case Severity.FATAL:
                self._print_type(FATAL_COLOR, "\u2620", file)
            case Severity.ERROR:
                self._print_type(ERROR_COLOR, "\u274c", file)
            case Severity.WARN:
                self._print_type(WARN_COLOR, "\u26a0", file)
            case Severity.UNSUPPORTED:
                self._print_type(UNSUPPORTED_COLOR, "?", file)
