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

```{figure} ../../../../figures/eda_radius_vs_momentum_theoretical.png
:name: eda_theoretical_radius_vs_momentum

Theoretical ring radius vs. track momentum from events data
```

At the stage of performing the EDA, our focus was to examine the behaviour of our data without fitting any models. Since the events data includes the ring radius predicted by the state-of-the-art method (SOTA),we plotted the relationship between the ring radius from SOTA vs. the track momentum in [Fig. 4](eda_theoretical_radius_vs_momentum) for investigation and comparison purpose. The plot reveals that the distribution of the predicted ring radius exhibits a wider spread and contains a number of outliers. Consequently, our objective is to develop models that can accurately predict the ring radius with a narrower distribution, thus achieving improved precision and reducing the occurrence of outliers.

```{figure} ../../../../figures/eda_radius_vs_momentum_sota.png
:name: eda_sota_radius_vs_momentum

SOTA ring radius vs. track momentum from events data
```

To further investigate the data, we plotted the track positions for both muons and pions. The resulting visualizations are shown in [Fig. 5](eda_muon_track_position) and [Fig. 6](eda_pion_track_position). 

In [Fig. 5](eda_muon_track_position), it is evident that pions display a wider distribution of y-coordinates, ranging approximately from -100 to 100. On the other hand, muons exhibit a narrower y-coordinate distribution, spanning from around -50 to 50. This disparity suggests that pions tend to have a greater variation in their vertical track positions compared to muons.

Additionally, [Fig. 5](eda_muon_track_position) and [Fig. 6](eda_pion_track_position) reveal differences in the x-coordinate distributions between muons and pions. Muons demonstrate a relatively narrower x-coordinate distribution compared to pions. This observation indicates that muons tend to be more tightly clustered along the horizontal axis compared to pions.

By visualizing and comparing the track positions of muons and pions, we gain more insights into their distinct spatial characteristics.

```{figure} ../../../../figures/eda_muon_track_position.png
:name: eda_muon_track_position

2D Histogram showing track position distribution of muons
```

```{figure} ../../../../figures/eda_pion_track_position.png
:name: eda_pion_track_position

2D Histogram showing track position distribution of pions
```

### EDA on the Hits Data 

There are 99,397,075 hits in the hits data. Among these hits, there are 41,003,172 in-time hits when using a cut-off of 0.5 ns for the `chod_delta` variable. To conduct the EDA, we filtered out the out-of-time hits and performed analysis on the in-time hits data only. 

To analyze the distribution of hit positions, we plotted 2D histograms to visualize the hit positions for both muons ([Fig. 7](eda_muon_hit_position_all)) and pions [Fig. 8](eda_pion_hit_position_all). These hit positions represent the positions of photon hits that collectively form the "ring image". For this reason, we expect to observe distinguishable differences in ring radii between muons and pions. However, a distinct disparity in the ring radii between muons and pions is not apparent from [Fig. 7](eda_muon_hit_position_all) and pions [Fig. 8](eda_pion_hit_position_all). 

```{figure} ../../../../figures/eda_hit_position_muon_all.png
:name: eda_muon_hit_position_all

2D Histogram showing hit position distribution of muons
```

```{figure} ../../../../figures/eda_hit_position_pion_all.png
:name: eda_pion_hit_position_all

2D Histogram showing hit position distribution of pions
```

To investigate the distinction in ring radii between muons and pions more effectively, we focused on a specific track momentum range of 20 to 25 GeV/c. This range was chosen because it exhibits a clear separation in ring radii between the two particle types, as demonstrated in [Fig. 3](eda_theoretical_radius_vs_momentum).

By examining the hit positions within this track momentum range, we plotted [Fig. 9](eda_muon_hit_position_subset) and pions [Fig. 10](eda_pion_hit_position_subset) to visualize the hit distributions for muons and pions, respectively. Notably, in these plots, the hit positions for muons exhibit a larger ring radius compared to pions. This finding agrees with the observed distinction in ring radii illustrated in [Fig. 3](eda_theoretical_radius_vs_momentum) in the specified track momentum region. From this observation, we believe that we need to select the correct momentum region for our model to yield the best separation between muons and pions. 


```{figure} ../../../../figures/eda_hit_position_muon_subset.png
:name: eda_muon_hit_position_subset

2D Histogram showing hit position distribution of muons between 20 and 25 GeV/c
```

```{figure} ../../../../figures/eda_hit_position_pion_subset.png
:name: eda_pion_hit_position_subset

2D Histogram showing hit position distribution of pions between 20 and 25 GeV/c
```
### Conclusion 

During the EDA on the data from the 2021A NA62 experiment, we examined the events and hits data to gain insights into the distribution of muon and pion data. The EDA showed distinctions between muons and pions in their track momentum, number of hits per event and track positions. The predicted ring radius from the state-of-the-art method displayed a wider distribution with outliers compared to the theoretical curves. It was also found that the hit positions for muons form a larger ring radius compared to pions for a selected momentum range between 20 and 25 GeV/c. From this observation, we believe that the optimal separation between muons and pions in our model should be achieved by selecting the proper momentum region.