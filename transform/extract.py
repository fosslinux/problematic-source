import magic
import os
import tarfile
import zipfile

from problem import Problem, Severity

class ExtractTransformer():
    MAGIC = 0xE8AC

    def execute(self, file: str) -> tuple[bool, Problem | None]:
        mime = magic.from_file(file, mime=True)
        match mime:
            case "application/x-tar":
                try:
                    with tarfile.open(file) as tar:
                        tar.extractall(path=os.path.dirname(file), filter="data")
                except tarfile.TarError as e:
                    return (False, Problem(Severity.FATAL, f"Unable to extract tar archive: {e}", file, self.MAGIC))
                os.remove(file)
                return (True, None)
            case "application/zip":
                try:
                    with zipfile.ZipFile(file, "r") as zipped:
                        zipped.extractall(path=os.path.dirname(file))
                except (zipfile.BadZipFile, zipfile.LargeZipFile) as e:
                    return (False, Problem(Severity.FATAL, f"Unable to extract zip archive: {e}", file, self.MAGIC))
                os.remove(file)
                return (True, None)
            case _:
                return (False, None)
