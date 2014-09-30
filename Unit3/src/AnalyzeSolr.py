import json
from pprint import pprint
from TaggingCorpus import extractTopPOS


json_data=open('../output/SolrFolder/SolrOutput')
fOutput =  open('../output/SolrFolder/SolrContentOutput.txt', 'r+')
data = json.load(json_data)

listLength = len(data["response"]["docs"])
content = " "
i = 0
'''
for query in data["response"]["docs"]:
    fOutput =  open(str( '../output/' + str(i) +'.txt'), 'w')
    print query["content"]
    content = query["content"]
    if len(content) != 0:
        fOutput.write(str(content))
    fOutput.close()
    i += 1
    #content = content + str(query["content"])
print ''.join(content)
'''
#fOutput.write(''.join(content))



#pprint(data)
json_data.close()

extractTopPOS('../output/', 'solr folder')
