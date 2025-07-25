# k-NN Credit Risk Analysis Presentation Script

## Slide 23: Workflow Overview

Similar to the other models, the general workflow for kNN is that we start with 16,000 credit records. We transform the data and engineered features for the pre-processing. After an 80-20 train-test split, we standardize features through scaling, then tune our k parameter through cross-validation. Finally, we evaluate against our baseline model.


## Slide 24: Optimal k Selection

This graph shows the performance at different k-values. We tested k from 1 to 60 using cross-validation. You can see accuracy jumps dramatically from k=1 to around k=20, then plateaus near 77%. The sweet spot is k=21—this balances the bias-variance tradeoff. Too low and we overfit to noise; too high and we lose local patterns. So this gives us the best generalization while maintaining sensitivity to local neighborhoods in our feature space.

## Slide 25: Learning Curves Analysis

These learning curves reveal how our model scales with data. The blue line shows training accuracy, green shows cross-validation. Notice how they converge and stabilize and small gap between them all indicate minimal overfitting, and both curves plateau around 10,000 samples. This tells us our model has found the signal in the data and more samples would yield diminishing returns. The tight confidence bands show consistent performance across different data splits.

## Slide 26: Curse of Dimensionality

Here's a fascinating experiment—we artificially added random features to demonstrate the curse of dimensionality. Starting at 72% accuracy with our engineered features, performance drops dramatically as we add noise, reaching just 61% at 100 dimensions. This validates our feature engineering approach. In high-dimensional spaces, all points become equidistant, making neighborhood relationships meaningless. Quality feature selection beats quantity every time with k-NN.

## Slide 27: Feature Importance Analysis

We then identified what really drives default prediction. The two dominant features are total late payments and revolving utilization, both log-transformed financial metrics. Removing either drops accuracy by over 10%. This aligns very well with lending intuition: payment history and credit utilization are the strongest default predictors. The other features contribute modestly, but these two are absolutely critical for accurate risk assessment.

## Slide 28: Confusion Matrix Deep Dive

Our test set results, again about 20% of the data. We correctly identify 1,356 good borrowers and 1,206 risky ones. The key concern is our 433 false negatives, risky loans we'd approve. At 13% of risky loans, this represents real financial exposure. However, our 348 false positives mean we'd only reject 10.4% of good applicants. This balance suggests the model could support lending decisions with appropriate risk management.

## Slide 29: Performance Metrics Summary

Wrapping up our evaluation: precision of 77.6% means when we predict default, we're right about 4 times out of 5. Recall of 73.6% means we catch roughly 3 out of 4 actual defaults. The F1 score of 75.5% balances these nicely. Overall accuracy of 76.6% represents a 7% improvement over random baseline models. For a simple model k-NN could meaningfully improve lending decisions while remaining explainable to stakeholders.
