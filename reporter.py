import os
import survey

from problem import Problem, Severity
from util import Colors

class Explanation():
    def __init__(self, message: str, color: str):
        self.message = message
        self._problems = []
        self._color = color

    def add_problems(self, problems: list[Problem]):
        self._problems += problems

    def json(self):
        return {
            "message": self.message,
            "problems": [x.json() for x in self._problems]
        }

    def __str__(self):
        filenames = sorted(list(set([x.file for x in self._problems])))
        filename_list = ", ".join([f"{Colors.BOLD}{Colors.YELLOW}{x}{Colors.RESET}" for x in filenames])
        return f"{self._color}{self.message}{Colors.RESET} ({filename_list})"

class Solution(Explanation):
    def __init__(self, message: str):
        super().__init__(message, Colors.GREEN)

    def json(self):
        json = super().json()
        json.update({"type": "solution"})
        return json

class Dismissal(Explanation):
    def __init__(self, message: str):
        super().__init__(message, Colors.MAGENTA)

    def json(self):
        json = super().json()
        json.update({"type": "dismissal"})
        return json

class Reporter():
    def __init__(self, problems: list[Problem]):
        self.problems = problems
        self._explanations = []

    def _help(self):
        print("The following commands are possible:")
        print("solve <message>: the problem is solved, one-line explanation of how it was solved.")
        print("dismiss <message>: the problem is invalid, one-line explanation of why it is invalid.")
        print("same: the problem is the same as a previous one.")
        print("cancel: go back to selection.")
        print("help: show this again")
        print("Press Enter to continue.")

    def _max_view(self, items: list[str]):
        size = os.get_terminal_size()
        max_rows = max([len(x) // size.columns + 1 for x in items])
        return size.lines // max_rows - 1

    def _select_problems(self) -> list[Problem]:
        indicies = survey.routines.basket("Which problems are you explaining?", options=map(str, self.problems), view_max=self._max_view(map(str, self.problems)))
        return [self.problems[i] for i in indicies]

    def repl(self):
        print("Our goal here is to fix all of these problems or dismiss them as invalid, and document.")
        self._help()
        input()
        while len(self.problems) > 0:
            problems = self._select_problems()
            done = False
            while not done:
                command = input("> ").strip()
                if command.startswith("solve "):
                    solution = Solution(command.removeprefix("solve "))
                    solution.add_problems(problems)
                    self._explanations.append(solution)
                    done = True
                elif command.startswith("dismiss "):
                    dismissal = Dismissal(command.removeprefix("dismiss "))
                    dismissal.add_problems(problems)
                    self._explanations.append(dismissal)
                    done = True
                elif command == "same":
                    if not self._same(problems):
                        break
                    done = True
                elif command == "cancel":
                    break
                elif command == "help":
                    self._help()
                else:
                    print("Invalid command")
                    self._help()
            if done:
                for problem in problems:
                    self.problems.remove(problem)

    def _same(self, problems: list[Problem]):
        choices = list(map(str, self._explanations)) + ["None"]
        index = survey.routines.select("Which explanation applies?", options=choices)

        if index == len(self._explanations):
            return False
        else:
            self._explanations[index].add_problems(problems)
            return True

    def json(self) -> str:
        return [x.json() for x in self._explanations]
