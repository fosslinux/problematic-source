from typing import Dict

from checks.base import Checker
from util import walk_directory, get_mime
from problem import Problem, Severity 

class MimeChecker(Checker):
    MAGIC = 0x414E

    # partially lifted from Debian's devscripts suspicious-source
    WHITELIST = [
        "application/pgp-keys",
        "application/vnd.font-fontforge-sfd",  # font source: fontforge
        "application/x-elc",
        "application/x-empty",
        "application/x-font-otf",  # font object and source
        "application/x-font-ttf",  # font object and source
        "application/x-font-woff",  # font object and source
        "application/x-symlink",
        "application/xml",
        "application/javascript",
        "application/x-javascript",
        "audio/x-wav",
        "font/otf",  # font object and source
        "font/ttf",  # font object and source
        "image/gif",
        "image/jpeg",
        "image/png",
        "image/svg+xml",
        "image/tiff",
        "image/vnd.adobe.photoshop",
        "image/x-icns",
        "image/x-ico",
        "image/x-icon",
        "image/x-ms-bmp",
        "image/x-portable-pixmap",
        "image/x-xpmi",
        "image/x-xcf",
        "inode/symlink",
        "inode/x-empty",
        "message/rfc822",
        "text/html",
        "text/plain",
        "text/rtf",
        "text/javascript",
        "text/troff",
        "text/x-Algol68",
        "text/x-asm",
        "text/x-awk",
        "text/x-c",
        "text/x-c++",
        "text/x-diff",
        "text/x-fortran",
        "text/x-java",
        "text/x-lisp",
        "text/x-m4",
        "text/x-makefile",
        "text/x-msdos-batch",
        "text/x-objective-c",
        "text/x-pascal",
        "text/x-perl",
        "text/x-php",
        "text/x-po",
        "text/x-ruby",
        "text/x-script.python",
        "text/x-shellscript",
        "text/x-tcl",
        "text/x-tex",
        "text/x-texinfo",
        "text/xml",
    ]

    BLACKLIST = [
        "application/x-pie-executable",
        "application/x-executable",
        "application/x-gettext-translation",
        "application/x-java-applet",
        "application/java-archive",
        "application/x-archive",
        "application/x-object",
        "application/x-sharedlib",
        "application/x-mach-binary",
        "application/x-coff",
        "application/vnd.microsoft.portable-executable",
    ]

    def execute(self, file: str) -> Problem | None:
        mime = get_mime(file)
        if mime in self.BLACKLIST:
            return Problem(Severity.ERROR, f"{mime} is blacklisted", file, self.MAGIC)
        elif mime not in self.WHITELIST:
            return Problem(Severity.WARN, f"{mime} is not whitelisted", file, self.MAGIC)
        return None
