# PointNet

## Why did we choose this architecture?

Developed in Stanford, [PointNet](https://arxiv.org/abs/1612.00593) is a simple yet effective architecture that directly consumes 3-dimensional point clouds and can perform diverse operations such as classification, part segmentation and even semantic parsing {cite}`qi2017pointnet`. Of these characteristics we concluded that, since the original hit data is already a 2 dimensional point cloud, the ability of the architecture to find patterns in a point cloud regardless of its positioning in space would make a good fit for the project.

In order to apply this architecture to the regression problem we had to do some modifications, including:
- Adding a third dimension to the hit locations using Gaussian noise in the range (0, 0.5)
- Substituting the output layer with a linear fully connected layer
- Changing the output size to 1

We developed 2 distinct architectures, based on the base PointNet architecture, in PyTorch to compare and test simultaneously. We used the MSELoss Loss function and Adam Optimizer. Each architecture also utilized ReLU as the activation function

## Benefits and Limitations

PointNet is an architecture developed to perform classifications, translating the architecture to a regression problem meant discarding the semantic segmentation portion and adding a 3rd dimension at first. This added complexity to the data preparation and in the end could not capture local information or immediately determine the particle for a given event.

Training time was also a limitation as, even with pre-transformed parquet files, the training time averaged 15 minutes per epoch on a high end GPU (RTX 3080).

## Results

```{figure} ../../../../../figures/pnt_pred_theo.png 
:name: pnt_predicted_vs_theoretical

Residual plot predicted vs. calculated ring radius for PointNet 
```

As shown in [Fig 17](pnt_predicted_vs_theoretical) the performance of PointNet is deficient, not being able to capture the trends in the model. The predicted results have a different behaviour than the ground truth, shown here as a black line. These results, combined with the long training time, motivated us to decide on XGBoost as the best modelling technique for this regression problem.


