from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, col, to_date, weekofyear, month

spark = SparkSession.builder.appName("OptimizedJoin").getOrCreate()

nasdaq_df = spark.read.parquet("nasdaq.snappy.parquet").select("date", "ticker", "open", "high", "low", "close", "volume")

weather_df = spark.read.parquet("weather.snappy.parquet").select("DATE", "PRCP", "SNOW", "TMAX", "TMIN", "NAME")

industry_data = spark.read.csv("nasdaq_industries.csv", header=True, inferSchema=True)



nasdaq_df = nasdaq_df.withColumn("date", to_date(col("date")))

nasdaq_df = nasdaq_df.withColumn("week_number", weekofyear(col("date")))

nasdaq_df = nasdaq_df.withColumn("month", month(col("date")))


industry_data = industry_data.drop("Last Sale", "Net Change", "% Change", "Market Cap", "Country", "IPO Year", "Volume")

merged_data = nasdaq_df.join(industry_data, on=nasdaq_df["ticker"] == industry_data["Symbol"], how="left")

merged_data = merged_data.drop("Symbol")

agg_weather_df = weather_df.groupBy("DATE").agg(sum("PRCP").alias("total_PRCP"), sum("SNOW").alias("total_SNOW"), avg("TMAX").alias("avg_TMAX"), avg("TMIN").alias("avg_TMIN"))

joined_df = nasdaq_df.join(agg_weather_df, nasdaq_df.date == agg_weather_df.DATE, how="inner").drop(agg_weather_df.DATE)

ordered_cols = ["date"] + [col for col in joined_df.columns if col != "date"]
joined_df = joined_df.select(*ordered_cols)


output_path = "joined_data.snappy.parquet"
joined_df.coalesce(1).write.mode("overwrite").parquet(output_path)

print(f"Join completed! File saved at {output_path}")