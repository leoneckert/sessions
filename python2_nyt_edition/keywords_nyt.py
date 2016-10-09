# On top of your script is where modules ("libraries") are imported.
# Some of them you have to download/install (using "pip"), 
# but there are many that just come with python
import requests # we use this to get actual data from the www
import json # data from the web comes a text. with thos module we format the text to be more useful.
from pprint import pprint # this is a classic, to print things nicer and get easier oversight.
import sys # i believe this stands for 'system'? often used especially for the two things we are using it for in this script

#here starts the main section of our code

# the next three line check if a search query was supplied,
# gives advice if not, and also exits the script. 
if len(sys.argv) == 1:
    print "Use a search query as the second argument."
    sys.exit()

# API's will ask you to sign up and authenticate with an API_key
# don't upload this key to github or anywhere else. 
# ask me (Leon) for best practise advice for avoiding this.
api_key = "[API KEY HERE]"

# get the query we type on the command line/terminal
our_query = sys.argv[1]
# bring query in right format
query_words = our_query.split()
query = "+".join(query_words)

# form request url
base_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?"
# add query and api_key:
url = base_url + "q=" + query + "&api-key=" + api_key

# get data from the www in string format
resp = requests.get(url)
# format string into a parseable object using json module
data = json.loads(resp.text)

# parse the json object/dictionairy for the information we want.
# the object normally conatains dictionairies (key:value) and lists (lots of values)
# here we use a for-loop to cycle through all the articles in the response
for article in data["response"]["docs"]:
    # we use try/except because some articles might not have the data
    # we ask for. this avoids errors to be thrown.
    try:
        # the [:4] at the end slices the string to give us only the first four characters (the year)
        print article["pub_date"][:4]
        print article["headline"]["main"] 
        # this is just a little divider that we print 
        print "-"*50
    except: TypeError