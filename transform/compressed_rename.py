import os

class CompressedRenameTransformer():
    def execute(self, file: str) -> tuple[bool, None]:
        newname = None
        if file.endswith(".tgz"):
            newname = file.removesuffix(".tgz") + ".tar.gz"
        if newname:
            os.rename(file, newname)
            return (True, None)
        return (False, None)
