# This file is in the same path as the source and dest folders
# Steps:
# 1. Run this file after editing source and destFolder
source= './Big_Jon/*.txt'
destFolder= 'LabelledBig_Jon'
# 2. Read document contents on screen and verify if the doc is pos / neg
# 3. Hit 'p' or 'n' or 's' on the keyboard to label the document as positive,
#    negative or to skip the document (without labelling) and go to the next doc.
# 4. Once you choose an option, the doc is automatically labelled. Repeat 1-3.
# 5. Make sure you have an equal number of positive and negative docs (75 each)-
#    use skip option. Also use skip if doc contents are identical to previous docs.
# 6. Hit 'x' to exit

import glob, os, sys

countPos=0
countNeg=0

docs = glob.glob(source)
for doc in docs:
    fread=open(doc)
    contents= fread.read()
    fread.close()
    print contents
    keyIn = raw_input('Is doc positive (p) or negative(n)? : ')
    if keyIn=='p':
        f= open(os.path.join(destFolder,os.path.basename(doc)[:-4]+'_pos.txt'),'w')
        f.write(contents)
        f.close()
        countPos+=1
    elif keyIn=='n':
        f= open(os.path.join(destFolder,os.path.basename(doc)[:-4]+'_neg.txt'),'w')
        f.write(contents)
        f.close()
        countNeg+=1
    else :
        print 'Skipping to next document'
    print 'Labelled positive =', countPos
    print 'Labelled negative =', countNeg

        
