import magic 
from typing import Dict

from util import walk_directory
from problem import Problem, Severity 

class MimeChecker:
    # lifted from Debian's devscripts suspicious-source
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
        "inode/symlink",
        "inode/x-empty",
        "message/rfc822",
        "text/html",
        "text/plain",
        "text/rtf",
        "text/troff",
        "text/x-asm",
        "text/x-c",
        "text/x-c++",
        "text/x-diff",
        "text/x-fortran",
        "text/x-java",
        "text/x-lisp",
        "text/x-m4",
        "text/x-makefile",
        "text/x-msdos-batch",
        "text/x-pascal",
        "text/x-perl",
        "text/x-php",
        "text/x-po",
        "text/x-ruby",
        "text/x-script.python",
        "text/x-shellscript",
        "text/x-tex",
        "text/x-texinfo",
        "text/xml",
    ]

    BLACKLIST = [
        "application/x-pie-executable",
        "application/x-executable",
    ]

    def execute(self, file: str) -> [Problem | None]:
        mime = magic.from_file(file, mime=True)
        if mime in self.BLACKLIST:
            return Problem(Severity.ERROR, f"{mime} is blacklisted")
        elif mime not in self.WHITELIST:
            return Problem(Severity.WARN, f"{mime} is not whitelisted")
        return None
