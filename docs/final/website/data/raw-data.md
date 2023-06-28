# Raw Data

The raw data we are working is prepared and provided by TRIUMF, and was stored in the [HDF5](https://www.loc.gov/preservation/digital/formats/fdd/fdd000229.shtml) format.

## Terminologies

Our dataset revolves around "events" and "hits". A "hit" refers to a signal in a detector (specifically, the RICH detector), while an "event" refers to a collection of hits attached to a physical process recorded.

A "track" refers to the path of a single particle in the experiment, and each "track" is uniquely identified by a set of 4 IDs (`run_id`, `burst_id`, `event_id`, and `track_id`). In our analyses, these are combined as one variable called the `composite_event_id`.

## Data Structure

### `Events` array

The `Events` "array" (technically a HDF5 Dataset) has the structure of:

```
DATATYPE H5T_COMPOUND {
    H5T_STD_I32LE "run_id";
    H5T_STD_I32LE "burst_id";
    H5T_STD_I64LE "event_id";
    H5T_STD_I32LE "track_id";
    H5T_IEEE_F32LE "track_momentum";
    H5T_IEEE_F32LE "chod_time";
    H5T_ARRAY { [ 2 ] H5T_IEEE_F32LE } "track_pos";
    H5T_IEEE_F32LE "ring_radius";
    H5T_ARRAY { [ 2 ] H5T_IEEE_F32LE } "ring_centre_pos";
    H5T_ARRAY { [ 5 ] H5T_IEEE_F32LE } "ring_likelihood";
    H5T_STD_I32LE "label";
}
```

When combined, `run_id`, `burst_id`, `event_id`, and `track_id` form an unique ID across the experiment.

`chod_time` gives the track time.

`track_momentum` and `track_pos` contains information about the track, provided by the STRAW detector.

`ring_radius`, `ring_centre_pos` and `ring_likelihood` columns are the outputs of the current state-of-the-art model used in the NA62 experiments. In particular, `ring_likelihood` is a set of probabilities given, corresponding to pion, muon, positron, kaon, and background.

The `label` is a label given by the calorimeter, indicating which particle it believed to be. It can show a different result from the `ring_likelihood` outputs.

### `Hits` array

`Hits` has the following structure:

```
DATATYPE H5T_COMPOUND {
    H5T_STD_I32LE "assigned_flag";
    H5T_STD_I32LE "disk_id";
    H5T_STD_I32LE "pmt_id";
    H5T_STD_I32LE "supercell_id";
    H5T_STD_I32LE "updowndisk_id";
    H5T_IEEE_F32LE "hit_time";
}
```

When combined, `disk_id`, `pmt_id`, `supercell_id` and `updowndisk_id` give the hit position, using the mapping defined by the [`rich_pmt_positions.dat`](https://github.com/TRIUMF-MDS-Capstone2023/project/blob/main/data/rich_pmt_positions.dat).

`assigned_flag` is an output of the current state-of-the-art NA62 algorithm.

`hit_time` contains the hit time, which is to be compared with `chod_time`.

### `Hitmapping` array

The `Hitmapping` array, each element containing an increasing unsigned integer, is exactly one unit longer than the `Hits` array, which is used to map the "event" and corresponding "hits" to that event.

The i-th event is associated with the hits, within the sequence starting from the i-th `Hitmapping` value, and up to (not including) the (i+1)-th `Hitmapping` value. For example, for a `Hitmapping` of values 0, 3, 7, 10, it would mean that:
- The 0<sup>th</sup> event is associated with the 0<sup>th</sup>, 1<sup>st</sup>, and 2<sup>nd</sup> (3 - 1) hits;
- The 1<sup>st</sup> event is associated with the 3<sup>rd</sup>, 4<sup>th</sup>, 5<sup>th</sup>, and 6<sup>th</sup> (7 - 1) hits;
- The 2<sup>nd</sup> event is associated with the 7<sup>th</sup>, 8<sup>th</sup>, and 9<sup>th</sup> (10 - 1) hits.

## Datasets

The two datasets we work with are from the 2021A run of the NA62 experiments, and share the exact same data structure.

### Main Dataset (`run`)

The main dataset was extracted from a full `RECO` stream, originally stored in the ROOT trees, getting the entirety of the Run 11100.

Counting only the pion and muon events, it contains 2,376,174 events and 99,397,075 hits.

### Supplementary Dataset (`pnn`)

The supplementary dataset is much larger, spanning several runs. However, since the events have been filtered, the label distribution is very different.

For the pion and muon events, there are 42,897,096 events and 1,635,601,517 hits.

## "Rings"

A function designed to display a ring, formed by the hits in a particular event, in a Jupyter notebook can be found at [`scripts/display_ring.py`](https://github.com/TRIUMF-MDS-Capstone2023/project/blob/main/scripts/display_ring.py).
