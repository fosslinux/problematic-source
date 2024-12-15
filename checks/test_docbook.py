import os

from checks.docbook import DocbookChecker
from checks.man import ManCheckerTester

class TestDocbookChecker(ManCheckerTester):
    checker = DocbookChecker(deep=False)
    path = os.path.join("testdata", "docbook")
    NAME = "DocBook XSL Stylesheets"
