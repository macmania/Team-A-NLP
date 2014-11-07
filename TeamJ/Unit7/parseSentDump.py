import re
from operator import itemgetter
import time

filename= 'sentdump.txt'
f = open(filename)
text= f.read()

ClusterDict={} # key : value, where key=Cluster_id, value=filename
def getSentsListFromCluster(cluster_id): # format VL-%d
    # find first occurrence of cluster_id
    c_id_idx= text.find(cluster_id)
    start_idx= c_id_idx
    # end_idx denotes beginning of next cluster 
    end_idx= text.find('VL-',c_id_idx+1)

    #Set search window to particular cluster output
    searchWindow= text[start_idx:end_idx]
    
    # Store cluster_size
    cluster_size= int(re.search('(n=)([0-9]+)',searchWindow).group(2))
    #print cluster_size
    #Store centroid
    centroid= re.search('(c=\[)(.+?)(\])',searchWindow).group(2)
    #print centroid

    # Store all filenames in this cluster
    fileTuples= re.findall('(1.0: /)(.+\.txt)',searchWindow)
    listOfFilenames = [t[1] for t in fileTuples]         
    #print listOfFilenames
    similarity= {} # dictionary of filename: similarityMeasure 
    # Find and process the list of sentences - choose top K
    for filename in listOfFilenames:
        #print searchWindow
        str_pre= '('+filename+' = \[)'+'(.+?)(])'     
        sentVect= re.search(str_pre, searchWindow).group(2)
        sim= getVectorsSimilarity(centroid,sentVect)
        similarity[filename]= sim

    sortedSimTuples= sorted(similarity.items(), key=itemgetter(1), reverse=True)

    #Choose top K documents (sentences) - we are choosing exactly one half 
    k= cluster_size/2
    topSentDocs= [t[0] for t in sortedSimTuples]
    ClusterDict[cluster_id]= topSentDocs[0:k]
    #print ClusterDict

def printSentsInCluster(cluster_id):
    sents=[]
    for filename in ClusterDict[cluster_id]:
        f= open ('../../collections/ClassEventAsSents/'+filename)
        #f= open ('../../lib/ClassEventAsSents/'+filename)
        sents.append(f.read())
    print len(sents)
    print sents

# Select clusters based on size 
def selectClusters():
    selectedClusters=[]
    cid_size_dict={}
    cid_size = re.findall('(VL-.*){n=([0-9]+)', text)
    cid_size_int= [(t[0],int(t[1])) for t in cid_size ]
    sorted_cid_size= sorted(cid_size_int, key=itemgetter(1), reverse=True)
    print sorted_cid_size
    print 'Selected clusters with big cluster size: '
    selectedClusters= [t[0] for t in sorted_cid_size if t[1]>1]
    print selectedClusters
    return selectedClusters

def getVectorsSimilarity(v1,v2):
    v2List= v2.split(', ')
    v1List= v1.split(', ')
    cv1 = {}
    cv2= {}
    #print 'Vectors v1 and v2 '
    #print v1List
    #print v2List
    for e in v1List:
        p = e.split(":")
        cv1[p[0].strip()] = float(p[1].strip())
    for e in v2List:
        p = e.split(":")
        cv2[p[0].strip()] = float(p[1].strip())
    sim = 0
    for k in cv2.keys():
        if k in cv1:
            sim += cv1[k]* cv2[k] 
    return sim

if __name__ == "__main__":
    selectedClusters= selectClusters()
    #print selectedClusters
    for c_id in selectedClusters:
        getSentsListFromCluster(c_id)
        printSentsInCluster(c_id)

"""
Notes:
1. re.findall(pattern, string, flags=0)
Return all non-overlapping matches of pattern in string, as a list of strings. The string is scanned left-to-right, and matches are returned in the order found. If one or more groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group. Empty matches are included in the result unless they touch the beginning of another match
"""

