from problem import Problem
from util import get_mime

class Checker():
    def __init__(self, deep: bool):
        self.deep = deep

    def _is_text(self, file: str):
        return get_mime(file).startswith("text/")

    def _text_deep(self, file: str):
        return self.deep and self._is_text(file)

    def execute(self, path: str) -> Problem | None:
        raise Exception("Must be implemented")
