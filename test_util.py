import os
import pytest
import util

class TestWalkDirectory():
    @pytest.fixture(autouse=True)
    def chdir(self, monkeypatch):
        monkeypatch.chdir(os.path.join("testdata", "util", "walk_directory"))

    def test_simple(self):
        assert sorted(util.walk_directory("simple")) == [
            "simple/a/b/c",
            "simple/d",
        ]

    def test_complex(self):
        assert sorted(util.walk_directory("complex")) == [
            "complex/x/d",
            "complex/x/w/y/c",
            "complex/x/w/z/a",
            "complex/x/y/b",
            "complex/x/y/z/a",
        ]

    def test_empty1(self):
        assert util.walk_directory("empty1") == []

    def test_empty2(self):
        assert util.walk_directory("empty2") == []
