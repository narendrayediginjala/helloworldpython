import pyspark
from pyspark import SparkContext

sc = SparkContext()



df = sc.textFile("gs://sparknarendra/offense_codes.csv")

print("line count is %s"%df.count())
print("Some Sample data is as below")
print(df.first())
