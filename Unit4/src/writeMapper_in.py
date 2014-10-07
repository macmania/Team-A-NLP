import os, glob, errno

def writeTrainList():
    files = glob.glob('../../Unit2/output/TexasExtractedFiles/*.txt')
    f= open('mapper_in.txt','w')
    for name in files:
        f.write(name)
    f.close()            
    
writeTrainList()
