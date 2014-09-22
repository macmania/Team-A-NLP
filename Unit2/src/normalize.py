import glob
import errno
import nltk
#-------------------------------------------------------------------------------------------------------------
# inputs: clean texts from files
# outputs: processedListOfTexts
def normalize(processedListOfTexts,mitStopWords,nounList):
    # listOfTexts contains the raw strings of all cleaned texts
    listOfTexts = []
    #directory = "IslipExtractedFiles/*.txt"
    directory = "../../lib/Corpus/TexasExtractedFiles/*.txt"
    files = glob.glob(directory)
    print('There were '+str(len(files))+' files found in the ' + directory + ' directory.')
    for curr in files:
        try:
            with open(curr) as f:
                raw = f.read()
                listOfTexts.append(raw)
        except IOError as e:
            if e.errno != errno.EISDIR:
                raise
    print('\nListOfTexts has: '+str(len(listOfTexts))+' texts in it')

    # Process the raw strings
    print('\nStarting lemmatizing, normalization and removal of stop-words')
    wnl = nltk.WordNetLemmatizer()
    for text in listOfTexts:
        #temp=[]
        wordsInText=text.split()
        for i in range(0,len(wordsInText)):
            word=wordsInText[i]
            # lemmatize
            lemWord=(wnl.lemmatize(word)).lower()
            # Should replace wordsInText[i-1][-1]!='.' with ~ re
            if '.' not in wordsInText[i-1] and word.istitle(): # Look for capital first letter for nouns. Nouns are of special interest to us.    
                nounList.append(lemWord)            
            if lemWord not in mitStopWords and word.isalpha(): # beware : we lose number info    
                processedListOfTexts.append(lemWord) # append all processed words in a particular text to masterList         
    print('Done lemmatizing and normalization')

    return listOfTexts
