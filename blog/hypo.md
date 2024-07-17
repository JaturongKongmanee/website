# Evaluating Hypotheses

One fundamental to machine learning is to estimate the accuracy of hypothesis accuracy. According to Tom M. Mitchell, this rises three important questions: 1) given the observed accuracy of a learned hypothesis over a limited examples, how well does this estimate its accuracy over additional examples (see Section [1](#estimating-hypothesis-accuracy) for methods for evaluting learned hypothesis)?; 2) given that one hypothesis outperforms another over some sample of data, how probable is it that this hypothesis is more accurate in general (see Section [2](#difference-in-error-of-two-hypotheses) for comparing the accuracy of two hypotheses)?; and 3) given that data is limited, what is the best way to use this data to both learn a hypothesis and estimate its accuracy (see Section [3](#comparing-learning-algorithms) for comparing the accuracy of two learning algorithms when only limited data is available)?

In practice we have access to only limited samples that migh misrepresent the general distribution of data of problems of our interests, leading to inaccurate estimate of true accuracy of a learned hypothesis (we would not have to worry if data is abundant and representive). Learning a hypothesis and estimate its accuracy on future, unseen data given only a limited data raises two key difficulties:
- ***Bias in the estimate*** Because the leanred hypothesis was derived from the training examples, its accuracy is often a poor estimate of future examples, especially when considering a rich hypothesis space (i.e., ovefitting training examples). Testing the hypothesis on a test set of examples chosen independently of the training examples and the hypothesis is a method to obtain an unbiased accuracy estimate for future, unseen examples.
  
- ***Variance in the estimate*** The measie

## 1. Estimating Hypothesis Accuracy
## 2. Difference in Error of Two Hypotheses
## 3. Comparing Learning Algorithms
