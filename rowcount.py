f = open("gs://sparknarendra/crime.csv","r+")
count = 0

for line in f:
  count += 1
  
print("line count is %s",count)
