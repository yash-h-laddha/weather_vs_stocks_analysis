import duckdb
import pandas as pd

df = pd.read_parquet("joined_data.snappy.parquet")
df.to_csv("joined.csv", index=False)

df1 = duckdb.sql("""
    SELECT AVG(close) AS avg_close, MONTH(date) AS month, YEAR(date) AS year 
    FROM 'joined.csv' 
    GROUP BY(YEAR(date), MONTH(date))
    ORDER BY month, year
""")

df1.to_csv('avg_closing_price_per_month.csv')

# avg closing price per week
df2 = duckdb.sql("""
    SELECT AVG(close) AS avg_close, WEEK(date) AS weekdate
    FROM 'joined.csv' 
    GROUP BY(WEEK(date))
    ORDER BY weekdate
""")
df2.to_csv('avg_closing_price_per_week.csv')

# average monthly trading volume
df3 = duckdb.sql("""
    SELECT AVG(volume) AS avg_volume, MONTH(date) AS month, YEAR(date) AS year 
    FROM 'joined.csv' 
    GROUP BY(YEAR(date), MONTH(date))
    ORDER BY month, year
""")
df3.to_csv('avg_monthly_trading_volume.csv')

# average weekly trading volume
df4 = duckdb.sql("""
    SELECT AVG(volume) AS avg_volume, WEEK(date) AS weekdate
    FROM 'joined.csv' 
    GROUP BY(WEEK(date))
    ORDER BY weekdate
""")
df4.to_csv('avg_weekly_trading_volume.csv')

df5 = duckdb.sql("""
    SELECT 
        WEEK(date) AS weekdate,
        SUM(CASE WHEN week_day = 1 THEN volume END) - 
        SUM(CASE WHEN week_day = 5 THEN volume END) AS volume_diff
    FROM 
        (SELECT volume, date, DAYOFWEEK(date) AS week_day FROM 'joined.csv' WHERE DAYOFWEEK(date) IN (1, 5))
    GROUP BY(WEEK(date))
    ORDER BY weekdate
""")
df5.to_csv('mon_to_fri_trading_difference.csv')

# std of returns per week and weather per week
df6 = duckdb.sql("""
    SELECT STDDEV(close) AS stdev_close, AVG(total_PRCP) as avg_prcp, AVG(total_SNOW) as avg_snow, WEEK(date) AS weekdate
    FROM 'joined.csv' 
    GROUP BY(WEEK(date))
    ORDER BY weekdate
""")

df6.to_csv('std_of_returns_per_week_and_weather_per_week.csv')

