---
title: A Gentle Introduction to Transformer Architecture
date: 2026-08-30
tags: deep-learning, nlp, attention-mechanism, transformers
author: Jaturong Kongmanee
url: https://jaturongkongmanee.github.io/website/blog/intro_to_transformers.html
---

# A Gentle Introduction to Transformer Architecture

## Introduction

The Transformer architecture has become the backbone of modern deep learning, powering everything from large language models (LLMs) to computer vision systems[^1]. In this post, we'll explore the key components that make transformers work, with clear mathematical explanations.

Before transformers, recurrent neural networks (RNNs) and their variants (LSTMs, GRUs) were the standard for sequence modeling. However, they have a fundamental limitation: they process sequences sequentially, which makes them slow to train on long sequences.

The transformer solves this with a clever mechanism called **attention** [1], which allows the model to look at all parts of the input at once. This breakthrough was introduced in the seminal paper "Attention is All You Need" and has since become the foundation for state-of-the-art models in NLP and beyond.

## The Problem with Sequences

Traditional RNNs process sequences like this:

$$h_t = \text{RNN}(x_t, h_{t-1})$$

where:
- $h_t$ is the hidden state at time $t$
- $x_t$ is the input at time $t$
- The computation depends on the previous hidden state $h_{t-1}$

This sequential dependency creates two problems:
1. **Slow training**: Each step must wait for the previous step to complete
2. **Limited context**: For very long sequences, information from early steps gets diluted

## The Attention Mechanism

The core innovation of transformers is the **Scaled Dot-Product Attention** [1]:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

where:
- $Q$ (Query), $K$ (Key), $V$ (Value) are learned projections of the input
- $d_k$ is the dimension of the keys
- The scaling factor $\frac{1}{\sqrt{d_k}}$ prevents the softmax from having very small gradients

### How Attention Works

Let's break this down step by step:

1. **Compute Attention Scores**: $QK^T$ produces a score for each pair of positions
2. **Scale**: Divide by $\sqrt{d_k}$ to keep gradients stable
3. **Softmax**: Convert scores to probabilities that sum to 1
4. **Weight Values**: Multiply probabilities by the value vectors

The result is a weighted sum of values, where weights represent how much each position should attend to each other position[^2].

### Example with Numbers

Suppose we have a sequence of 3 words with embedding dimension $d_k = 2$:

Let's say the Query, Key, and Value matrices are:

$$Q = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix}, \quad K = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix}, \quad V = \begin{pmatrix} 2 & 0 \\ 0 & 2 \\ 1 & 1 \end{pmatrix}$$

Then:

$$QK^T = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 2 \end{pmatrix}$$

After scaling by $\sqrt{d_k} = \sqrt{2} \approx 1.41$:

$$\text{Scores} = \begin{pmatrix} 0.71 & 0 & 0.71 \\ 0 & 0.71 & 0.71 \\ 0.71 & 0.71 & 1.41 \end{pmatrix}$$

After softmax on each row, we get attention weights between 0 and 1 that sum to 1.

## Multi-Head Attention

Instead of using one attention function, transformers use **multiple attention heads** in parallel[^3]:

$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h)W^O$$

where each head is:

$$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

**Why multiple heads?**
- Different heads can learn different types of relationships
- One head might focus on syntactic structure, another on semantic meaning
- Typically 8-16 heads in modern transformers

## The Complete Transformer Block

A transformer encoder block consists of:

1. **Multi-Head Attention**
2. **Add & Norm** (residual connection + layer normalization)
3. **Feed-Forward Network** (two dense layers with ReLU)
4. **Add & Norm** (residual connection + layer normalization again)

Mathematically:

$$\text{Attention Out} = \text{LayerNorm}(x + \text{MultiHeadAttention}(x, x, x))$$

$$\text{Output} = \text{LayerNorm}(\text{Attention Out} + \text{FFN}(\text{Attention Out}))$$

where the FFN is:

$$\text{FFN}(x) = \text{ReLU}(xW_1 + b_1)W_2 + b_2$$

## Positional Encoding

Since attention has no inherent notion of position (it's just a weighted sum), we need to inject position information. This is done with **sinusoidal positional encodings**:

$$PE_{(pos,2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right)$$

$$PE_{(pos,2i+1)} = \cos\left(\frac{pos}{10000^{2i/d}}\right)$$

where:
- $pos$ is the position in the sequence
- $i$ is the dimension index
- $d$ is the embedding dimension

These are added to the input embeddings before passing through the transformer blocks.

## From Encoder to Decoder

The full transformer consists of:

- **Encoder**: Stack of transformer blocks processing the input
- **Decoder**: Stack of transformer blocks generating the output, with cross-attention to the encoder

In the decoder:
- **Self-Attention**: Attends to previous tokens (with masking to prevent looking ahead)
- **Cross-Attention**: Attends to encoder outputs
- **Feed-Forward**: Same as encoder

## Key Advantages

| Property | RNN | Transformer |
|----------|-----|-------------|
| Parallelizable | ❌ Sequential | ✅ All at once |
| Long-range dependencies | ⚠️ Difficult | ✅ Direct |
| Training speed | Slow | Fast |
| Memory usage | Low | High |
| Position info | Implicit | Explicit (positional encoding) |

## Simple Implementation Sketch

Here's a minimal PyTorch-like pseudocode based on the transformer architecture [1]:

```python
class Attention(nn.Module):
    def forward(self, Q, K, V):
        scores = Q @ K.T / sqrt(d_k)  # Compute scores
        weights = softmax(scores)       # Convert to probabilities
        return weights @ V              # Weight values

class TransformerBlock(nn.Module):
    def forward(self, x):
        # Multi-head attention with residual connection
        x = x + MultiHeadAttention(x, x, x)
        x = LayerNorm(x)
        
        # Feed-forward with residual connection
        x = x + FFN(x)
        x = LayerNorm(x)
        
        return x

class Transformer(nn.Module):
    def __init__(self, num_blocks):
        self.blocks = [TransformerBlock() for _ in range(num_blocks)]
    
    def forward(self, x):
        x = x + PositionalEncoding(x)
        for block in self.blocks:
            x = block(x)
        return x
```

## Common Applications

### Natural Language Processing

- **GPT series** [4]: Decoder-only transformers for text generation. Pioneered by OpenAI, these models demonstrate the effectiveness of transformer-only architectures for language understanding and generation.

- **BERT** [2]: Encoder-only transformers for classification and understanding. Introduced bidirectional training of transformers, which significantly improved performance on NLP tasks.

- **T5** [3]: Encoder-decoder for sequence-to-sequence tasks. Unified NLP tasks as text-to-text problems, showing the flexibility of the transformer architecture.

### Computer Vision

- **Vision Transformer (ViT)** [5]: Applies transformers directly to image patches, demonstrating that pure transformer-based models can achieve competitive results on image classification without convolutional layers.

- **DETR**: Detection with transformers, treating object detection as a sequence-to-sequence problem.

### Multimodal

- **CLIP**: Vision + Language models that align image and text representations.
- **Flamingo**: Vision + Language generation combining the strengths of both modalities.

## Conclusion

The transformer architecture revolutionized deep learning by [1]:
1. Enabling **parallel processing** of sequences
2. Capturing **long-range dependencies** effectively
3. Providing a **flexible building block** for many domains

The key insight is the attention mechanism: instead of processing sequences step-by-step, allow the model to dynamically focus on relevant parts of the input. Since its introduction, the transformer has been continuously improved with variants like BERT [2], T5 [3], GPT [4], Vision Transformers [5], and ELECTRA [6], showing its versatility across different domains and tasks.

[^1]: The transformer architecture was introduced by Vaswani et al. in 2017 and has since become the foundation for most modern NLP and vision models.

[^2]: This mechanism allows the model to learn which parts of the input are most relevant for each output position, enabling complex reasoning and long-range dependencies.

[^3]: Multi-head attention allows the model to attend to information from different representation subspaces at different positions. With just one head, the model would have limited expressiveness.

## Cited as

Please cite this work as:

<!-- **APA Style:** -->
```
Kongmanee, J. (Aug 2026). A Gentle Introduction to Transformer Architecture. 
Jaturong Kongmanee. https://jaturongkongmanee.github.io/website/blog/intro_to_transformers.html
```

Or use the BibTeX citation:

<!-- **BibTeX:** -->
```bibtex
@article{kongmanee2026transformers,
  title   = "A Gentle Introduction to Transformer Architecture",
  author  = "Kongmanee, Jaturong",
  journal = "jaturongkongmanee.github.io",
  year    = "2026",
  month   = "Aug",
  url     = "https://jaturongkongmanee.github.io/website/blog/intro_to_transformers.html"
}
```

---

## References

[1] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. ["Attention is all you need."](https://arxiv.org/abs/1706.03762) *Advances in Neural Information Processing Systems* (2017)

[2] Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. ["BERT: Pre-training of deep bidirectional transformers for language understanding."](https://arxiv.org/abs/1810.04805) arXiv preprint arXiv:1810.04805 (2018)

[3] Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., ... & Liu, P. J. ["Exploring the limits of transfer learning with a unified text-to-text transformer."](https://arxiv.org/abs/1910.10683) arXiv preprint arXiv:1910.10683 (2019)

[4] Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., ... & Amodei, D. ["Language models are few-shot learners."](https://arxiv.org/abs/2005.14165) arXiv preprint arXiv:2005.14165 (2020)

[5] Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., ... & Houlsby, N. ["An image is worth 16x16 words: Transformers for image recognition at scale."](https://arxiv.org/abs/2010.11929) arXiv preprint arXiv:2010.11929 (2020)

[6] Clark, K., Luong, M. T., Le, Q. V., & Manning, C. D. ["ELECTRA: Pre-training text encoders as discriminators rather than generators."](https://arxiv.org/abs/2020.04687) *International Conference on Learning Representations* (2020)
<!-- 
## Further Reading

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) - Great visual explanation
- [Transformers from Scratch](https://e2eml.school/transformers.html) - Interactive walkthrough
- [The Transformer Blueprint](https://samrawal.medium.com/transformers-from-scratch-in-pytorch-a-step-by-step-guide-6318e79f367b) - Step-by-step PyTorch guide

--- -->

<!-- **Tags**: #DeepLearning #NLP #Transformers #Attention #MachineLearning -->
