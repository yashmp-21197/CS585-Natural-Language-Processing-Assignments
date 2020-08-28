#!/bin/bash

# Replace this line with one or more shell commands
# You may write to intermediate text files on disk if necessary
cut -d ',' -f 3,5 > column35.txt
cut -d ',' -f 1 < column35.txt | awk '{print $1}' > column3.txt
cut -d ',' -f 2 < column35.txt > column5.txt
paste -d ' ' column3.txt column5.txt > column35.txt
awk '{for(i=2;i<=NF;i++) { if($1 == $i) { print $1 > "column35_lines.txt"; break;} } }' column35.txt
wc -l column35_lines.txt | tr ' ' '\n' | head -n 1
#first, copy column 3 and 5 in column35 file
#second, copy first word of 1st column in column3 file from column35 file
#third, copy 2nd column in column5 file from column35 file
#fourth, merge column3 and column5 and paste it in column35 file
#fifth, counth 1st word of every line in that line and print that word in column35_lines if count is more than
# sixth, count lines in column35_lines file, replace spaces with new line character and then take first line as required output
