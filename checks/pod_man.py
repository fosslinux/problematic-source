from checks.man import ManChecker

class PodManChecker(ManChecker):
    MATCH = b"Automatically generated by Pod::Man"
    ERROR = "file generated by Perl's Pod::Man"
