from pyspark.sql import sparksession

spark = sparksession.builder.appName("Testing").getOrCreate()

df = spark.read.format("csv").load("gs://sparknarendra/offense_codes.csv")

print("line count is %s",df.count())
