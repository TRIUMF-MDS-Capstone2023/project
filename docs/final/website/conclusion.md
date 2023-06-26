# Conclusion

In this capstone project we have applied machine learning regression methods to predict the ring radius from variable number of "hits" (excited photodetectors in the RICH detector) for each event of decay. Three models, XGBRegressor, MLP, and PointNet, have been adopted to perform the ring fitting. Both XGBRegressor and MLP were using engineered features generated from hit positions as inputs, while PointNet was directly trained on the raw data of hit coordinates. The result of regression evaluation metrics shown XGBRegressor had the best performance compared to the other two deep learning approaches. Considering the simplicity of model structure and implementation, timing, and future maintenance, we recommend XGBRegressor as the best option to perform the regression task.

Although the result of PointNet did not yield an expected performance, we have identified the probable reason, a vanishing gradient, a thus have devised solutions to this problem. Due to the time consuming process of training a new model with the necessary modifications we are keeping these conclusions for the moment and will update if a solution is found and has proven to yield better results than XGBoost.

## Future works

For the future works, we would suggest the following areas:

1.  In addition to the three regular regression models, we have also started a quantile regression based on the MLP architecture. Due to time constraints, more research and [analysis](https://triumf-mds-capstone2023.github.io/project/data-science-methods/neural-networks/mlp-quantile.html) could be continued to explore the possibility of quantile regression to facilitate the differentiation of pions and muons in different track momentum ranges.

2.  Since the ultimate goal of the NA62 project is to distinguish pions and muons{cite}`Gil_2017`, the resolution of fitted ring radius for the two particles in each track momentum range would be important. We need to consider both accuracy and precision of the predictions in order to separate two particles effectively in the future studies.

3.  We also suggest exploring the use of a [Convolutional Neural Network (CNN)](https://www.ibm.com/topics/convolutional-neural-networks) in future experiments as they have proven reliability in image pattern recognition. If the RICH photodetector is treated as a pixel array there could be the opportunity to obtain a promising result.
