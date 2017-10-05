
#enables us to open the url to retrieve the information we need
import urllib2
#enables us to manipulte the json information
import json

def main():

# create a variable to hold the source URL
# This is the feed shows all the earthquakes for the past day with magnitudes greater then 4.5
urlInfo = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"

# Open the URL and read's the info
  webInfo = urllib2.urlopen(urlInfo) #calls the urlopen function on the url to get the information
  print (webInfo.getcode()) #prints out the result code to make sure we're getting a result code of 200
  if (webInfo.getcode() == 200):
    data = webInfo.read()     #if the code comes back as 200 then get the json info from the website
    # prints out the results
    printResults(data)
  else:
    print "Houston we have a problem. I dunno what it is yet but we have a problem" + str(webInfo.getcode())


 if __name__ == "__main__":
  main()