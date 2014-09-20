import glob
import errno
import os
from noiseFilter_1 import  *
from noiseFilter_2 import  *

#-------------------------------------------------------------------------------------------------------------
# input: noisy files
# output: 1) raw extracted string (non-tokenized), 2) cleaned text files, 3) sublStopWordList.
def cleanUp_1(extractTxt,sublStopWords):
    print('Beginning to clean up files and Extraction of article contents')
    files = glob.glob("Texas Fertilizer Plant Explosion/*.txt")
    #files = glob.glob("Islip13Rain/*.txt")
    artcle, nonArtcl = 0, 0
    art, nonArt = [], [] 
    for name in files: 
            try: 
                    with open(name) as f: 
                            lines = f.read()
                            if classifyTxt(lines):
                                    artcle += 1 # counts how many articles it has classified successfully
                                    #if artcle%50==0:
                                    print ('Articles=',artcle)
                                    art.append(name)
                                    fileName=os.path.split(name)[1]
                                    extractTxt = extractTxtArticle(lines)
                                    newFile = open(str("TexasExtractedFiles/" + fileName), 'w')
                                    #newFile = open(str("IslipExtractedFiles/" + fileName), 'w')
                                    newFile.write(str(extractTxt))
                            else:
                                    sublStopWords.append(lines)
                                    nonArtcl += 1
                                    if nonArtcl%100==0:
                                            print('Non article=',nonArtcl)
                                    nonArt.append(name)
            except IOError as exc: 
                    if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
                            raise # Propagate other kinds of IOError
    print('Extraction of article contents Done')        

#-------------------------------------------------------------------------------------------------------------
# input: noisy files
# output: 1) raw extracted string (non-tokenized), 2) cleaned text files.
def cleanUp_2(extractTxt):
    # Note: no sub-language stop word list created in this method
    print('Beginning to clean up files and Extraction of article contents')
    files = glob.glob("Texas Fertilizer Plant Explosion/*.txt")
    #files = glob.glob("Islip13Rain/*.txt")
    fileCount=0
    for name in files: 
        try: 
            with open(name) as f: 
                lines = f.read()
                extractTxt=noiseFilter_2(lines)
                fileName=os.path.split(name)[1]
                newFile = open(str("TexasExtractedFiles/" + fileName), 'w')
                #newFile = open(str("IslipExtractedFiles/" + fileName), 'w')
                newFile.write(str(extractTxt))
                fileCount+=1
                print(fileCount)
        except IOError as exc: 
            if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
                raise # Propagate other kinds of IOError
    print('Extraction of article contents Done')
