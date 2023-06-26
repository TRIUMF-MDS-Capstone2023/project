# Introduction

## Background

The project focuses on the NA62 project conducted by [CERN](https://home.cern). The NA62 requires a high level of Identification performance to distinguish between muons and pions during a rare meson decay in order to verify the Standard Model of Physics. This identification is performed using the Cherenkov Radiation phenomenon, specifically the photon ring radius constructed from the array of photodetectors in the RICH detector.

## Scope and Challenges

A similar project from last year, *RICH AI* {cite}`RICHAI`, aimed to improve the particle identification performance of the Ring Imaging Cherenkov (RICH) detector. This project, *Calorich AI* follows from the conclusions of the 2022 project, which used classification experiments to determine the specific particle decay in a certain "event". Each event consists of a certain number of "hits" (excited photodetectors in the RICH detector) and the specific momentum of the particle as detected in the STRAW detection array in a previous step of the NA62 process.

Our challenge is to improve the capability to determine the specific ring radius of the Cherenkov Radiation cone in the RICH detector by avoiding the use of the momentum detection and performing a regression analysis instead of a classification based on the "hits" data only.

## Output and Deliverables

The aim of the *Calorich AI* project is the creation of a concise, documented and reproducible machine learning pipeline. The pipeline must include the data preprocessing, hyperparameters, models and training procedures required to achieve the results presented on this report in a manner such that the TRIUMF team can verify the findings and potentially incorporate the pipeline into their own ML pipelines.
