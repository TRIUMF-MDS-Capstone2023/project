# CALORICH AI

## Introduction

WIP

## Installation

(TODO: Include a Conda environment)

## Dataset

The dataset we are using is `CaloRICH_Run11100_CTRL_v1.h5`, in [H5F5](https://www.loc.gov/preservation/digital/formats/fdd/fdd000229.shtml) format.

For easier access, the raw dataset is also processed and saved as [Parquet](https://parquet.apache.org/) files.

To obtain the necessary files, after placing the `CaloRICH_Run11100_CTRL_v1.h5` file at `data/` file, run:

```bash
make
```

Make sure there are `hdf5`, `polars`, `numpy`, and `termcolor` in the Python environment.
