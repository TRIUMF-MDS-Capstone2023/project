# PointNet

## Architecture

Developed in Stanford, PointNet is a simple yet effective architecture that directly consumes 3-dimensional point clouds and can perform diverse operations such as classification, part segmentation and even semantic parsing. In order to apply this architecture to the regression problem we had to do some modifications (refer to appendix for further explanation and architecture).

We developed 2 distinct architectures based on the base PointNet architecture to compare and test simultaneously.

## Benefits and Limitations

PointNet is an architecture developed to perform classifications, translating the architecture to a regression problem meant discarding the semantic segmentation portion and adding a 3rd dimension at first. This added complexity to the data preparation and in the end could not capture local information or immediately determine the particle for a given event.

Training time was also a limitation as, even with pre-transformed parquet files, the training time averaged 15 minutes per epoch on a high end GPU (RTX 3080).

## Results

```{figure} ../../../../../figures/pnt_pred_theo.png 
:name: pnt_predicted_vs_theoretical

Residual plot predicted vs. calculated ring radius for PointNet
```

As shown in [Fig 7](pnt_predicted_vs_theoretical) the performance of PointNet is deficient, not being able to capture the trends in the model. The predicted results have a different behaviour than the ground truth, shown here as a black line. These results, combined with the long training time, motivated us to decide on XGBoost as the best modelling technique for this regression problem.
