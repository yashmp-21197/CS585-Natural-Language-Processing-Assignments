#!/bin/bash

# Replace this line with a sequence of shell commands connected with Unix pipes ("|")
tr ' ' '\n' | sed '/^$/d' | sort | uniq
#first, apply tr command to replance all space with new line character to separate all words
#second, apply sed command to remove unnecessary all blank spaces or newlines
#third, apply sort command to order all words in assending order
#fourth, apply uniq command to get all distinct words
