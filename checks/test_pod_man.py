import os

from checks.pod_man import PodManChecker 
from checks.man import ManCheckerTester

class TestPodManChecker(ManCheckerTester):
    checker = PodManChecker(deep=False)
    path = os.path.join("testdata", "pod_man")
    NAME = "Pod::Man"
