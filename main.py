import os
import shutil
import sys
import json
import survey

from problem import Problem, Severity
from util import walk_directory
from reporter import Reporter

from transform.compressed import CompressedTransformer
from transform.compressed_rename import CompressedRenameTransformer
from transform.extract import ExtractTransformer

DEEP = True

# Ordered list of transforms
_transforms = [
    CompressedRenameTransformer(),
    CompressedTransformer(),
    ExtractTransformer(),
]

from checks.autogen import AutogenChecker
from checks.autotools import AutotoolsChecker
from checks.bison import BisonChecker
from checks.docbook import DocbookChecker
from checks.flex import FlexChecker
from checks.gperf import GperfChecker
from checks.help2man import Help2manChecker
from checks.po4a import Po4aChecker
from checks.pod_man import PodManChecker
from checks.mime import MimeChecker
from checks.comments import CommentsChecker
from checks.gnulib import GnulibChecker
from checks.texi import TexiChecker

# List of checks
_file_checks = [
    AutogenChecker(DEEP),
    AutotoolsChecker(DEEP),
    BisonChecker(DEEP),
    DocbookChecker(DEEP),
    FlexChecker(DEEP),
    GperfChecker(DEEP),
    Help2manChecker(DEEP),
    Po4aChecker(DEEP),
    PodManChecker(DEEP),
    TexiChecker(DEEP),
    MimeChecker(DEEP),
    CommentsChecker(DEEP),
]
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
        if whitelisted(file):
            continue
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

def whitelisted(file: str) -> bool:
    PREFIXES = ["Changelog", "ChangeLog", "NEWS"]

    filename = os.path.basename(file)
    for prefix in PREFIXES:
        if filename.startswith(prefix):
            return True

    return False

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
    if transform_problems != {}:
        print("The following problems were encountered while transforming files to be checked:")
        for file, problems in transform_problems.items():
            for problem in problems:
                print(problem)
        print()
        print("This usually indicates a problem with problematic-source.")
        sys.exit(1)

    check_problems = checks(outdir)
    all_problems = []
    print("The follow possible problems were found:")
    for file, problems in check_problems.items():
        all_problems += problems
        for problem in problems:
            print(problem)

    reporter = Reporter(all_problems)
    reporter.repl()
    file = survey.routines.input("File to write report to: ")
    with open(file, "w") as f:
        f.write(json.dumps(reporter.json(), indent=4))

if __name__ == "__main__":
    main()
