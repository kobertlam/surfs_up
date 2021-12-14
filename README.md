# Surfs_up

## Overview of the statistical analysis:
W. Avy wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

The following tools are being used: Python, SQLite, and SQLAlchemy.

## Results:
![Jun Results](Resources/June_Results.png)
![Dec Results](Resources/Dec_Results.png)
- There are 1700 and 1517 temperature records collected for the month of June and Decemeber in Oahu.
- For June, the average temperature is 74.94°F, and the temperature range is 64-85°F.
- For December, the average temperature is 71.04°F, and the temperature range is 56-83°F.

## Summary:
- Based on the results above, the average temperature is 74.94°F and 71.04°F for June and December respectively, which is very suitable for the surf and ice cream shop business.
- In addition, we can also perform the following queries to gather more weather data for June and December:
    1) Write a query that filter the Measurement table to retrieve the precipitation (`Measurement.prcp`) for the month of June and December, and provide the summary statistics for June and Decemeber.
    2) Write a query that filter the Station table to retrieve a weather station which is closest to the location W. Avy want to open the surf shop, and then write another query from the Measurement table to retrieve precipitation for the month of Jun and Dec for that particular weather station.
