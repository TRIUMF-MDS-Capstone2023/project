# Engineered Features

The raw data only comprises the x and y hit positions for each event, which represent the recorded positions on a grid of PMTs relative to the coordinates of the grid. These positions correspond to the detection of light photons by photomultiplier tube ("PMT") tubes. To enhance the informative value of the data and enable better model fitting, we aimed to engineer features that extract more meaningful information from the x and y hit positions. Consequently, we created 18 engineered features based on these positions:

1. `total_in_time_hits`: total number of in-time hits in each event
1. `x_aligned_min`: minimum hit position realigned by subtracting track position x in each event
1. `x_aligned_max`: maximum hit position realigned by subtracting track position x in each event
1. `y_aligned_min`: minimum hit position realigned by subtracting track position y in each event
1. `y_aligned_max`: maximum hit position realigned by subtracting track position y in each event
1. `x_aligned_width`: maximum hit position x minus minimum hit position x in each event
1. `y_aligned_witdh`: maximum hit position y minus minimum hit position y in each event
1. `hit_distance_min`: minimum distance between hit position and track position in each event
1. `hit_distance_max`: maximum distance between hit position and track position in each event
1. `hit_distance_mean`: mean distance between hit position and track position in each event
1. `hit_distance_median`: median distance between hit position and track position in each event
1. `hit_distance_q25`: 25% percentile distance between hit position and track position in each event
1. `hit_distance_q75`: 75% percentile distance between hit position and track position in each event
1. `hit_distance_rms`: root mean squared distance between hit position and track position in each event
1. `hull_area`: hull area of the convex hull
1. `hull_diameter`: the longest line among all the points
1. `hull_diff_width_diameter`: the absolute difference between hull_diameter and hull_width
1. `hull_width`: closest distance of the parallel lines that encloses all points
