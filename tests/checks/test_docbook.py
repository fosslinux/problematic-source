import os

from checks.docbook import DocbookChecker
from checks.man import ManCheckerTester

class TestDocbookChecker(ManCheckerTester):
    checker = DocbookChecker(deep=False)
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdata", "docbook")
    NAME = "DocBook XSL Stylesheets"
