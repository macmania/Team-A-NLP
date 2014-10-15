import nltk
from nltk.book import *
validwords = [w for w in text7 if(len(w) >= 6 and w.isalpha)]
fdist = FreqDist(validwords)
print(fdist.most_common(50))