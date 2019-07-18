import logging
import os
import cloudstorage as gcs
import webapp2

f = gcs.open("gs://sparknarendra/crime.csv","r+")
count = 0

for line in f.readlines():
  count += 1
  
print("line count is %s",count)
