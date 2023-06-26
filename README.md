[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deploy final report](https://github.com/TRIUMF-MDS-Capstone2023/project/actions/workflows/deploy-final-report.yml/badge.svg)](https://github.com/TRIUMF-MDS-Capstone2023/project/actions/workflows/deploy-final-report.yml)

# CaloRICH AI

## Introduction

This GitHub repository includes the work associated with the 2023 CaloRICH AI Capstone Project, which was undertaken by Crystal Geng, Daniel Merigo, Kelvin Wong, and Peng Zhang as part of the Master of Data Science program at the University of British Columbia. The project was conducted in collaboration with scientists from [TRIUMF](https://www.triumf.ca/), Canada's leading particle accelerator center and a leading research facility in subatomic physics.

The purpose of this repository is to serve as a central hub for accessing general information about the project. You have the option to navigate directly to specific sections using the links provided below, or you can simply scroll down for more details.

- [CaloRICH AI](#calorich-ai)
  - [Introduction](#introduction)
  - [Executive Summary](#executive-summary)
  - [Installation](#installation)
  - [Dataset](#dataset)
    - [Main Dataset](#main-dataset)
    - [Supplementary Dataset](#supplementary-dataset)
    - [Clean-up](#clean-up)
  - [Copyright and Licensing](#copyright-and-licensing)

The summary of this project can be accessed via [the respective GitHub page](https://triumf-mds-capstone2023.github.io/project).

Other written materials, including the proposal, can be found in [the `docs/proposal` folder](docs/proposal).

## Executive Summary

The *CaloRICH AI* project is proposed by TRIUMF, Canada's national particle accelerator center, to improve the Ring-Imaging CHerenkov detector (RICH detector) particle identification performance. Our work this year is an extension of the *RICH AI* project [[den Hooff N *et al.*, 2022](https://triumf-mds-capstone2023.github.io/project/references.html#id11 "Van den Hooff N, Pandey R, Iyer M, and Jena S. Rich ai final report. 2022. Accessed: 2023-05-12. URL: https://triumf-capstone2022.github.io/richai/welcome.html.")], attempted by an MDS capstone team of similar goals last year.

The project dataset comes from the NA62 experiment at CERN, the European Organization for Nuclear Research, which involves a particle physics experiment designed to study rare decays of charged kaons. The capstone project aims to build a model to accurately classify a particle as a pion produced in a decay event. We aim to train models using the data from a subset of the 2021A NA62 experiments, which contains around 2.4 million decay events labeled by calorimeter [[Gil *et al.*, 2017](https://triumf-mds-capstone2023.github.io/project/references.html#id5 "E. Cortina Gil, E. Martin Albarran, E. Minucci, G. Nüssle, S. Padolski, P. Petrov, N. Szilasi, B. Velghe, G. Georgiev, V. Kozhuharov, L. Litov, T. Husek, K. Kampf, M. Zamkovsky, R. Aliberti, K. H. Geib, G. Khoriauli, K. Kleinknecht, J. Kunze, D. Lomidze, R. Marchevski, L. Peruzzo, M. Vormstein, R. Wanke, A. Winhart, M. Bolognesi, V. Carassiti, S. Chiozzi, A. Cotta Ramusino, A. Gianoli, R. Malaguti, P. Dalpiaz, M. Fiorini, E. Gamberini, I. Neri, A. Norton, F. Petrucci, M. Statera, H. Wahl, F. Bucci, R. Ciaranfi, M. Lenti, F. Maletta, R. Volpe, A. Bizzeti, A. Cassese, E. Iacopini, A. Antonelli, E. Capitolo, C. Capoccia, A. Cecchetti, G. Corradi, V. Fascianelli, F. Gonnella, G. Lamanna, R. Lenci, G. Mannocchi, S. Martellotti, M. Moulson, C. Paglia, M. Raggi, V. Russo, M. Santoni, T. Spadaro, D. Tagnani, S. Valeri, T. Vassilieva, F. Cassese, L. Roscilli, F. Ambrosino, T. Capussela, D. Di Filippo, P. Massarotti, M. Mirra, M. Napolitano, G. Saracino, M. Barbanera, P. Cenci, B. Checcucci, V. Duk, L. Farnesini, E. Gersabeck, M. Lupi, A. Papi, M. Pepe, M. Piccini, G. Scolieri, D. Aisa, G. Anzivino, M. Bizzarri, C. Campeggi, E. Imbergamo, A. Piluso, C. Santoni, L. Berretta, S. Bianucci, A. Burato, C. Cerri, R. Fantechi, S. Galeotti, G. Magazzu\textquotesingle , M. Minuti, A. Orsini, G. Petragnani, L. Pontisso, F. Raffaelli, F. Spinella, G. Collazuol, I. Mannelli, C. Avanzini, F. Costantini, L. Di Lella, N. Doble, M. Giorgi, S. Giudici, E. Pedreschi, R. Piandani, G. Pierazzini, J. Pinzino, M. Sozzi, L. Zaccarelli, A. Biagioni, E. Leonardi, A. Lonardo, P. Valente, P. Vicini, G. D\textquotesingle Agostini, R. Ammendola, V. Bonaiuto, N. De Simone, L. Federici, A. Fucci, G. Paoluzzi, A. Salamon, G. Salina, F. Sargeni, C. Biino, G. Dellacasa, S. Garbolino, F. Marchetto, S. Martoiu, G. Mazza, A. Rivetti, R. Arcidiacono, B. Bloch-Devaux, M. Boretto, L. Iacobuzio, E. Menichetti, D. Soldi, J. Engelfried, N. Estrada-Tristan, A. M. Bragadireanu, O. E. Hutanu, N. Azorskiy, V. Elsha, T. Enik, V. Falaleev, L. Glonti, Y. Gusakov, S. Kakurin, V. Kekelidze, S. Kilchakovskaya, E. Kislov, A. Kolesnikov, D. Madigozhin, M. Misheva, S. Movchan, I. Polenkevich, Y. Potrebenikov, V. Samsonov, S. Shkarovskiy, S. Sotnikov, L. Tarasova, M. Zaytseva, A. Zinchenko, V. Bolotov, S. Fedotov, E. Gushin, A. Khotjantsev, A. Khudyakov, A. Kleimenova, Yu. Kudenko, A. Shaikhiev, A. Gorin, S. Kholodenko, V. Kurshetsov, V. Obraztsov, A. Ostankov, V. Rykalin, V. Semenov, V. Sugonyaev, O. Yushchenko, L. Bician, T. Blazek, V. Cerny, M. Koval, R. Lietava, G. Aglieri Rinella, J. Arroyo Garcia, S. Balev, M. Battistin, J. Bendotti, F. Bergsma, S. Bonacini, F. Butin, A. Ceccucci, P. Chiggiato, H. Danielsson, J. Degrange, N. Dixon, B. Döbrich, P. Farthouat, L. Gatignon, P. Golonka, S. Girod, A. Goncalves Martins De Oliveira, R. Guida, F. Hahn, E. Harrouch, M. Hatch, P. Jarron, O. Jamet, B. Jenninger, J. Kaplon, A. Kluge, G. Lehmann-Miotto, P. Lichard, G. Maire, A. Mapelli, J. Morant, M. Morel, J. Noël, M. Noy, V. Palladino, A. Pardons, F. Perez-Gomez, L. Perktold, M. Perrin-Terrin, P. Petagna, K. Poltorak, P. Riedler, G. Romagnoli, G. Ruggiero, T. Rutter, J. Rouet, V. Ryjov, A. Saputi, T. Schneider, G. Stefanini, C. Theis, S. Tiuraniemi, F. Vareia Rodriguez, S. Venditti, M. Vergain, H. Vincke, P. Wertelaers, M. B. Brunetti, S. Edwards, E. Goudzovski, B. Hallgren, M. Krivda, C. Lazzeroni, N. Lurkin, D. Munday, F. Newson, C. Parkinson, S. Pyatt, A. Romano, X. Serghi, A. Sergi, R. Staley, A. Sturgess, H. Heath, R. Page, B. Angelucci, D. Britton, D. Protopopescu, I. Skillicorn, P. Cooke, J. B. Dainton, J. R. Fry, L. Fulton, D. Hutchcroft, E. Jones, T. Jones, K. Massri, E. Maurice, K. McCormick, P. Sutcliffe, B. Wrona, A. Conovaloff, P. Cooper, D. Coward, P. Rubin, and R. Winston. The beam and detector of the NA62 experiment at CERN. Journal of Instrumentation, 12(05):P05025–P05025, May 2017. URL: https://doi.org/10.1088%2F1748-0221%2F12%2F05%2Fp05025, doi:10.1088/1748-0221/12/05/p05025.")]. The final data product of the project consists of a modularized machine learning pipeline that takes in the raw experiment data in a HDF5 format, pre-processes it, prepares training data, trains a model on the training data, and finally runs the model.

One of the challenges in the project is, instead of using classification methods to distinguish between a muon or pion decay, we are only using the hit co-ordinates captured by this detector.

Based on the research and advice by the partner, we chose XGBoost as the baseline Machine Learning model, and applied a modified version of PointNet as well as a simple Multi-Layer Perceptron neural network.

From our results, the XGBoost seemed to be the best model to perform this ring-fitting. The results, unfortunately, did not yield a better performance than the current State of the Art algorithm employed by the NA62 team, which uses a maximum likelihood estimation (MLE) model.

## Installation

The project runs on Python 3.9+, and a Conda environment file can be found at [`environment.yaml`](environment.yaml).

To run the code, first clone the repository with [Git](https://git-scm.org/):

``` bash
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

``` bash
make run-all
```

It would create all the necessary Parquet files for the analyses involving the `run` dataset.

The main dataset (after cleaning) contains 2,376,174 events and 99,397,075 hits.

(Note that there is also `make run-full`, which also includes some of the obsolete data files derived from the main dataset.)

### Supplementary Dataset

The supplementary dataset (or the `pnn` dataset) is much larger, spanning several runs. However, since the events have been filtered, the label distribution is very different.

To generate the Parquet files associated with the `pnn` dataset, run the following command in the Conda environment:

``` bash
make pnn-all
```

The supplementary dataset (after cleaning) contains 42,897,096 events and 1,635,601,517 hits.

(Note that, similar to the main dataset, there is also `make pnn-full`, which also includes some of the obsolete data files associated with the supplementary dataset.)

### Clean-up

To clean up the generated Parquet files, run:

``` bash
make clean
```

Rest assured that it would *not* remove the raw H5 files.


## Copyright and Licensing

Unless otherwise specified, the code in this repository is covered under this copyright statement:

Copyright (c) 2023 Crystal Geng, Daniel Merigo, Kelvin Wong, Peng Zhang

The software and associated documentation files are licensed under [the MIT License](https://opensource.org/license/mit/). You may find a copy of the license at [`LICENSE.md`](LICENSE.md).

The materials in the `docs/` folder are licensed under [the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND 4.0) License](https://creativecommons.org/licenses/by-nc-nd/4.0/). A copy of the license can be found at [`LICENSE-CC-BYNCND.md`](LICENSE-CC-BYNCND.md).
