import os
import magic
import functools

class Colors():
    RESET = "\033[0m"
    BRIGHT_RED = "\033[91m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    GRAY = "\033[90m"
    BOLD = "\033[1m"
    GREEN = "\033[32m"
    MAGENTA = "\033[35m"

def walk_directory(path: str, exclusions: list[str]=[]):
    all_files = []
    for (root, _, files) in os.walk(path):
        for file in files:
            relpath = os.path.join(root, file)
            ok = True
            for exclusion in exclusions:
                if relpath.endswith(exclusion):
                    ok = False
                    break
            if ok:
                all_files.append(relpath)
    return all_files

@functools.cache
def get_mime(file: str) -> str:
    return magic.from_file(file, mime=True)
