import magic

from problem import Problem

class Checker():
    def __init__(self, deep: bool):
        self.deep = deep

    def _is_text(self, file: str):
        return magic.from_file(file, mime=True).startswith("text/")

    def _text_deep(self, file: str):
        return self.deep and self._is_text(file)

    def execute(self, path: str) -> Problem | None:
        raise Exception("Must be implemented")
