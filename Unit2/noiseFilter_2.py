# Filter noisy sentences from webpages. Assume that relevant text to us is only Sentenes.
# Assumption: sentences are strings ending with '.', '?' or '!'
import nltk
import re

#input : rawText Before tokenization.
#output: Input raw text is split into sentences. Non-sentences are discarded.
def noiseFilter_2(rawText):
    rawSentences=re.findall( '.+?[.?!]',rawText)
    # re.findall Returns all non-overlapping matches of 'string.' in rawText, as a list of strings
    #print(RawSentences)
    sentences= [sent for sent in rawSentences if len(sent)>80]
    return sentences
    
    #Now tokenize and continue processing
#noiseFilter_2('abc. def. \n\n\n\tTitle....! of \n\nSent1? Sent2.\nSent3.')    

#disadvantage: noise is discarded - can't create stop word list.
# So we use both approaches and give two results. better method depends on noisy text files.

