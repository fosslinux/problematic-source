import enum

class Severity(enum.Enum):
    FATAL = enum.auto
    ERROR = enum.auto
    WARN = enum.auto
    UNSUPPORTED = enum.auto

class Problem():
    def __init__(self, severity: Severity, desc: str):
        self.severity = severity
        self.desc = desc
