import os
import filecmp

from transform.compressed import CompressedTransformer
from problem import Severity

class TestCompressedTransformer():
    path = os.path.join("testdata", "compressed")
    transformer = CompressedTransformer()
    
    def ok(self, filename: str):
        assert self.transformer.execute(os.path.join(self.path, filename)) == (True, None)
        noext = os.path.splitext(filename)[0]
        assert filecmp.cmp(os.path.join(self.path, "file"), os.path.join(self.path, noext))

    def test_ok1(self):
        self.ok("file1.gz")

    def test_ok2(self):
        self.ok("file2.bz2")

    def test_ok3(self):
        self.ok("file3.xz")

    def test_ok4(self):
        self.ok("file4.lz")

    def test_ok5(self):
        self.ok("file5.lzma")
    
    def test_ok6(self):
        self.ok("file6.zst")

    def test_bad1(self):
        changed, problem = self.transformer.execute(os.path.join(self.path, "file1.gnz"))
        assert changed == False
        assert problem != None
        assert problem.severity == Severity.UNSUPPORTED

    def test_bad2(self):
        changed, problem = self.transformer.execute(os.path.join(self.path, "file7.gz"))
        assert changed == False
        assert problem != None
        assert problem.severity == Severity.FATAL

    def test_none(self):
        assert self.transformer.execute(os.path.join(self.path, "file")) == (False, None)
