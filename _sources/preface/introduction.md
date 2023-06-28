# Introduction

## Background

The CaloRICH AI project is proposed by TRIUMF, Canada’s national particle accelerator center, to improve the Ring-Imaging CHerenkov detector (RICH detector) particle identification performance. Our work this year is an extension of the RICH AI project [den Hooff N et al., 2022], attempted by an MDS capstone team of similar goals last year.

The project dataset comes from the NA62 experiment at CERN, the European Organization for Nuclear Research, which involves a particle physics experiment designed to study rare decays of charged kaons. The capstone project aims to build a model to accurately classify a particle as a pion produced in a decay event. We aim to train models using the data from a subset of the 2021A NA62 experiments, which contains around 2.4 million decay events labeled by calorimeter [Gil et al., 2017].

Based on the research and advice by the partner, we chose XGBoost as the baseline Machine Learning model, and applied a modified version of PointNet as well as a simple Multi-Layer Perceptron neural network.

## Scope and Challenges

A similar project from last year, *RICH AI* [@RICHAI], aimed to improve the particle identification performance of the Ring Imaging Cherenkov (RICH) detector. This project, *CaloRICH AI* follows from the conclusions of the 2022 project, which used classification experiments to determine the specific particle decay in a certain "event". Each event consists of a certain number of "hits" (excited photodetectors in the RICH detector) and the specific momentum of the particle as detected in the STRAW detection array in a previous step of the NA62 process.

Our challenge is to improve the capability to determine the specific ring radius of the Cherenkov Radiation cone in the RICH detector, by avoiding the use of the momentum detection and performing a regression analysis instead of a classification based on the "hits" data only.

## Output and Deliverables

The aim of the *CaloRICH AI* project is the creation of a concise, documented and reproducible machine learning pipeline. The pipeline must include the data preprocessing, hyperparameters, models and training procedures required to achieve the results presented on this report in a manner such that the TRIUMF team can verify the findings and potentially incorporate the pipeline into their own ML pipelines.
