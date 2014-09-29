import json
from pprint import pprint
from TaggingCorpus import extractTopPOS

json_data=open('../output/SolrOutput')
fOutput =  open('../output/SolrContentOutput.txt', 'r+')
data = json.load(json_data)

listLength = len(data["response"]["docs"])
content = ""
for query in data["response"]["docs"]:
    content +=str(query["content"])

fOutput.write(content)



#pprint(data)
json_data.close()
fOutput.close()

extractTopPOS('../output/SolrFolder')