# Executive Summary

The *Calorich AI* project is proposed by TRIUMF, Canada's national particle accelerator center, to improve the Ring-Imaging CHerenkov detector (RICH detector) particle identification performance. Our work this year is an extension of the *RICH AI* project {cite}`RICHAI`, attempted by an MDS capstone team of similar goals last year.

The project dataset comes from the NA62 experiment at CERN, the European Organization for Nuclear Research, which involves a particle physics experiment designed to study rare decays of charged kaons. The capstone project aims to build a model to accurately classify a particle as a pion produced in a decay event. We aim to train models using the data from a subset of the 2021A NA62 experiments, which contains around 2.4 million decay events labeled by calorimeter {cite}`Gil_2017`. The final data product of the project consists of a modularized machine learning pipeline that takes in the raw experiment data in a HDF5 format, pre-processes it, prepares training data, trains a model on the training data, and finally runs the model.

One of the challenges in the project is, instead of using classification methods to distinguish between a muon or pion decay, we are only using the hit co-ordinates captured by this detector.

Based on the research and advice by the partner, we chose XGBoost as the baseline Machine Learning model, and applied a modified version of PointNet as well as a simple Multi-Layer Perceptron neural network.

From our results, the XGBoost seemed to be the best model to perform this ring-fitting. The results, unfortunately, did not yield a better performance than the current State of the Art algorithm employed by the NA62 team, which uses a maximum likelihood estimation (MLE) model.
