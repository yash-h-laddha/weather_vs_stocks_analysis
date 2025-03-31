# 405 Final Project: Cloudy with a Chance of Trades

This project aims to identify the relationship between weather—specifically, precipitation and snow levels—on Nasdaq trading volumes and closing prices.

### <b>tl;dr:</b>
To run the pipeline, git clone this repo to your local machine and download the 3 data files [here](https://drive.google.com/drive/folders/1bkWz8vMf-Gt-6Eu7kJHgzwyFsPrrS_sm?usp=sharing). Use `bash run_script.sh` on your local terminal to run the entire pipeline in one command.


The Tableau visualization can be accessed through [this link](https://public.tableau.com/app/profile/jane.lee6070/viz/StockMarketandWeather/WEATHERSTOCKMARKETANALYSIS). 

<br>

## Full README:

### Pre-Processing
We pre-processed our data before loading it into our pipeline. We filtered our data to only include data points from the year 2016 using the *spark_preprocessing.ipynb* notebook, and yielded two datasets in parquet format (weather.snappy.parquet and nasdaq.snappy.parquet). A third dataset was added later.

### Data
You can skip the pre-processing step and directly download the data files through [this link](https://drive.google.com/drive/folders/1bkWz8vMf-Gt-6Eu7kJHgzwyFsPrrS_sm?usp=sharing).
<br>
The original unprocessed data is available further down.
<br>


### Step 1: Data Manipulation
The *pyspark_script.py* file is used to run the data manipulation code, which includes some column removals, transformations, and joins.
<br>

### Step 2: Aggregations
The *queries_script.py* file is used to run the data aggregation code, which includes DuckDB queries that output 6 CSV files to be used for our Tableau visualizations.
<br>

### Step 3: The One Line to Run Them All
Once all the required data files are downloaded and available, you can skip manually doing Steps 1 & 2 by simply running the *run_script.sh* file by using the following command on your local command line:
`bash run_script.sh`
<br>

### Step 4: Visualization
Step 3 will give you 6 CSV files as outputs. These files were visualized to draw our conclusions.

We used Tableau Public for our visualizations. Our dashboard can be accessed through [this link](https://public.tableau.com/app/profile/jane.lee6070/viz/StockMarketandWeather/WEATHERSTOCKMARKETANALYSIS).


<br>

### Original Data

You can find the original sources to our data at the links below.

<b>[Global Daily Weather Data](https://data.opendatasoft.com/explore/dataset/noaa-daily-weather-data%40public/table/) </b> </br>
Same columns as in weather.snappy.parquet.<br>
GHCN_DIN: Global Historical Climatology Network Daily Identification Number<br>
DATE (year-month-day)<br>
PRCP: precipitation (tenths of mm)<br>
SNOW: snowfall (mm)<br>
TMAX: daily maximum temperature (Cº)<br>
TMIN: daily minimum temperature (Cº)<br>
NAME: weather station name<br>
ELEVATION: elevation (meters)<br>
COUNTRY_CODE: two-letter country code<br>
COORD: latitude and longitude of the station, in decimal degrees<br>

<b> [Nasdaq data](https://data.nasdaq.com/tables/WIKI-PRICES/export?api_key=YOURAPIKEY) </b> 
<br>
To download this, you will need to sign up for an API key.<br> 
Same columns as in nasdaq.snappy.parquet.<br>
ticker: stock ticker<br>
date (year-month-day)<br>
open: first price that the stock was traded on that day<br>
high: highest price that the stock reached on that day<br>
low: lowest price that the stock reached on that day<br>
close: last price that the stock was traded on that day<br>
volume: total number of shares traded on that day<br>
ex-dividend: cash dividend per share paid by the company on that day, adjusted for stock splits<br>
split_ratio: ratio of a stock split that occurred on that day<br>
adj_open: open, adjusted for stock splits and dividends<br>
adj_high: high, adjusted for stock splits and dividends<br>
adj_low: low, adjusted for stock splits and dividends<br>
adj_close: close, adjusted for stock splits and dividends<br>
adj_volume: volume, adjusted for stock splits<br>

<b> [Nasdaq Industries Data](https://www.nasdaq.com/market-activity/stocks/screener?page=1&rows_per_page=25)
</b>

Same columns as in nasdaq_industries.csv.<br>
Symbol: stock ticker<br>
Name: company name<br>
Last Sale: most recent price at which the company's stock was traded<br>
Net Change: difference between the last sale price and the previous day's closing price​<br>
% Change: percentage change in the stock's price compared to the previous day's closing price<br>
Market Cap: total market value of a company's outstanding shares<br>
Country: country where the company is headquartered.<br>
IPO Year: year the company first offered its shares to the public through an Initial Public Offering<br>
Sector: company sector<br>
Industry: company industry

<br>

### Further Work / To Do

- Testing GCP integration

<br>

### Credits

This project was made by: <br>
[Alyssa Fontaine](https://www.linkedin.com/in/alyssa-mfontaine/) <br>
[Eliz Zhou](https://www.linkedin.com/in/elizzhou/) <br>
[Jane Lee](https://www.linkedin.com/in/jajanelee/) <br>
[Joshua Bastin](https://www.linkedin.com/in/joshua-bastin/) <br>
[Megan Bennett](https://www.linkedin.com/in/megan-e-bennett/) <br>
[Yash Laddha](https://www.linkedin.com/in/yash-h-laddha/)
