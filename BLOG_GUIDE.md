# Blog Post Guide

This guide explains how to create and publish blog posts with math notation and interactive animations on your GitHub Pages site.

## Quick Start

### 1. Create a Markdown File

Create a new `.md` file in the `blog/` directory:

```bash
touch blog/my_awesome_post.md
```

### 2. Add Front Matter (Optional but Recommended)

Add metadata at the top of your markdown file:

```markdown
---
title: Your Blog Post Title
date: 2026-08-30
tags: machine-learning, tutorial, python
author: Your Name
---

# Your Blog Post Title

Your content here...
```

**Front matter fields:**
- `title`: Post title (also used in HTML page title)
- `date`: Publication date (YYYY-MM-DD format)
- `tags`: Comma-separated tags (displayed as colored badges)
- `author`: Author name (defaults to "Jaturong Kongmanee")

### 3. Write Your Content

Use standard Markdown with these enhancements:

#### Math Notation (LaTeX)

Inline math: `$E = mc^2$` renders as $E = mc^2$

Display math (block):
```markdown
$$\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$$
```

Renders as a centered equation block.

#### Embedded Scripts and Animations

You can embed HTML and JavaScript directly in your Markdown:

```html
<div style="text-align: center; margin: 2em 0;">
  <canvas id="myCanvas" width="400" height="300"></canvas>
</div>

<script>
  // Your JavaScript code here
  const canvas = document.getElementById('myCanvas');
  const ctx = canvas.getContext('2d');
  // Draw or animate something
</script>
```

### 4. Convert Markdown to HTML

Run the Python converter:

```bash
python3 md_coverter.py my_awesome_post.md
```

This will:
- Convert your Markdown to HTML
- Add MathJax support (renders LaTeX equations)
- Auto-generate a **table of contents** from your headers (right sidebar)
- Display **metadata** (date, author, tags) at the top
- Style tags as colored badges
- Include Bootstrap styling and professional layout
- Add a back link to the main page
- Create `blog/my_awesome_post.html`

**Output example:**
```
✓ Successfully converted intro_to_transformers.md to intro_to_transformers.html
  Title: A Gentle Introduction to Transformer Architecture
  Date: 2026-08-30
  Tags: deep-learning, nlp, attention-mechanism, transformers
```

### 4. Push to GitHub

```bash
git add blog/my_awesome_post.md blog/my_awesome_post.html
git commit -m "Add blog post: my_awesome_post"
git push origin master
```

Your post will be live at:
`https://jaturongkongmanee.github.io/website/blog/my_awesome_post.html`

## New Features

### ✨ Table of Contents (Right Sidebar)

Your blog posts now automatically display a **sticky table of contents** on the right side of the page:
- Auto-generated from your headings (h2-h6)
- Clickable links that jump to sections
- Sticky positioning (stays visible while scrolling)
- Responsive (moves below content on mobile)

Just use standard Markdown headers and the TOC is created automatically:

```markdown
## Section 1
## Section 2
### Subsection 2.1
```

### ✨ Metadata & Tags

Display post information professionally:
- **Date**: When the post was published
- **Author**: Who wrote it
- **Tags**: Topic categorization with colored badges

```markdown
---
title: My Post
date: 2026-08-30
tags: machine-learning, python, tutorial
author: Your Name
---
```

Tags appear as styled badges that can be clicked to filter (if you add that feature later).

### ✨ Professional Layout

The new template features:
- Two-column layout (content + sidebar)
- Modern, clean design inspired by high-quality tech blogs
- Better typography and spacing
- Responsive design (adapts to mobile)
- Code syntax highlighting
- Styled tables with hover effects

## Features

### ✅ Math Notation Support

- **Inline math**: `$formula$`
- **Display math**: `$$formula$$`
- Full LaTeX support via MathJax
- Common expressions:
  - `$\alpha, \beta, \gamma$` → Greek letters
  - `$\frac{a}{b}$` → Fractions
  - `$x^2$` → Superscripts
  - `$x_i$` → Subscripts
  - `$\sum_{i=1}^n x_i$` → Summation
  - `$\int_a^b f(x) dx$` → Integration

### ✅ Interactive Elements

- Canvas-based graphics
- Interactive sliders and inputs
- Animations
- Event listeners
- Real-time calculations

### ✅ Footnotes

Add footnotes in your text with `[^1]` markers and define them at the bottom:

```markdown
This is text with a footnote[^1].

More text here[^2].

[^1]: This is the first footnote content.
[^2]: This is the second footnote content.
```

**Features:**
- Superscript numbers appear in the text
- Clickable links to footnote definitions
- Footnotes appear at the end of the article
- Professional academic styling

### ✅ Code Blocks

Use triple backticks with language specification:

````markdown
```python
def hello():
    print("Hello, World!")
```
````

### ✅ Tables

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

## Example: Creating an Animation

Here's a template for creating an animated visualization:

```markdown
# My Animated Post

## Interactive Animation

<div style="text-align: center;">
  <canvas id="animCanvas" width="500" height="300" style="border: 1px solid #ccc;"></canvas>
</div>

<script>
  const canvas = document.getElementById('animCanvas');
  const ctx = canvas.getContext('2d');
  let t = 0;

  function animate() {
    // Clear canvas
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw something that changes with t
    ctx.fillStyle = 'blue';
    ctx.beginPath();
    ctx.arc(100 + 50 * Math.cos(t), 150 + 50 * Math.sin(t), 10, 0, 2 * Math.PI);
    ctx.fill();

    t += 0.02;
    requestAnimationFrame(animate);
  }

  animate();
</script>
```

## Example Files

- `blog/example_with_math_and_animation.md` - Interactive visualization example with:
  - Math notation
  - Interactive Gaussian distribution visualization
  - Canvas graphics
  - Sliders for parameter adjustment

- `blog/intro_to_transformers.md` - Complete tutorial example with:
  - Front matter (metadata + tags)
  - Professional layout with table of contents
  - Extensive math notation
  - Tables and code examples
  - Proper section structure

- `blog/math_notation_reference.md` - Reference guide featuring:
  - Comprehensive math notation catalog
  - Organized by category (Greek letters, calculus, linear algebra, etc.)
  - Real-world usage examples
  - Quick reference formulas

## Directory Structure

```
website/
├── blog/
│   ├── my_post.md           # Your markdown source
│   ├── my_post.html         # Generated HTML
│   ├── example_with_math_and_animation.md
│   └── example_with_math_and_animation.html
├── md_coverter.py           # Markdown to HTML converter
├── stylesheet.css           # Main styles
├── index.html              # Main page
└── BLOG_GUIDE.md           # This file
```

## Tips

1. **Write markdown first, convert second**: Keep your `.md` files as the source of truth. Regenerate `.html` when you make changes.

2. **Test locally**: If you have a local web server, test your HTML files before pushing.

3. **Math syntax**: Double-check LaTeX syntax. MathJax has good error messages in the browser console.

4. **Performance**: Complex animations may impact performance on slower devices. Test on mobile.

5. **Linking**: Use relative paths:
   - `[Link](../index.html)` for main page
   - `[Image](../images/photo.jpg)` for images

## Troubleshooting

### Math Not Rendering?

- Make sure you're using `$...$` for inline and `$$...$$` for display math
- Check that MathJax is loading (look in browser console for errors)
- Try reloading the page

### Canvas Not Showing?

- Check browser console for JavaScript errors
- Make sure canvas element has width and height attributes
- Test in a modern browser (Chrome, Firefox, Safari)

### Converter Not Working?

```bash
# Make sure you have markdown library installed
pip install markdown

# Then run
python md_coverter.py filename.md
```

## Advanced Features

### Adding Custom CSS

Modify the `HTML_TEMPLATE` in `md_coverter.py` to add custom styles in the `<style>` section.

### Using External Libraries

You can include any CDN-hosted library:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
```

Common choices:
- **Three.js**: 3D graphics
- **Plotly.js**: Interactive charts
- **D3.js**: Data visualization
- **Anime.js**: Animation library

### Responsive Design

The HTML template includes Bootstrap, so you can use Bootstrap classes:

```markdown
<div class="container">
  <div class="row">
    <div class="col-md-6">Column 1</div>
    <div class="col-md-6">Column 2</div>
  </div>
</div>
```

## Citations and References

### Adding a References Section

Include a References section at the end of your post for academic rigor:

```markdown
## References

[1] Vaswani, A., et al. (2017). "Attention Is All You Need." 
    *Advances in Neural Information Processing Systems (NeurIPS)*.
    Available: https://arxiv.org/abs/1706.03762

[2] Devlin, J., et al. (2018). "BERT: Pre-training of Deep Bidirectional 
    Transformers for Language Understanding." arXiv preprint arXiv:1810.04805.
    Available: https://arxiv.org/abs/1810.04805
```

### Citation Styles

**IEEE Style** (Engineering, Computer Science):
```
[1] A. Author, "Paper title," Journal Name, vol. 10, no. 5, pp. 123-145, 2020.
```

**APA Style** (Social Sciences):
```
Author, A. (2020). Paper title. Journal Name, 10(5), 123-145. 
https://doi.org/10.xxxx/xxxxx
```

**Chicago Style** (Humanities):
```
Author, A. "Paper Title." Journal Name 10, no. 5 (2020): 123-145.
```

### Recommended Resources

- **arXiv**: https://arxiv.org - Preprints in CS, math, physics
- **Google Scholar**: https://scholar.google.com - Academic search engine
- **PapersWithCode**: https://paperswithcode.com - ML papers with implementations
- **DOI Resolver**: https://doi.org - Find papers by DOI number

### Inline Citations

Reference citations in your text:

```markdown
This technique was introduced by Smith et al. [1] and later improved by 
Jones and Brown [2]. Recent work [3] suggests that...
```

## Publishing Checklist

Before pushing to GitHub:

- [ ] Wrote content in `blog/your_post.md`
- [ ] Added front matter (title, date, tags, author)
- [ ] Ran `python3 md_coverter.py your_post.md`
- [ ] Tested `blog/your_post.html` in a browser
- [ ] Math renders correctly
- [ ] Table of contents generated properly
- [ ] Interactive elements work
- [ ] Links work and are relative paths
- [ ] No broken images or resources
- [ ] Citations and references included
- [ ] Grammar and spelling checked

Enjoy writing!
