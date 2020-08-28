
# IIT CS 585 Homework 3: Naive Bayes for Text Classification (80 points)
In this lab, you will extend the naive_bayes.py python program to implement the functionality of a Naive Bayes text classifier, and experiment to set the alpha hyperparameter to an optimal value.
Starting with the naive_bayes.py script, implement the missing calculations where indicated in the code with #TODO comments. Then run the Naive Bayes text classifier on the data set provided (which applies sentiment analysis to movie reviews) using different settings of the count smoothing parameter alpha. Choose the value that you think will give you the best performance on a held-out set of data, and set that as the value of ALPHA in the naive_bayes.py script.

Your submission will be evaluated on

the accuracy of probabilities calculated by the predict function for specific test cases
the overall accuracy of the classifier on held-out data, using the selected value of alpha
Download a template script for you to extend, as well as some sample outputs here(http://www.cs.iit.edu/~cs585/hw3/hw3-handout.tgz).

Download the data to use for model training here(http://www.cs.iit.edu/~cs585/hw3/hw3_data.tgz). The python script expects the data to be found in a directory named hw3_data. If you download both .tgz files to the same location, you should be able to get started by running:

tar xzf hw3-handout.tgz
tar xzf hw3_data.tgz
python -u naive_bayes.py
                
(You will get a math error, since none of the counts in the model are properly initialized.)
Submit your naive_bayes.py file to Autolab using the "Submit file" link.
