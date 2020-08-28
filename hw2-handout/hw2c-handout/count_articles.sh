#!/bin/bash

# Replace this line with one or more shell commands
# You may write to intermediate text files on disk if necessary
#ls test_*.txt
for file in test_*.txt
do
	the=$(grep -c '\bthe\b' $file);
	a=$(grep -c '\ba\b' $file);
	an=$(grep -c '\ban\b' $file);
	echo "${file},${the},${a},${an}";
done
#first, iterate all input files
#second, find counts using searching the,a and an word using grep command
#third, print filename, the count, a count and an count comma separated
