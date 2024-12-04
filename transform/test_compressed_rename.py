import os

from transform.compressed_rename import CompressedRenameTransformer

class TestCompressedRenameTransformer():
    path = os.path.join("testdata", "compressed_rename")
    transformer = CompressedRenameTransformer()

    def test_ok(self):
        assert self.transformer.execute(os.path.join(self.path, "x.tgz")) == (True, None)
        assert os.path.isfile(os.path.join(self.path, "x.tar.gz"))
        assert not os.path.isfile(os.path.join(self.path, "x.tgz"))

    def test_nop(self):
        assert self.transformer.execute(os.path.join(self.path, "y.tar.gz")) == (False, None)
        assert os.path.isfile(os.path.join(self.path, "y.tar.gz"))
