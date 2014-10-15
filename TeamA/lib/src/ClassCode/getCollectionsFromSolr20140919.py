# getCollectionsFromSolr20140919 revised to cover several cases and to report progress
#  VT CS4984, Computational Linguistics, by Xuan Zhang, Tarek Kanan, Edward Fox
import os

from sunburnt import SolrInterface

si = SolrInterface("http://jingluo.dlib.vt.edu:8080/solr")

# This is where you put the event name

eventQuery = "Texas_Fertilizer_Plant_Explosion"

#these are the query lists for Team A
eventQueryList = ["Texas_Fertilizer_Plant_Explosion", "Rain_at_Islip"]
# Commented out lines support the special handling when there are spaces in the event name.
# eventQuery = "Connecticut School Shooting"

# This is where you put the downloaded files
#root = 'D:\Test\EventCollections\SmallCollections'
# Or, for a Mac, use something like
#someone needs to change this part
root = '../Unit3/output'

# Create and execute a Solr query
words = eventQuery.split();
query = si.query(event=words[0])
for w in words[1:]:
    query = query.query(event = w)
response = query.execute()
# Or, for the case of spaces in the name:
#  response = si.query(event="Connecticut").query(event="School").query(event="shooting").execute()
tot = response.result.numFound

#print response.result.numFound
print tot, "documents found in collection [", eventQuery, "]\n"
print "Retrieving documents...\n"

response = si.query(event=eventQuery).paginate(0,tot).execute()
# Or, for the case of spaces in the name:
#  response = si.query(event="Connecticut").query(event="School").query(event="shooting").paginate(0,tot).execute()

i = 1
empties = 0
directory = root + os.sep + eventQuery

# Create a directory if necessary
if not os.path.exists(directory):
    os.makedirs(directory)

# Write the downloaded documents into local files
for res in response:
    content = res['content'][0]

    # Filter out empty files
    if len(content) > 0 :
        f = open(directory + os.sep + str(i) + ".txt","w")
        f.write(content.encode("utf-8"))
        f.close()
        if i % 300 == 0:
            print i, " files downloaded out of ", tot
        i+=1
    else:
        empties+=1

print "\nDownloading Complete! ", i-1, "files downloaded out of", tot, "items"
print empties, "Empty documents filtered"