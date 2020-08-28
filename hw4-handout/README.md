
# IIT CS 585 Homework 4: Using pre-trained BERT vectors for text classification
(150 points)
In this assignment, you will build a text classification model to address the task of native language identification. You are given a dataset of English texts authored by writers whose native language is some other language than English, and you will build a model to predict their native language based on the text.
You will use a tool called BERT (Bidirectional Encoder Representations from Transformers), developed at Google, to obtain vector representations for each text, and then use these representations as predictive features in your model. BERT is a flexible neural-network model for NLP that has demonstrated high accuracy across many tasks. However, it is also quite resource-intensive. For that reason, we will only be using it for feature generation, rather than retraining the model itself.

# Assignment Details
In order to complete the assignment, you will need to

Clone the BERT repository (https://github.com/google-research/bert) from the maintainers into a local directory on your computer, which you can later refer to as BERT_BASE_DIR. E.g., you can run the command:
 git clone https://github.com/google-research/bert.git
Download a pre-trained BERT model and uncompress it into a location you can refer to as BERT_DATA_DIR. I recommend BERT-Base, Uncased (https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip), which is about half a gigabyte uncompressed.
Programmatically re-format the datafiles from the handout materials (http://www.cs.iit.edu/~cs585/hw4/hw4-handout.tgz) so that they can be processed by the BERT extract_features.py script. This script requires that each input file contain each text on a single line, with no other information.
Run the texts through BERT using the run_bert_fv.sh script (adapting it as necessary) in order to generate feature vectors to represent each document. This takes about 45 minutes on my laptop, with no GPU, and results in about 7.5 GB of data. Note that the BERT repository is not compatible with Tensorflow 2; you may need to downgrade the Tensorflow version in your python environment to an earlier version. (I used 1.14.)
Train a text categorization model using the features derived from BERT in order to predict the native_language attribute of the data provided. A example of how to read BERT vectors and use them in an sklearn model is provided in a notebook in the handout materials.
Use the trained model to make predictions on the test data (lang_id_test.csv). Produce appropriate evaluation metrics for each class, and identify the frequencies of misclassifications between each pair of classes.
Document your work with a written summary (markdown, text, or PDF format), which should include:
Instructions for running your code on the data provided in order to reproduce your results
A summary of your evaluation findings, including overall performance, metrics by class, and frequency of errors between classes
Notes on any challenges you ran into during the assignment that contributed to incomplete or suboptimal results

# Resources
Download the data, a shell script demonstrating BERT feature extraction, and a sample modeling notebook here(http://www.cs.iit.edu/~cs585/hw4/hw4-handout.tgz).

You will also need the BERT repsitory (https://github.com/google-research/bert) on GitHub, and a pre-trained model such as this one(https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip).

# Scoring
Your submission will be scored manually by the instructor and TA, based on the following criteria:

Completeness (50 points): Whether the project completes all of the steps requested under Assignment Details -- data processing, generation of feature vectors, training a model, generating evaluation results, and documenting the process and results
Correctness (50 points): Whether the project is free of conceptual or coding errors that would invalidate the evaluation results obtained
Writeup (50 points): Whether the writeup is clear, correct and thorough in its description of the process for analyzing the data, and its presentation of the evaluation results obtained. Note that the discussion should go beyond simply reporting evaluation metrics, and include some discussion about what those metrics indicate about the nature of the problem, and what opportunities for further improvement there might be.
Your submission will not be scored based on the accuracy of the model created for this project.

# Submission
When you have completed the assignment, compress all of your code and documentation files into a single zipfile named project.zip. Do not include the data files or the code from the BERT repository in this zipfile. Submit your project.zip file to Autolab using the "Submit file" link.
