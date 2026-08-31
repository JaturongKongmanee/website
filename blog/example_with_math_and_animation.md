# Understanding Gaussian Distributions with Interactive Visualization

## Introduction

The Gaussian (normal) distribution is one of the most important probability distributions in statistics and machine learning. In this post, we'll explore its mathematical properties and visualize it interactively.

## Mathematical Definition

The probability density function (PDF) of a Gaussian distribution is defined as:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

where:
- $\mu$ is the mean (center of the distribution)
- $\sigma$ is the standard deviation (controls the width)
- $\pi$ and $e$ are mathematical constants

## Properties

Some key properties of the Gaussian distribution:

1. **Symmetry**: The distribution is symmetric around the mean $\mu$
2. **68-95-99.7 Rule**: 
   - ~68% of data falls within $\mu \pm \sigma$
   - ~95% of data falls within $\mu \pm 2\sigma$
   - ~99.7% of data falls within $\mu \pm 3\sigma$

3. **Cumulative Distribution Function (CDF)**:

$$F(x) = \frac{1}{2}\left[1 + \text{erf}\left(\frac{x-\mu}{\sigma\sqrt{2}}\right)\right]$$

where $\text{erf}$ is the error function.

## Interactive Visualization

Below is an interactive visualization where you can adjust the mean ($\mu$) and standard deviation ($\sigma$) to see how the Gaussian distribution changes:

<div style="text-align: center; margin: 2em 0;">
  <canvas id="gaussianCanvas" width="600" height="400" style="border: 1px solid #ccc; background: white;"></canvas>
</div>

<div style="text-align: center; margin: 1em 0;">
  <div>
    <label>Mean (μ): <input type="range" id="muSlider" min="-5" max="5" step="0.1" value="0" style="width: 200px;"> <span id="muValue">0</span></label>
  </div>
  <div style="margin-top: 1em;">
    <label>Std Dev (σ): <input type="range" id="sigmaSlider" min="0.1" max="3" step="0.1" value="1" style="width: 200px;"> <span id="sigmaValue">1</span></label>
  </div>
</div>

<script>
  const canvas = document.getElementById('gaussianCanvas');
  const ctx = canvas.getContext('2d');
  const muSlider = document.getElementById('muSlider');
  const sigmaSlider = document.getElementById('sigmaSlider');
  const muValue = document.getElementById('muValue');
  const sigmaValue = document.getElementById('sigmaValue');

  function gaussian(x, mu, sigma) {
    const exponent = -Math.pow(x - mu, 2) / (2 * Math.pow(sigma, 2));
    return (1 / (sigma * Math.sqrt(2 * Math.PI))) * Math.exp(exponent);
  }

  function drawGaussian() {
    const mu = parseFloat(muSlider.value);
    const sigma = parseFloat(sigmaSlider.value);
    
    muValue.textContent = mu.toFixed(1);
    sigmaValue.textContent = sigma.toFixed(1);

    // Clear canvas
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw grid
    ctx.strokeStyle = '#e0e0e0';
    ctx.lineWidth = 1;
    for (let i = -5; i <= 5; i++) {
      const x = ((i - (-5)) / 10) * canvas.width;
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, canvas.height);
      ctx.stroke();
    }

    // Draw axes
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 2;
    const axisY = canvas.height * 0.8;
    ctx.beginPath();
    ctx.moveTo(0, axisY);
    ctx.lineTo(canvas.width, axisY);
    ctx.stroke();

    // Draw curve
    ctx.strokeStyle = '#2196F3';
    ctx.lineWidth = 2;
    ctx.beginPath();
    
    for (let px = 0; px < canvas.width; px++) {
      const xVal = -5 + (px / canvas.width) * 10;
      const y = gaussian(xVal, mu, sigma);
      const py = axisY - (y * canvas.height * 0.6);
      
      if (px === 0) {
        ctx.moveTo(px, py);
      } else {
        ctx.lineTo(px, py);
      }
    }
    ctx.stroke();

    // Draw labels
    ctx.fillStyle = '#000';
    ctx.font = '12px Arial';
    for (let i = -5; i <= 5; i++) {
      const x = ((i - (-5)) / 10) * canvas.width;
      ctx.fillText(i.toString(), x - 5, axisY + 20);
    }
  }

  muSlider.addEventListener('input', drawGaussian);
  sigmaSlider.addEventListener('input', drawGaussian);
  
  // Initial draw
  drawGaussian();
</script>

## Applications

Gaussian distributions are fundamental to many machine learning algorithms:

- **Linear Regression**: Assumes normally distributed residuals
- **Gaussian Processes**: A non-parametric approach using Gaussians
- **Variational Inference**: Uses Gaussian approximations
- **Neural Networks**: Weight initialization often assumes Gaussians

## Conclusion

Understanding the Gaussian distribution is crucial for anyone working in statistics, probability, or machine learning. The interactive visualization above helps build intuition about how the parameters affect the shape of the distribution.
