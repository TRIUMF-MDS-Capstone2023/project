# Best Performing Model

## Justification

After evaluating the performance of three models: XGBRegressor, MLP, and PointNet, it appears that XGBRegressor currently outperforms the others. According to Table 1, both XGBRegressor and MLP demonstrate similar best R2 scores. However, the performance of the PointNet architecture has not been satisfactory thus far, and it also requires an exceptionally long training time.

| Model        | Training Time  | Best Test R2 |
|--------------|----------------|--------------|
| XGBRegressor | \~ 3 minutes   | 0.94         |
| MLP          | \~ 8 minutes   | 0.94         |
| PointNet     | \~ 23.5 hours  | 0.20         |

: Table 1. Model performance comparison

When comparing the performance of XGBRegressor and MLP, it is difficult to determine the better performing model solely based on their performance scores. However, taking into account the difference in training time, with XGBRegressor being more than 2 times faster, and considering the additional complexity associated with MLP modeling, it is reasonable to conclude that XGBRegressor is a more efficient and simpler choice in terms of both time consumption and computational power. Overall, we determine XGBRegressor to be the best performing model with our training data.
