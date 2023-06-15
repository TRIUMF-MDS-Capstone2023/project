# CALORICH AI

## Introduction

(WIP)

The proposal presentation and report can be found in [the `docs/proposal` folder](docs/proposal).

## Installation

The project runs on Python 3.9+, and a Conda environment file can be found at [`environment.yaml`](environment.yaml).

To run the code, first clone the repository with [Git](https://git-scm.org/):

```bash
git clone git@github.com:TRIUMF-MDS-Capstone2023/project.git calorich
cd calorich
```

After installing [Conda](https://github.com/conda/conda), create a Conda environment by:

```
conda env create -f environment.yaml
```

Alternatively, if you are using [Mamba](https://github.com/mamba-org/mamba), run:

```
mamba env create -f environment.yaml
```

To update a created environment to the latest version defined by the `environment.yaml`, run:

```
conda env update -f environment.yaml
```

or:

```
mamba env update -f environment.yaml
```

## Dataset

All the data files used are prepared and provided by the NA62 team from [TRIUMF](https://triumf.ca/). All of the data is from the 2021a experiments.

We are using a series of processed files, in [Parquet](https://parquet.apache.org/) format, instead of using the raw dataset directly. The data wrangling process includes creating engineered features. The relevant scripts are in [the `scripts/` folder](scripts/).

> Note: For access to the dataset, please reach out to TRIUMF.

### Main Dataset

The main dataset (or the `run` dataset) we are using is in [HDF5](https://www.loc.gov/preservation/digital/formats/fdd/fdd000229.shtml) format. The file was extracted from a full `RECO` stream.

To obtain the necessary files, after placing the aforementioned H5 file in [the `data/` folder](data/), run the following command in the Conda environment:

```bash
make run-all
```

It would create all the necessary Parquet files for the analyses involving the `run` dataset.

The main dataset (after cleaning) contains 2,376,174 events and 99,397,075 hits.

(Note that there is also `make run-full`, which also includes some of the obsolete data files derived from the main dataset.)

### Supplementary Dataset

The supplementary dataset (or the `pnn` dataset) is much larger, spanning several runs. However, since the events have been filtered, the label distribution is very different.

To generate the Parquet files associated with the `pnn` dataset, run the following command in the Conda environment:

```bash
make pnn-all
```

The supplementary dataset (after cleaning) contains 42,897,096 events and 1,635,601,517 hits.

(Note that, similar to the main dataset, there is also `make pnn-full`, which also includes some of the obsolete data files associated with the supplementary dataset.)

### Clean-up

To clean up the generated Parquet files, run:

```bash
make clean
```

Rest assured that it would _not_ remove the raw H5 files.

## Run the Model

(WIP)

## Copyright and Licensing

Unless otherwise specified, the code in this repository is covered under this copyright statement:

Copyright (c) 2023 Crystal Geng, Daniel Merigo, Kelvin Wong, Peng Zhang

The software and associated documentation files are licensed under [the MIT License](https://opensource.org/license/mit/). You may find a copy of the license at [`LICENSE.md`](LICENSE.md).

The report texts are licensed under [the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND 4.0) License](https://creativecommons.org/licenses/by-nc-nd/4.0/). A copy of the license can be found at [`LICENSE-CC-BYNCND.md`](LICENSE-CC-BYNCND.md).
