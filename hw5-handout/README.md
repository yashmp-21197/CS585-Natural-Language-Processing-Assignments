
#IIT CS 585 Homework 5: CYK Phrase Parsing (80 points)
In this assignment, you will extend the cyk.py python program to implement the Cocke-Younger-Kasami Parsing algorithm.
Starting with the cyk.py script, implement the missing functionality where indicated in the code with #TODO comments. (The missing piece to fill in is the bottom-up traversal of the chart to fill in information about constituents that span different subparts of the sentence.)

The resulting script will read a grammar file with phrase structure rules and a sentence file with sentences to parse, and will output a single valid parse for each sentence in the input (or "Parsing failed", in case it cannot be parsed).

You can check your parsing code using the test grammars and input sentences provided. To run the script on grammar 1, for example, run:

python cyk.py --grammar_file grammar_1.txt --sentence_file sentences_1.txt
                
Note that your output may differ from the answer provided if a senence is ambiguous (multiple different parses are possible according to the grammar). The automatic grader will give credit for any parse that is valid according to the grammar.
Your submission will be evaluated on

whether it produces a correct parse for each sentence according to the grammar (or fails to parse in case the sentence is not admissible given the grammar).
Download a template script for you to extend, as well as some sample outputs here(http://www.cs.iit.edu/~cs585/hw5/hw5-handout.tgz).

Submit your cyk.py file to Autolab using the "Submit file" link.