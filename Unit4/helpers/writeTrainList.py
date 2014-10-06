from TextUtils import *
import os, glob, errno

YourSmallDocsRawPath= '../../lib/Corpus/YourSmallDocs_old/*.txt'
YourSmallDocs='../../lib/Corpus/YourSmallDocs/'
def getYourSmallDocs():
    print('Beginning Extraction of raw article contents')
    files = glob.glob(YourSmallDocsRawPath)
    for name in files: 
        try: 
            with open(name) as f: 
                text= f.read()
                #print 'Done reading'
                f.close()
                text= filter_empty_lines(text)
                text= filter_non_alpha_chars(text)
                filename= os.path.join(YourSmallDocs,os.path.basename(name))
                f1= open("%s"%(filename),'w')
                f1.write(text)
                f1.close()
        except IOError as exc: 
            if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
                raise # Propagate other kinds of IOError
    print('Extraction of YourDocs and cleaning up done')

getYourSmallDocs()
