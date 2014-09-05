import os

# You must install the Sunburnt 0.7 to work with the Solr version provided in the link below, please see the installing tutorial
from sunburnt import SolrInterface

si = SolrInterface("http://jingluo.dlib.vt.edu:8080/solr/")

# This is where you put the event name (collection name)
# event name is "China flood", you need to change the even name in the line below according to your specific event name
eventQuery = "Train Derailment in Quebec"

print("poop")

# This is where you put the downloaded files, you need to change this according to your directory location
root = 'D:/Storage/EventCollections/'

response = si.query(event=eventQuery).execute()

# This will return the number of documents found in the event (collection)
tot = response.result.numFound


response = si.query(event=eventQuery).paginate(0,tot).execute()

docs = {}

# This will print the number of documents found in the event (collection)
print response.result.numFound

i = 1

directory = root + "//" + eventQuery

# This is to create a directory for the event name
if not os.path.exists(directory):
    os.makedirs(directory)

# This loop is to store the text files extracted form Solr
for res in response:
    f = open(directory + "//" + str(i) + ".txt","w")

    content = res['content'][0]

    f.write(content.encode("utf-8"))

    f.close()

    i+=1
    