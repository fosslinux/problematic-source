# problematic-source

This program provides a number of heuristics to find pre-generated files within
a codebase, and to report on those problems.

The program is quite straightforward to use. Simply point it to a tarball, git
repository, or something else, wait a few seconds to minutes, and then create a
report on the pre-generated files within the codebase. Eg:

```
python3 main.py -o report.txt coreutils.tar.gz
```

## Known Issues

- This program is still fairly rough around the edges. Problems are to be expected.
- Sometimes, you may come up with a new heuristic that you think makes sense in
  general. Create a PR or issue.

## Reporting

The report's primary purpose is for live-bootstrap, so the categories are
created with that in mind. The report exists to help you document your findings. 
