import urllib2
import json

def main():

# create a variable to hold the source URL
# This is the feed shows all the earthquakes for the past day with magnitudes greater then 4.5
urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"