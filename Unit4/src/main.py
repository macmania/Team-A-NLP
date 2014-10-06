import os, glob, errno
from classifier import *

#YourSmallDocsRawPath= '../../lib/Corpus/Islip13Rain'
YourSmallDocsRawPath= '../../lib/Corpus/YourSmallDocs_old/*.txt'
YourSmallDocs='../../lib/Corpus/YourSmallDocs/'

def main():
    extractFeatures()
    classify_NaiveBayes()
    
if __name__=="__main__":
    main()
