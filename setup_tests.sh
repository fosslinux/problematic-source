#!/bin/bash

set -e

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

# test_compressed_rename.py
mkdir -p compressed_rename
pushd compressed_rename || exit

touch x.tgz
touch y.tar.gz

popd || exit
#

# test_extract.py
mkdir -p extract
pushd extract || exit

echo hello > a
echo xyz > b
echo zzzzzz > z
mkdir -p some/nested/dir
echo abc > some/nested/dir/file
echo 1 2 3 > nums
mkdir -p other/nested/dir
echo 4 5 6 > other/nested/dir/file
mkdir -p answer
cp -r ./* answer || true
tar -cf big.tar a b some
tar -cf z.tar z
zip -r together.zip nums other
rm -r a b z some/nested other
touch d

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

# test_gnulib.py
mkdir -p gnulib
pushd gnulib || exit

mkdir -p bad/m4
echo "# Generated by gnulib-tool.\nsomething else" > bad/m4/gnulib-comp.m4

mkdir -p bad_deep/a/b
echo "#!/bin/bash\necho a script\n# Generated by gnulib-tool." > bad_deep/a/b/covert.sh

mkdir -p ok
echo nothing to see here > ok/s
mkdir -p ok/a/b
cp /bin/sh ok/a/b/

popd || exit
#

# test_autotools.py
mkdir -p autotools
pushd autotools || exit

echo "# File generated by automake 2.55" > Makefile.bad.in
echo "# Generated by GNU Autoconf 2.69" > configure
echo "nothing to see here" > Makefile.in
mkdir a
echo "this one's ok too" > a/configure
echo "# generated automatically by aclocal 1.15 -*- Autoconfig" > a/aclocal.m4
echo "# some handwritten aclocal.m4" > aclocal.m4
touch config.h.in
echo hii > allgood

popd || exit
#

# test_comments.py
mkdir -p comments
pushd comments || exit

echo "// DO NOT MODIFY THIS FILE!" > a.c
echo "# This file was generated by Bob's code generator" > b.sh
echo "int main() {return 42;}" > c.c
echo "A recipe book" > d.txt
echo "/* Be careful with this file. It was generated by James over 20 years ago and barely works anymore. */" > e

popd || exit
#

# test_help2man.py
mkdir -p help2man
pushd help2man || exit

echo ".\\\" DO NOT MODIFY THIS FILE!  It was generated by help2man 1.25." > bad.1
echo ".\\\" DO NOT MODIFY THIS FILE!  It was generated by help2man 1.25." > bad.8
echo ".\\\" DO NOT MODIFY THIS FILE!  It was generated by help2man 1.25." > bad.man
echo ".SH I made this myself!" > good.3
echo "no problem" > random.txt

popd || exit
#

# test_pod_man.py
mkdir -p pod_man
pushd pod_man || exit

echo ".\\\" Automatically generated by Pod::Man 1.23." > bad.1
echo ".\\\" Automatically generated by Pod::Man 1.23." > bad.8
echo ".\\\" Automatically generated by Pod::Man 1.23." > bad.man
echo ".SH I made this myself!" > good.3
echo "no problem" > random.txt

popd || exit
#

# test_docbook.py
mkdir -p docbook 
pushd docbook || exit

echo ".\\\" Generator: DocBook XSL Stylesheets" > bad.1
echo ".\\\" Generator: DocBook XSL Stylesheets" > bad.8
echo ".\\\" Generator: DocBook XSL Stylesheets" > bad.man
echo ".SH I made this myself!" > good.3
echo "no problem" > random.txt

popd || exit
#

# test_po4a.py
mkdir -p po4a 
pushd po4a || exit

echo ".\\\" This file was generated with po4a. Translate the source file." > bad.1
echo ".\\\" This file was generated with po4a. Translate the source file." > bad.8
echo ".\\\" This file was generated with po4a. Translate the source file." > bad.man
echo ".SH I made this myself!" > good.3
echo "no problem" > random.txt

popd || exit
#

# test_autogen.py
mkdir -p autogen
pushd autogen || exit

echo "  This file has been AutoGen-ed!" > Makefile.in.in
echo "# This file was generated by GNU Autoconf" > configure
echo "//  Generated from AutoOpts" > bad.c
echo "// I am a normal C file" > innocent.c
touch bad.def autogen.def

popd || exit
#

# test_texi.py
mkdir -p texi
pushd texi || exit

touch x.dvi x.pdf x.texi
echo "This is x.info, produced by makeinfo version 6.7" > x.info
echo "Created on January 1, 1970 by texi2html 5.0" > x.html
echo "This is a handwritten .info file" > y.info
echo "<!DOCTYPE html>" > y.html
echo "This looks like it could be generated, but isn't" > z.info
touch z.texi
echo "<!DOCTYPE html>" > hidden
echo "<title>sneaky</title>" >> hidden
echo "This is hidden.info, renamed, produced by makeinfo" > imnothere
echo "normal file" > normal.txt

popd || exit
#

# test_bison.py
mkdir -p bison
pushd bison || exit

echo "/* A Bison parser, made from parse.y */" > a.c
echo "/* A Bison parser, made from betterparser.y */" > b
echo "int main() {return 42;}" >> b
echo "int main() {return 42;}" > c.c
echo "#ifndef BISON_Y_TAB_H" > d.h
echo "#define HI 42" > e.h
cp e.h a.h
touch y.tab.c y.tab.h
touch f.y f.c f.h

popd || exit
#

# test_flex.py
mkdir -p flex
pushd flex || exit

echo "/* A lexical scanner generated by flex 2.6.4 */" > a.c
echo "/* A lexical scanner written by hand */" > b.c
echo "nothing" > nothing.txt
cp b.c d.c
touch d.l
cp b.c lex.yy.c

popd || exit
#

# test_gperf.py
mkdir -p gperf
pushd gperf || exit

echo "/* ANSI-C code produced by gperf version 3.0.3 */" > a.h
echo "/* this is a normal file" > b.h
echo "ntohing" > nothing.txt
touch c.c c.h c.gperf

popd || exit
#

popd || exit
