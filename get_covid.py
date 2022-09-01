from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName('GCSFilesRead').getOrCreate()
df = spark.read.option("header",True).csv("source/covid.csv")
df.show()
df.write.json('result/shofa')

#intinya program ini akan copy file csv dari source/covid.csv ke result/<nama> dengan format json
