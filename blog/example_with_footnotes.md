---
title: Understanding Neural Networks with Footnotes
date: 2026-08-30
tags: deep-learning, neural-networks, tutorial
author: Jaturong Kongmanee
---

# Understanding Neural Networks with Footnotes

## Introduction

Neural networks have become the foundation of modern deep learning[^1]. They are inspired by biological neural networks in animal brains[^2], and consist of interconnected nodes (neurons) that process information through weighted connections.

## What are Neural Networks?

A neural network is a computational model inspired by biological neurons[^3]. Each neuron receives inputs, applies a weight to each input, sums them up, and passes the result through an activation function[^4].

The basic structure consists of:
- **Input layer**: Receives raw data
- **Hidden layers**: Process information through learned weights
- **Output layer**: Produces predictions

## Mathematical Foundation

The output of a single neuron is computed as:

$$y = \sigma(w_1 x_1 + w_2 x_2 + \cdots + w_n x_n + b)$$

where:
- $x_i$ are the input values
- $w_i$ are the weights
- $b$ is the bias term
- $\sigma$ is the activation function[^5]

## Training Neural Networks

Neural networks are trained using backpropagation[^6], which calculates the gradient of the loss function with respect to each weight. This allows us to update weights in the direction that minimizes the loss:

$$w_{new} = w_{old} - \eta \frac{\partial \mathcal{L}}{\partial w}$$

where $\eta$ is the learning rate[^7].

## Activation Functions

Common activation functions include[^8]:

- **ReLU (Rectified Linear Unit)**: $f(x) = \max(0, x)$
- **Sigmoid**: $f(x) = \frac{1}{1 + e^{-x}}$
- **Tanh**: $f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$

Each has different properties and is suited for different scenarios[^9].

## Applications

Neural networks are used in numerous applications[^10]:
- Computer vision for image classification
- Natural language processing for text analysis
- Reinforcement learning for game playing
- Time series forecasting

## Conclusion

Neural networks are powerful tools that have revolutionized machine learning[^11]. Understanding their mathematical foundations is crucial for building effective models[^12].

[^1]: LeCun, Y., Bengio, Y., & Hinton, G. (2015). "Deep learning." Nature, 521(7553), 436-444.

[^2]: McCulloch, W. S., & Pitts, W. (1943). "A logical calculus of ideas immanent in nervous activity." The Bulletin of Mathematical Biophysics, 5(4), 115-133.

[^3]: The biological inspiration includes the structure of synapses and neurotransmitters in the brain.

[^4]: Common activation functions include ReLU, sigmoid, and tanh, each with different properties.

[^5]: The activation function introduces non-linearity, allowing networks to learn complex patterns.

[^6]: Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). "Learning representations by back-propagating errors." Nature, 323(6088), 533-536.

[^7]: The learning rate controls the size of weight updates and is a critical hyperparameter.

[^8]: Different activation functions have different properties: ReLU is computationally efficient, sigmoid is bounded between 0 and 1, and tanh is bounded between -1 and 1.

[^9]: ReLU is popular in hidden layers due to its computational efficiency and effectiveness in deep networks.

[^10]: Modern deep learning applications extend far beyond traditional machine learning domains.

[^11]: The deep learning revolution has transformed fields like computer vision, NLP, and speech recognition.

[^12]: Understanding backpropagation, gradient descent, and the role of activation functions is essential for practitioners.
