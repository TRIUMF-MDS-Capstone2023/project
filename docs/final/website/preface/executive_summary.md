# Executive Summary

The project focuses on the NA62 project conducted by [CERN](https://home.cern). The NA62 requires a high level of identification performance to distinguish between muons and pions during a rare meson decay in order to verify the Standard Model of Physics. This identification is performed using the Cherenkov Radiation phenomenon, specifically the photon ring radius constructed from the array of photodetectors in the RICH detector.

From our results, the XGBoost seemed to be the best model to perform this ring-fitting. The results, unfortunately, did not yield a better performance than the current state-of-the-art algorithm employed by the NA62 team, which uses a maximum likelihood estimation (MLE) model.
