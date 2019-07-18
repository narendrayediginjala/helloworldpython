import pyspark
from pyspark import SparkContext

sc = SparkContext()



df = sc.textFile("gs://sparknarendra/crime.csv")

print("line count is %s"%df.count())
print("Some Sample data is as below")
print(df.take(10))
