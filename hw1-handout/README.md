
#IIT CS 585 Homework 1: Distributional Measures (80 points)
In this lab, you will write a python program, called dist_measures.py. This program should
Read a list of words from text_a.txt, and calculate the frequency distribution of words in that text.
Read a list of words from text_b.txt, and calculate the frequency distribution of words in that text.
Calculate the following measures, and print them on eight consecutive lines, rounded to three digits:
The entropy of the frequency distribution for list A -- H(P(A))
The entropy of the frequency distribution for list B -- H(P(B))
The cross-entropy -- H(P(A),P(B))
The cross-entropy -- H(P(B),P(A))
The KL divergence -- D_{KL}(P(A)||P(B))
The KL divergence -- D_{KL}(P(B)||P(A))
The JS divergence -- D_{JS}(P(A)||P(B))
The JS divergence -- D_{JS}(P(B)||P(A))
For convenience (Python's math.log function is the natural log), calculate all values in nats rather than bits.

Download a template script for you to extend, as well as some sample inputs and outputs, here(http://www.cs.iit.edu/~cs585/hw1/hw1-handout.tgz).

Do not import any python packages in your code other than those that are already included in the template script.

Submit your dist_measures.py file to Autolab using the "Submit file" link.