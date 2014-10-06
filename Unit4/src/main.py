import os, glob, errno
from classifiers import *

#YourSmallDocsRawPath= '../../lib/Corpus/Islip13Rain'
YourSmallDocsRawPath= '../../lib/Corpus/YourSmallDocs_old/*.txt'
YourSmallDocs='../../lib/Corpus/YourSmallDocs/'

def main():
    #extractFeatures()
    #classify_NaiveBayes()
    #classify_DecisionTree()
    #classify_Maxent()
    #classify_SVM()
    crossValidation(nltk.NaiveBayesClassifier)
    crossValidation(nltk.DecisionTreeClassifier)
    crossValidation(nltk.MaxentClassifier)
    crossValidation(nltk.classify.SklearnClassifier(SVC()))
    
    
if __name__=="__main__":
    main()
