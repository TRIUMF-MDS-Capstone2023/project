# Exploratory Data Analysis 

As part of our analysis, we conducted exploratory data analysis (EDA) on the raw data from the 2021A NA62 experiment, specifically Run 11100. Our analysis involved both the events data and the hits data, serving the purpose of exploration and discovery.

### EDA on the Events Data

In the events data, there are a total of 2,376,174 events. Among all the events, 2,160,219 events are muons, while 215,955 events are pions. Notably, the total number of pions is approximately 10% of the total number of muons. When examining the `track_momentum` variable within the events data, we observed that the minimum value is 45.9 GeV/c, and the highest value is 75.5 GeV/c. From the histograms shown in [Fig. 1](eda_momentum_distribution) below, it can be seen that there are more muons within the higher momentum range compared to pions, especially from 60 to 70 GeV/c. 

```{figure} ../../../../figures/eda_momentum_distribution.png 
:name: eda_momentum_distribution

Track momentum distribution of muons and pions from events data
```
We also plotted the number of hits per event for muons and pions as displayed in [Fig. 2](eda_number_of_hits_distribution). From the distribution it can be seen that the shape and spread of the distribution for both muons and pions are left skewed, with the mean being approximately 42 hits per event. 

```{figure} ../../../../figures/eda_number_hits.png 
:name: eda_number_of_hits_distribution

Histogram showing distribution of number of hits per event for muons and pions from events data
```

To further investigate the behaviour of our data, we have also computed the relationship between the ring radius and the track momentum. Since the theoretical ring radius is calculated from the track momentum and mass of the particle, an ideal relationship between the predicted ring radius and the track momentum should be similar to the plot shown in [Fig. 3](eda_theoretical_radius_vs_momentum). 

```{figure} ../../../../eda_radius_vs_momentum_theoretical.png
:name: eda_theoretical_radius_vs_momentum

Theoretical ring radius vs. track momentum from events data
```

At the stage of performing the EDA, our focus was to examine the behaviour of our data without fitting any models. Since the events data includes the ring radius predicted by the state-of-the-art method (SOTA),we plotted the relationship between the ring radius from SOTA vs. the track momentum in [Fig. 4](eda_theoretical_radius_vs_momentum) for investigation and comparison purpose. The plot reveals that the distribution of the predicted ring radius exhibits a wider spread and contains a number of outliers. Consequently, our objective is to develop models that can accurately predict the ring radius with a narrower distribution, thus achieving improved precision and reducing the occurrence of outliers.

```{figure} ../../../../eda_radius_vs_momentum_sota.png
:name: eda_sota_radius_vs_momentum

SOTA ring radius vs. track momentum from events data
```

