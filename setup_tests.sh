#!/bin/bash

rm -rf testdata

mkdir -p testdata
pushd testdata || exit

# test_util.py
mkdir -p util
pushd util || exit

### walk_directory
mkdir -p walk_directory
pushd walk_directory || exit
touch x

mkdir -p simple/a/b
touch simple/a/b/c simple/d

mkdir -p complex/x/y/z complex/x/w/z complex/x/w/y
touch complex/x/y/z/a complex/x/y/b complex/x/w/z/a complex/x/w/y/c complex/x/d

mkdir -p empty1

mkdir -p empty2/a empty2/b empty2/c empty2/a/d empty2/a/d/e

popd || exit
###

popd || exit
#

# test_compressed.py
mkdir -p compressed
pushd compressed || exit

echo hello > file
gzip -ck file > file1.gz
bzip2 -ck file > file2.bz2
xz -ck file > file3.xz
lzip -ck file > file4.lz
lzma -ck file > file5.lzma
zstd -ck file > file6.zst
cp file1.gz file1.gnz
head -c 6 file1.gz > file7.gz

popd || exit
#

# test_mime.py
mkdir -p mime
pushd mime || exit

echo hello > ok
cp /bin/bash bad
echo > warn

popd || exit
#

popd || exit
