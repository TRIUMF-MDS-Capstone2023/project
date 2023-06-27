# Exploratory Data Analysis 

As part of our analysis, we conducted exploratory data analysis (EDA) on the raw data from the 2021A NA62 experiment, specifically Run 11100. Our analysis involved both the events data and the hits data, serving the purpose of exploration and discovery.

### EDA on the Events Data

In the events data, there are a total of 2,376,174 events. Among all the events, 2,160,219 events are muons, while 215,955 events are pions. Notably, the total number of pions is approximately 10% of the total number of muons. When examining the `track_momentum` variable within the events data, we observed that the minimum value is 45.9 GeV/c, and the highest value is 75.5 GeV/c. From the histograms shown in [Fig. 1](eda_momentum_distribution) below, it can be seen that there are more muons within the higher momentum range compared to pions, especially from 60 to 70 GeV/c. 

```{figure} ../../../../../eda_momentum_distribution.png 
:name: eda_momentum_distribution

Track momentum distribution of muons and pions from events data
```
