import os, glob, errno, re
import nltk
# feature extractor
#input text is string
featureList=['texas', 'west', 'north', 'waco', 'town', 'explosion', 'blast', 'fertilizer', 'plant', 'company', 'fire', 'flames', 'firefighters', 'responders', 'extinguish', 'people', 'damage', 'destroyed', 'danger', 'injured', 'dead', 'death', 'killed', 'casualties', 'bodies', 'toll', 'rescue', 'buildings', 'homes', 'wednesday', 'authorities', 'officials', 'police', 'state', 'trooper', 'firemen', 'cause', 'ammonia', 'chemical', 'Mary', 'Reyes', 'farming', 'community']
trainFeatureSets=[]
testFeatureSets=[]

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
    
