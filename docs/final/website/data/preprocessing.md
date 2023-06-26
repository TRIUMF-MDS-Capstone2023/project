# Preprocessing

Time is seriously limited in this project. To save training and loading time, we rely on preprocessed [Parquet files](https://parquet.apache.org/), to do preprocessing.

The [`scripts/` folder](https://github.com/TRIUMF-MDS-Capstone2023/project/tree/main/scripts) contains all of the respective preprocessing scripts.

To run the analysis, after placing the H5 files at `data/` folder, run:

```bash
make
```

This would preprocess the H5 files and place the generated files, required to do the analysis, at `data/` folder.

There are a number of generated files that are defined in the [Makefile](https://github.com/TRIUMF-MDS-Capstone2023/project/blob/main/Makefile) but are not used in the final report. To generate _all_ of those, run:

```bash
make full
```

```{warning}
This `make full` is *very* slow and generates around 400GB of intermediate files!
```

To remove the generated files, run:

```bash
make clean
```
