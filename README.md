# SpamClassifier
A simple Naive Bayes spam email classifier

To train:
python3 nblearn.py /path/to/input
Run nblearn.py, with the data directory as the only input argument. Data directory should contain directories named "ham" and "spam".
Generates model file "nbmodel.txt"

To classify:
python3 nbclassify.py /path/to/input
Input directory should contain emails to classify as .txt documents. Uses "nbmodel.txt" file.
Generates output file "nboutput.txt" with the predictions.

To evaluate:
python3 nbevaluate.py /path/to/nboutput.txt
Returns precision, recall, and F1 score for the model.
