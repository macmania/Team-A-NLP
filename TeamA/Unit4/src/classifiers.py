import os, glob, errno, re
import nltk
#from sklearn.svm import SVC
from cPickle import dump

featureList=['texas', 'west', 'north', 'waco', 'town', 'explosion', 'blast', 'fertilizer', 'plant', 'company', 'fire', 'flames', 'firefighters', 'responders', 'extinguish', 'people', 'damage', 'destroyed', 'danger', 'injured', 'dead', 'death', 'killed', 'casualties', 'bodies', 'toll', 'rescue', 'buildings', 'homes', 'wednesday', 'authorities', 'officials', 'police', 'state', 'trooper', 'firemen', 'cause', 'ammonia', 'chemical', 'Mary', 'Reyes', 'farming', 'community', 'determine', 'investigation', 'department']
output = open('featureList.pkl', 'wb')
dump(featureList, output, -1)
output.close()
    
trainFeatureSets=[]
testFeatureSets=[]

def saveTrainModel(trainModel):
    output = open('classifierModel.pkl', 'wb')
    dump(trainModel, output, -1)
    output.close()
    
# Do this based on most_informative_features
# TO BE DONE
def modifyFeatureList(): 
    print ''
    
def crossValidation(classifier):
    f1= open('YourSmallAllLabelled.txt')
    totalAcc=0
    allImages= f1.read().splitlines()
    f1.close()
    numImgs= len(allImages)
    print numImgs
    for i in range(0,5):
        startIdxTestImgs= int((numImgs*i)/5)
        endIdxTestImgs= int((numImgs*(i+1))/5)
        #print range(startIdxTestImgs,endIdxTestImgs)
        #print 'Starting Index of testing images = '+str(startIdxTestImgs)
        #print 'Starting Index of testing images = '+str(endIdxTestImgs)
        for idx in range(0, numImgs): # name.split()[0] = file name, [1]= label
            name = allImages[idx]
            f2= open(os.path.join('../YourSmallAllLabelled',name.split()[0]))
            if idx in range(startIdxTestImgs,endIdxTestImgs):
                print 'Testing using '+name.split()[0]
                testFeatureSets.append((feature_ext(f2.read().lower()),name.split()[1]))
            else:
                print 'Training using '+name.split()[0]
                trainFeatureSets.append((feature_ext(f2.read().lower()),name.split()[1]))
            f2.close()
            # Train and test classifier for this set of training/test data
        training_model= nltk.NaiveBayesClassifier.train(trainFeatureSets)
        #print(str(classifier)+' accuracy = ')
        acc= nltk.classify.accuracy(training_model, testFeatureSets)    
        #print acc
        totalAcc+= acc
    avgAcc=totalAcc/5
    print str(classifier)+' average accuracy ='+str(avgAcc)
    return training_model

def extractFeatures():
    f1= open('YourSmallTrain.txt')
    trainImages= f1.read().splitlines()
    f1.close()
    f1= open('YourSmallTest.txt')
    testImages= f1.read().splitlines()
    f1.close()
    #print 'trainImages'
    #print trainImages
    for name in trainImages: # name.split()[0] = file name, [1]= label
        print 'Training using '+name.split()[0]
        f2= open(os.path.join('../TrainYourSmall',name.split()[0]))
        trainFeatureSets.append((feature_ext(f2.read().lower()),name.split()[1]))
        f2.close()
    for name in testImages:
        print 'Testing using '+name.split()[0]
        f2= open(os.path.join('../TestYourSmall',name.split()[0]))
        testFeatureSets.append((feature_ext(f2.read().lower()),name.split()[1]))
        f2.close()
    return classifier

def feature_ext(text):
    #print 'text'+text
    featureset={}
    for word in featureList:
        featureset[word]= doesWordExist(word, text)
    #print 'featureset'+str(featureset)
    return featureset

def doesWordExist(word, text):
    if re.search(word,text):
        return True
    else:
        return False
    
def classify_NaiveBayes():
    # Train Naive Bayes classifier 
    classifier_NB = nltk.NaiveBayesClassifier.train(trainFeatureSets)
    print 'Naive Bayes classifier accuracy= '
    print nltk.classify.accuracy(classifier_NB, testFeatureSets)
    return classifier_NB

def classify_DecisionTree():
    # Train Naive Bayes classifier 
    classifier_DT = nltk.DecisionTreeClassifier.train(trainFeatureSets)
    print 'Decision Tree classifier accuracy= '
    print nltk.classify.accuracy(classifier_DT, testFeatureSets)
    return classifier_DT

def classify_Maxent():
    print 'Train Maximum Entropy classifier'
    classifier_ME = nltk.classify.MaxentClassifier.train(trainFeatureSets)
    print 'Maximum Entropy classifier accuracy= '
    print nltk.classify.accuracy(classifier_ME, testFeatureSets)
    return classifier_ME

def classify_SVM():
    print 'Train SVM classifier'
    #classifier_SVM = nltk.classify.SklearnClassifier(SVC()).train(trainFeatureSets)
    #print 'SVM classifier accuracy= '
    #print nltk.classify.accuracy(classifier_SVM, testFeatureSets)    
