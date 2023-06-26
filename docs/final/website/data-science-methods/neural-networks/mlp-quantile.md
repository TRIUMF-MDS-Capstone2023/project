# MLP Quantile Regression

## Why did we choose this model

A regular machine learning approach for regression problems only provides a numerical prediction for each observation. In order to evaluate how confident the prediction is, we need to know the quantiles of the predicted value. Moreover, for our particular project as part of the NA62 experiment, the ultimate goal is to distinguish pions and muons. It would be useful if we have more tools available to examine the uncertainty of the predicted ring radius so further researches may be continued to identify the two particles based on the difference of their fitted ring radius at a certain level of track momentum.

## Features and model structure

Based on the MLP architecture in the previous section, we have defined a quantile loss function and modified the trainer function to implement the quantile regression approach. The rest of the model structure, input features, target and the training process are the same as the MLP. We can specify the desired quantile as one of the parameters in the trainer function to predict the corresponding quantile of ring radius.

## Results

Since it is a preliminary research as part of our project, so far we have only experimented with three quantiles (q = 0.05, 0.5, 0.95) of predicted ring radius as shown in [Fig. 6](qmlp_pred_plot). To demonstrate the trend, all values are sorted and the x-axis only indicates the index of the observations. The red line on the most right side of the plot is the theoretical ring radius (the target of the regression model). And the predicted ring radius for three quantiles are the scatter points in different colours on the left side. From the plot, the predictions with three quantiles show the same pattern of distributions, and we did not see a significant variation between three quantiles.

```{figure} ../../../../../figures/qmlp_pred_plot.png
:name: qmlp_pred_plot

Predicted ring radius per quantile 0.05, 0.5, and 0.95
```

## Further analysis

Due to time constraints of the capstone project, we have not conducted a full study and analysis on the MLP Quantile Regression approach. We suggest further works to be performed in the future, such as predicting more quantiles, exploring predictions of pions and muons in different momentum ranges.
