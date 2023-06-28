# Preprocessing

Time is seriously limited in this project. To save training and loading time, we rely on preprocessed [Parquet files](https://parquet.apache.org/), to do preprocessing.

The [`scripts/` folder](https://github.com/TRIUMF-MDS-Capstone2023/project/tree/main/scripts) contains all of the respective preprocessing scripts, and the generation was orchestrated by the [`Makefile`](https://github.com/TRIUMF-MDS-Capstone2023/project/blob/main/Makefile).

The important files are highlighted as follows:

# [`data_extract_events.py`](https://github.com/TRIUMF-MDS-Capstone2023/project/blob/main/scripts/data_extract_events.py)

The script extracts events from the source file. It filters out the events labeled as `muon` and `pion`, and exports as `events.parquet` for each dataset.

For each event, it also calculates the theoretical mass (`mass`) and the corresponding calculated ring radius (`ring_radius_cal`) using the theoretical mass and the measured momentum.

# [`data_extract_hits.py`](https://github.com/TRIUMF-MDS-Capstone2023/project/blob/main/scripts/data_extract_hits.py)

The script extracts hits from the source file. It outputs a `hits.parquet` for each dataset.

Using the raw `x` and `y`, it performs the following operations:

- "Adjusting" the `x_raw` and `y_raw` to be `x_adjusted` and `y_adjusted`, using the `disk_id` to adjust the position depending whether it is on the Jura side or the Salève side; and
- "Aligning" the `x_adjusted` and `y_adjusted` to be `x_aligned` and `y_aligned`, by offsetting the expected track position (`track_pos_x` and `track_pos_y`)

The `x_aligned` and `y_aligned` are also used to calculate a series of `hit_distance`, which can be understood as the distance between the hit and the track position.

`chod_delta` is also calculated as the difference between the `hit_time` and the `chod_time`.

# [`data_features.py`](https://github.com/TRIUMF-MDS-Capstone2023/project/blob/main/scripts/data_features.py)

The script engineers features for each events and corresponding hits. For each configurable cut-off time, it outputs a corresponding `events_with_hit_features*.parquet`.

For each event, the in-time hits are identified (by using the _absolute_ value of `chod_delta` smaller than the cut-off time, defaulted to 0.5ns). The in-time hits then have the following features calculated:

- `hit_distance_*`: the parameters correspond to some summary statistics corresponding to the hit distances, e.g., min, max, quantiles, and RMS value;
- `hull_*`: the parameters related to the [convex hull](https://en.wikipedia.org/wiki/Convex_hull) formed by the in-time hits, e.g., area, width and diameter; and
- `radius_fit_*`: experimental parameters related to the fitted radius using some published algorithms, provided by the [`circle-fit` library](https://github.com/AlliedToasters/circle-fit)

# [`data_sample.py`](https://github.com/TRIUMF-MDS-Capstone2023/project/blob/main/scripts/data_sample.py)

The script randomly samples the same number of examples in each bin of track_momentum (bin size = 1 Gev), with the number of examples is equal to the minimum number of examples in all the bins. It outputs the `sampled_event_ids*.parquet` for each of the defined `min_momentum` and `max_momentum` ranges.

# [`utils.py`](https://github.com/TRIUMF-MDS-Capstone2023/project/blob/main/scripts/utils.py)

The script holds some of the utility functions used by the scripts. One of the important functions is `compute_composite_event_id` (and the complement `decompose_composite_event_id`), in which we pack the composite IDs for each event (i.e., `run_id`, `burst_id`, `event_id`, `track_id`) as an unsigned 64-bit integer (`UInt64`).

In the bit-packing scheme, we assume that the `run_id` and `event_id` are smaller than 16,777,216 (2 ^ 24); where the `burst_id` and `track_id` are stored with 11 bits and 4 bits respectively.
