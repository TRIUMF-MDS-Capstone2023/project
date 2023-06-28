# Engineered Features

The raw data only comprises of the coordinates of the hit positions for each event, which represent the recorded positions on a grid of PMTs relative to the coordinates of the grid. These positions correspond to the detection of light photons by photomultiplier tube ("PMT") tubes.

To enable better model fitting, we have a number of engineered features that aims to extract more meaningful information from the hit positions. In our analyses,  we use these 18 engineered features based on these positions:

1. `total_in_time_hits`: total number of in-time hits in each event
2. `x_aligned_min`: minimum hit position realigned by subtracting track position x in each event
3. `x_aligned_max`: maximum hit position realigned by subtracting track position x in each event
4. `y_aligned_min`: minimum hit position realigned by subtracting track position y in each event
5. `y_aligned_max`: maximum hit position realigned by subtracting track position y in each event
6. `x_aligned_width`: maximum hit position x minus minimum hit position x in each event
7. `y_aligned_witdh`: maximum hit position y minus minimum hit position y in each event
8. `hit_distance_min`: minimum distance between hit position and track position in each event
9. `hit_distance_max`: maximum distance between hit position and track position in each event
10. `hit_distance_mean`: mean distance between hit position and track position in each event
11. `hit_distance_median`: median distance between hit position and track position in each event
12. `hit_distance_q25`: 25% percentile distance between hit position and track position in each event
13. `hit_distance_q75`: 75% percentile distance between hit position and track position in each event
14. `hit_distance_rms`: root mean squared distance between hit position and track position in each event
15. `hull_area`: hull area of the convex hull
16. `hull_diameter`: the longest line among all the points
17. `hull_diff_width_diameter`: the absolute difference between hull_diameter and hull_width
18. `hull_width`: closest distance of the parallel lines that encloses all points

There are also a number of features related to fitted radius that are not used in the final analyses. These can be found here:

1. `radius_fit_lsq`: radius fit using a "standard" version of least square circle fit
2. `radius_fit_lsq_err`: residual/error from the fitted radius from `radius_fit_lsq`
3. `radius_fit_lsq_hyper`: radius fit using a "hyperaccuracy" version of least square circle fit {cite}`KANATANI20112197`
4. `radius_fit_lsq_hyper_err`: residual/error from the fitted radius from `radius_fit_lsq_hyper`
5. `radius_fit_riemann_swfla`: radius fit using Riemann circle fit, SWFL version A {cite}`STRANDLIE200095`
6. `radius_fit_riemann_swfla_err`: residual/error from the fitted radius from `radius_fit_riemann_swfla`
7. `radius_fit_svd_pratt`: radius fit using Pratt's algebraic circle fit {cite}`Pratt_2002`
8. `radius_fit_svd_pratt_err`: residual/error from the fitted radius from `radius_fit_svd_pratt`
9. `radius_fit_svd_taubin`: radius fit using Taubin's algebraic circle fit {cite}`Taubin_1991`
10. `radius_fit_svd_taubin_err`: residual/error from the fitted radius from `radius_fit_svd_taubin`
11. `radius_fit_svd_hyper`: radius fit using algebraic circle fit with "hyperaccuracy" by [Chernov](https://people.cas.uab.edu/~mosya/cl/HyperSVD.m)
12. `radius_fit_svd_hyper_err`: residual/error from the fitted radius from `radius_fit_svd_hyper`
13. `radius_fit_kmh`: radius fit using a consistent circle fit by Kukush, Markovsky and van Huffel {cite}`Markovsky_2004`
14. `radius_fit_kmh_err`: residual/error from the fitted radius from `radius_fit_kmh`
