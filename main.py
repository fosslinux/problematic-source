import os
import shutil
import sys

from problem import Problem, Severity
from util import walk_directory

from transform.compressed import CompressedTransformer
from transform.compressed_rename import CompressedRenameTransformer
from transform.extract import ExtractTransformer

DEEP = True

# Ordered list of transforms
_transforms = [CompressedRenameTransformer(), CompressedTransformer(), ExtractTransformer()]

from checks.mime import MimeChecker
from checks.gnulib import GnulibChecker
from checks.autotools import AutotoolsChecker

# List of checks
_file_checks = [MimeChecker(DEEP), AutotoolsChecker(DEEP)]
_global_checks = [GnulibChecker(DEEP)]

def transforms(directory: str) -> dict[str, list[Problem]]:
    # The first pass runs the first transform
    # This is repeated until it is a no-op
    # Then, the second pass runs the first two transforms
    # Repeated until it is a no-op, etc.
    problems = {}
    for i in range(len(_transforms)):
        action = True 
        while action:
            action = False
            for transform in _transforms[:i + 1]:
                for file in walk_directory(directory):
                    acted, problem = transform.execute(file)
                    if acted:
                        action = True
                    if problem:
                        if file not in problems:
                            problems[file] = [problem]
                        elif problem not in problems[file]:
                            problems[file].append(problem)
    return problems

def checks(directory: str) -> dict[str, list[Problem]]:
    problems = {}
    for file in walk_directory(directory):
        file_problems = []
        for check in _file_checks:
            problem = check.execute(file)
            if problem:
                file_problems.append(problem)
        if file_problems != []:
            problems[file] = file_problems

    for check in _global_checks:
        problem = check.execute(directory)
        if problem:
            if "" not in problems:
                problems[""] = [problem]
            else:
                problems[""].append(problem)

    return problems

def main():
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    for arg in sys.argv[2:]:
        dest = os.path.join(outdir, os.path.basename(arg))
        if os.path.isdir(arg):
            shutil.copytree(arg, dest)
        elif os.path.isfile(arg):
            shutil.copyfile(arg, dest)

    transform_problems = transforms(outdir)
    print("The following problems were encountered while transforming files to be checked:")
    for file, problems in transform_problems.items():
        for problem in problems:
            problem.print(file)
    print()

    print("The follow possible problems were found:")
    check_problems = checks(outdir)
    for file, problems in check_problems.items():
        for problem in problems:
            problem.print(file)

if __name__ == "__main__":
    main()
