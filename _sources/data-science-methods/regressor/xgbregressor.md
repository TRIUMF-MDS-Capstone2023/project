# XGBoost Regressor

## Why did we choose this model?

For our baseline model, we have attempted training XGBRegressor, RandomForestRegressor, LigtGBM and CatBoostRegressor. Out of all the models we have trained, we selected XGBRegressor {cite}`Chen_2016` as our baseline model because of its impressive performance and fast execution compared to other baseline models we experimented with. We employed XGBRegressor to train our data set, which exclusively consisted of muons. In addition to the previously mentioned engineered features, we included `total_in_time_hits` as one of the features in our model. The target variable `y_train` used for training the model corresponds to the calculated ring radius (`ring_radius_calc`), which is the theoretical ring radius determined based on the track momentum and mass of the particles.

## Performance

Using the default hyperparameters of `n_estimators = 100` and `max_depth = 6`, the XGBRegressor achieved an average training R2 score of 0.96 and an average test R2 score of 0.94 during 5-fold cross-validation. We attempted hyperparameter optimization using `RandomizedSearch`, but it did not yield significant improvements in performance. Additionally, the best parameter value found by `RandomizedSearch` was `n_estimators = 500`, which required substantial computational cost. Therefore, we decided to stick with the default hyperparameters.

## Residual Analysis

Although the XGBRegressor showed excellent performance, we noticed a bias near the higher end of the radius spectrum. The scatter plot of residuals shown in [Fig. 11](xgb_residual_plot), which represents the difference between the calculated ring radius and the predicted ring radius, reveals a slight bias towards the higher end of the calculated ring radius. More data points are concentrated above the 0 line, indicating that the model tends to underestimate the radius for higher values. In light of this residuals pattern, further in-depth analyses were conducted to investigate the underlying cause of this phenomenon.

```{figure} ../../../../../figures/xgb_residual_plot.png 
:name: xgb_residual_plot

Residual plot residuals vs. calculated ring radius for XGBRegressor
```       

To examine the correlation between the predicted ring radius and the theoretical ring radius, we computed the difference between the theoretical ring radius and its overall maximum for each data point. This is illustrated by the red line in [Fig. 12](xgb_max_calc_diff). If a data point lies above the red line, it suggests that the predicted ring radius is smaller than the theoretical ring radius. Conversely, if a data point lies below the red line, it indicates that the predicted ring radius is larger than the theoretical ring radius. Upon examining the more detailed plot on the right side of [Fig. 12](xgb_max_calc_diff), it becomes apparent that the data points below the red line are considerably scarce. Additionally, the data points appear to be "pushed" upwards by the presence of the red line. This observation suggests that the predictions are constrained by the upper limit of the theoretical ring radius. As a result, the predictions are unable to exceed the maximum value of the theoretical ring radius.

```{figure} ../../../../../figures/xgb_max_calc_diff.png
:name: xgb_max_calc_diff

Overlaid residual plot showing the difference between the theoretical ring radius and its overall maximum for each data point (shown as red line)
```

The underestimation can be further demonstrated by [Fig. 13](xgb_radius_vs_momentum), which illustrates the relationship between the ring radius and track momentum. As previously mentioned, the theoretical ring radius is determined based on the track momentum and mass of the particles, and it is depicted as the green curves in the plot. The predicted radii are represented by the blue and orange scatter points on the plot. By examining the magnified view of the predicted radius specifically for muons in the right plot, it becomes apparent that the model begins to underestimate the radius predictions when the track momentum reaches approximately 57 GeV/c. At this point, the predicted values start to plateau, whereas the theoretical values continue to gradually increase.

```{figure} ../../../../../figures/xgb_radius_vs_momentum.png 
:name: xgb_radius_vs_momentum

Overlaid plot showing predicted ring radius and theoretical ring radius vs. track momentum for XGBRegressor
```       

## SHAP Analysis

To identify the feature responsible for the underestimation, we performed two analyses: feature importance computation and Shapley Additive Explanations (SHAP) analysis. The SHAP analysis allowed us to visualize the contribution of each feature towards the model's output. SHAP values provide insights into the impact of each feature on the predictions made by the machine learning model. A negative SHAP value indicatees that the feature has a negative influence on the prediction, while a positive SHAP value indicates a positive contribution to the prediction. These analyses enabled us to gain a better understanding of the factors leading to the underestimation issue.

[Fig. 14](xgb_shap_plot) illustrates the feature importance rankings in a descending order from top to bottom. The colour scheme represents the feature values, with high values depicted in pink and low values depicted in blue. In the plot, the feature `hit_distance_median` is positioned at the top, indicating that it is the most important feature. This aligns with the feature importance value of 0.87 derived from our analysis results. Notably, for `hit_distance_median`, it can be observed that lower feature values correspond to lower SHAP values, which is expected since a lower `hit_distance_median` is correlated with a smaller predicted radius.

However, the SHAP values for higher feature values of `hit_distance_median` appear to be clustered and fail to extend as far as the negative SHAP values. This observation suggests that the predicted radius may exhibit a non-linear relationship with the `hit_distance_median feature` when it comes to higher radius values. Furthermore, it indicates that the prediction reaches an upper limit beyond which it cannot surpass. This finding supports our earlier speculation that the prediction is constrained by the upper limit of the theoretical ring radius values.

```{figure} ../../../../../figures/xgb_shap_plot.png
:name: xgb_shap_plot

SHAP summary plot showing the SHAP values and feature values for all the features in XGBRegressor
```

## Conclusion

The XGBRegressor model demonstrates favourable performance, as evidenced by high training and test R2 scores, with the majority of residuals concentrated around 0. However, there exists an underestimation issue specifically associated with higher radius values. This underestimation is believed to be limited by the upper limit of the theoretical ring radius, a hypothesis supported by our residual analysis and SHAP analysis.

In attempts to address this problem, we explored various techniques such as feature selection, L1 and L2 regularization, and hyperparameter optimization. Unfortunately, these approaches did not effectively mitigate the bias. Notably, we observed the same residual bias when employing other tree-based models such as RandomForestRegressor, LightGBMRegressor, and CatBoostRegressor.

Given the persistent bias, we became intrigued by the possibility of utilizing more sophisticated models like neural networks, hoping they may alleviate the issue.
