# MLP (Multilayer Perceptron)

## Why did we choose this model

A multilayer perceptron (MLP) is a classic fully connected feedforward neural network. In our project for the regression problem, by designing appropriate number of hidden layers and incorporating a non-linear activation function, the model is expected to capture more complex linear and non-linear relationships between input features (regressors) and the target in the training dataset, and output predictions for the unseen testing dataset. MLP is easy to implement in the PyTorch {cite}`pytorch` framework. It provides us with the extensive flexibility to custom design deep learning structures, define particular loss functions, or add more functionalities to our modeling. For example, we have also implemented a quantile regression based on the MLP architecture.

## Features and model structure

The MLP model has taken all [18 engineered features](https://triumf-mds-capstone2023.github.io/project/data/engineered-features.html) as the inputs, the theoretical ring radius as the target, to predict the ring radius for each event.

After a number of experiments, we have selected a MLP model with 4 hidden layers. The hidden size is gradually decreased from 1024 to 12, and the [ReLU activation function](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) has been used in each hidden layer.

## Training process and results

To avoid possible bias from two particles, the model has been trained on randomly split 75% of muon events, then tested on the rest of muon events and all pion events. Based on the PyTorch framework, we have developed the training and validation data loaders, the custom defined trainer, used standard [MSELoss function](https://pytorch.org/docs/stable/generated/torch.nn.MSELoss.html) and Adam optimizer {cite}`kingma2017adam` to train the MLP model.

In addition, before feeding features into the model, the [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) has been applied to rescale the inputs considering unscaled inputs could result in exploding gradients during the learning process.

After the training completed, we tested the regression performance on the test data. Between the predicted ring radius and the theoretical values, the R2 score was 0.934 and the MAE (Mean Absolute Error) was 1.92. Compared to the result of the XGBRegressor approach (R2 was 0.94), the accuracy of the MLP model was slightly lower.

We have also performed residual analysis for the MLP model. As shown in [Fig. 5](mlp_residual_plot), the similar patterns were observed compared to the residual plot from the XGBRegressor. The result confirms the bias analysis in the previous section.

```{figure} ../../../../../figures/mlp_residual_plot.png
:name: mlp_residual_plot

Residual plot residuals vs. calculated ring radius for MLP model
```

## Conclusion

From the result comparison between XGBRegressor and the MLP model, we can see the deep learning architecture (MLP) did not improve the regression performance. Considering the longer training time, and the extra pre-processing steps including normalisation and tensor conversion required for the MLP modeling, we think the XGBRegressor is the better approach for the regression purpose.

One of the advantages of deep learning methods is to rely on the complex networks to perform feature engineering and feature extraction. In our case, we feed the MLP model with explicitly engineered features rather than the raw data (coordinates of hits for each event). It is possible that the method we have used in this section did not reach the full potential of the deep learning. Therefore, we are exploring other neural network architectures that can be directly trained with the raw hit coordinates.
