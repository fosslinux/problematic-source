import os

from checks.pod_man import PodManChecker 
from checks.man import ManCheckerTester

class TestPodManChecker(ManCheckerTester):
    checker = PodManChecker(deep=False)
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdata", "pod_man")
    NAME = "Pod::Man"
