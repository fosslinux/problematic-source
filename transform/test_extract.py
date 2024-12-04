import filecmp
import os

from transform.extract import ExtractTransformer

class TestExtractTransformer():
    path = os.path.join("testdata", "extract")
    transformer = ExtractTransformer()

    def test_z_tar(self):
        assert self.transformer.execute(os.path.join(self.path, "z.tar")) == (True, None)
        assert not os.path.isfile(os.path.join(self.path, "z.tar"))
        assert os.path.isfile(os.path.join(self.path, "z"))
        assert filecmp.cmp(os.path.join(self.path, "z"), os.path.join(self.path, "answer", "z"))

    def test_big_tar(self):
        assert self.transformer.execute(os.path.join(self.path, "big.tar")) == (True, None)
        assert not os.path.isfile(os.path.join(self.path, "big.tar"))
        assert os.path.isdir(os.path.join(self.path, "some"))
        assert os.path.isdir(os.path.join(self.path, "some", "nested", "dir"))
        assert os.path.isfile(os.path.join(self.path, "some", "nested", "dir", "file"))
        assert filecmp.cmp(os.path.join(self.path, "some", "nested", "dir", "file"), os.path.join(self.path, "answer", "some", "nested", "dir", "file"))

    def test_zip(self):
        assert self.transformer.execute(os.path.join(self.path, "together.zip")) == (True, None)
        assert not os.path.isfile(os.path.join(self.path, "together.zip"))
        assert os.path.isfile(os.path.join(self.path, "nums"))
        assert filecmp.cmp(os.path.join(self.path, "nums"), os.path.join(self.path, "answer", "nums"))
        assert os.path.isdir(os.path.join(self.path, "other", "nested", "dir"))
        assert os.path.isfile(os.path.join(self.path, "other", "nested", "dir", "file"))
        assert filecmp.cmp(os.path.join(self.path, "other", "nested", "dir", "file"), os.path.join(self.path, "answer", "other", "nested", "dir", "file"))

    def test_nop(self):
        assert self.transformer.execute(os.path.join(self.path, "d")) == (False, None)
