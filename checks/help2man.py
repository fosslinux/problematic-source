from checks.man import ManChecker

class Help2manChecker(ManChecker):
    MATCH = b"generated by help2man"
    ERROR = "file generated by help2man"
    MAGIC = 0xE12A
