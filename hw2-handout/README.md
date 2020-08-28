
# IIT CS 585 Homework 2: Text Processing
# 2A: Vocabulary (30 points)
In this lab, you will write a shell script, called gen_vocab.sh. This program should
Read a text from standard input (STDIN),
Identify all of the words in the text, separated by the space character or a newline,
Print to standard output (STDOUT) a list of all of the distinct words occurring in the text, in ascending alphabetical order
Download a template script for you to extend, as well as some sample inputs and outputs, here(http://www.cs.iit.edu/~cs585/hw2/hw2a-handout.tgz).

Submit your gen_vocab.sh file to Autolab using the "Submit file" link.

# 2B: Compare columns (30 points)
In this lab, you will write a shell script, called compare_cols.sh. This program should
Read a CSV file from standard input (STDIN).
Note that in general, CSV files may contain quoted fields with embedded newlines. But for this assignment you can assume that there are no fields with embedded newlines, and therefore each new line represents a new row of the CSV file.
Print a single number (integer) to standard output (STDOUT): the count of the lines in the CSV file for which the first word occurring in column 3 of the CSV also occurs as a word in column 5 of the CSV.
For the purposes of this assignment, words are considered to be sequences of non-space characters delimited on either side by spaces or by the beginning/end of the text string.
Whitespace surrounding the integer output will be ignored for scoring.
For example, in the following CSV row, the word "six" occurs at the beginning of column 3, and also as a word in column 5:
one two three,four five,six seven,eight,nine six ten,eleven
Download a template script for you to extend, as well as some sample inputs and outputs, here(http://www.cs.iit.edu/~cs585/hw2/hw2b-handout.tgz).

Submit your compare_cols.sh file to Autolab using the "Submit file" link.

# 2C: Count articles (20 points)
In this lab, you will write a shell script, called count_articles.sh. This program should
Consider all of the files in the current working directory with names starting with test_ and ending with .txt.
Print one comma-separated row to standard output (STDOUT) for each input file, with four fields:
The first field should be the name of the file.
The second field should be the number of lines in the file that include "the" as a word.
The third field should be the number of lines in the file that include "a" as a word.
The fourth field should be the number of lines in the file that include "an" as a word.
Note that as in other exercises, words are considered to be sequences of non-space characters delimited on either side by spaces or by beginning/end of line.
Download a template script for you to extend, as well as some sample inputs and outputs, here(http://www.cs.iit.edu/~cs585/hw2/hw2c-handout.tgz).

Submit your count_articles.sh file to Autolab using the "Submit file" link.
