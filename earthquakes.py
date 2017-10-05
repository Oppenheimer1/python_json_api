
#enables us to open the url to retrieve the information we need
import urllib2
#enables us to manipulte the json information
import json

def printResults(info):
  # Use the json module to load and process the information
  theEarthquakeInfo = json.loads(info)

  # displays earthquakes with magnidude of 4.5 or greater
  for i in theEarthquakeInfo["features"]:
    if i["properties"]["mag"] >= 4.5:
      print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]

def main():

  # create a variable to hold the source URL
  # This is the feed shows all the earthquakes with 4.5 or greater magnitudes
  urlInfo = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"

  # Open the URL and read's the info
  webInfo = urllib2.urlopen(urlInfo) #calls the urlopen function on the url to get the information
  print (webInfo.getcode()) #prints out the result code to make sure we're getting a result code of 200
  if (webInfo.getcode() == 200):
    info = webInfo.read()     #if the code comes back as 200 then get the json info from the website
    printResults(info) # prints out the results
  else:
    print "Houston we have a problem. I dunno what it is yet but we have a problem" + str(webInfo.getcode())


if __name__ == "__main__":
  main()