import bz2
import gzip
import lzma
import magic
import os
import shutil
import zstandard
from typing import Callable

from util import walk_directory
from problem import Problem, Severity 

class CompressedTransformer():
    def _execute_type(self, file: str, opener: Callable, extension: str, name: str) -> [Problem | None]:
        extension = f".{extension}"
        if file.endswith(extension):
            outfile = file.removesuffix(extension)
            try:
                with opener(file, "rb") as f_in:
                    with open(outfile, "wb") as f_out:
                        shutil.copyfileobj(f_in, f_out)
                os.remove(file)
            except (OSError, EOFError) as e:
                try:
                    os.remove(outfile)
                except FileNotFoundError:
                    pass
                return Problem(Severity.FATAL, f"Unable to parse {name}: {e}")
        else:
            return Problem(Severity.UNSUPPORTED, f"Unknown extension {extension} for {name} file")
        return None

    def execute(self, file: str) -> tuple[bool, Problem | None]:
        mime = magic.from_file(file, mime=True)
        problem = None
        match mime:
            case "application/gzip" | "application/x-gzip":
                problem = self._execute_type(file, gzip.open, "gz", "gzip")
            case "application/x-bzip2":
                problem = self._execute_type(file, bz2.open, "bz2", "bzip2")
            case "application/x-xz":
                problem = self._execute_type(file, lzma.open, "xz", "xz")
            case "application/x-lzip":
                problem = self._execute_type(file, lzma.open, "lz", "lzip")
            case "application/x-lzma":
                problem = self._execute_type(file, lzma.open, "lzma", "lzma")
            case "application/zstd" | "application/x-zstd":
                problem = self._execute_type(file, zstandard.open, "zst", "Zstandard")
            case _:
                return (False, None)
        return (problem == None, problem)
