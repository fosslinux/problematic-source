from problem import Problem

class Checker():
    def __init__(self, deep: bool):
        self.deep = deep

    def execute(self, path: str) -> Problem | None:
        raise Exception("Must be implemented")
