'''
Code for the 'Fetching Data from the Altmetric API' instructional video. 
Produced for STEM Fellowship's Big Data Challenge.
'''

import requests
import json

api = "http://api.altmetric.com/v1/doi/"
doi = "10.1101/SQB.1953.018.01.020" # a paper by Watson and Crick

response = requests.get(api + doi) # this is the request
print(response.status_code) 
# checking to see whether our response worked out
# you'll likely encounter one of these:
    # 200 - everything went okay <- what you're hoping for!
    # 404 - not found/no data available

# but you might also run into these
    # 301 - server redirect
    # 401 - you're not authenticated
    # 400 - bad request
    # 403 - resource being accessed is forbidden

result = response.json() # converts the data you've fetched to dictionary format
type(result) # should return dict
sorted(result.keys()) # having a look at the kind of altmetric information we're getting
# result.keys() is sufficient for this but I use sorted() to alphabetically sort output

result # prints *all* our altmetrics out into the console
# usually not recommended to do it that way though...

# let's save the results to a file instead
# got to convert it to a string first
result_string = json.dumps(result, sort_keys = True, indent = 4) # converts dict to string
with open('results.txt', 'w') as f:
    f.write(result_string) # writes our results to a txt file in the current working directory
    
# if you want to check your current working directory first
import os
os.getcwd() # get current wd
os.chdir('/Users/Me/Desktop') # change wd

# using the time library to stagger loop functionality
# if you're fetching multiple records through a loop, Altmetric recommends making a maximum of one request per second
import time
counter = 5
while counter > 0:
  counter = counter - 1
  print('Currently at ', counter, '. Will subtract again in three seconds.')
  time.sleep(3)
