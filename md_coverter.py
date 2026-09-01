import markdown
import sys
import re
from markdown.extensions import tables, fenced_code, toc, footnotes
from datetime import datetime

LINK_TO_MAIN_PAGE = '<a class="link" href="https://jaturongkongmanee.github.io/website/"><input type="button" value="Back to the main page"></a>'
PATH = './blog/'

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="../stylesheet.css">
    <link href="https://fonts.cdnfonts.com/css/iowanoldst-bt" rel="stylesheet">
    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            font-family: 'IowanOldSt BT', Georgia, serif;
            line-height: 1.6;
            color: #333;
            background: #fafafa;
        }}

        .blog-container {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 20px;
        }}

        .back-link {{
            margin-bottom: 2em;
        }}

        .blog-wrapper {{
            display: grid;
            grid-template-columns: 150px 1fr 180px;
            gap: 30px;
            margin-bottom: 3em;
        }}

        article {{
            order: 2;
        }}

        .toc-sidebar {{
            order: 1;
        }}

        .sidenote-column {{
            order: 3;
            position: relative;
        }}

        @media (max-width: 900px) {{
            .blog-wrapper {{
                grid-template-columns: 1fr;
            }}
            article {{
                order: 0;
            }}
            .toc-sidebar {{
                order: 0;
            }}
            .toc-sidebar {{
                position: static;
                margin-top: 3em;
                padding: 20px;
                background: #f9f9f9;
                border-radius: 5px;
            }}
        }}

        article {{
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        }}

        .post-header {{
            margin-bottom: 2em;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 1.5em;
        }}

        .post-title {{
            font-size: 2.5em;
            font-weight: 700;
            margin: 0 0 0.3em 0;
            color: #2c3e50;
            line-height: 1.2;
        }}

        .post-meta {{
            color: #7f8c8d;
            font-size: 0.95em;
            margin-bottom: 1em;
            line-height: 1.6;
        }}

        .post-tags {{
            display: flex;
            gap: 0.5em;
            flex-wrap: wrap;
            margin-top: 2em;
            margin-bottom: 2em;
            padding-top: 1.5em;
            border-top: 1px solid #ecf0f1;
        }}

        .tag {{
            display: inline-block;
            background: #e8f4f8;
            color: #2980b9;
            padding: 0.3em 0.8em;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 500;
            text-decoration: none;
            border: 1px solid #b8dbe8;
            transition: all 0.2s ease;
        }}

        .tag:hover {{
            background: #2980b9;
            color: white;
            border-color: #2980b9;
        }}

        h1, h2, h3, h4, h5, h6 {{
            margin-top: 1.8em;
            margin-bottom: 0.6em;
            font-weight: 700;
            color: #2c3e50;
            line-height: 1.3;
        }}

        h1 {{
            font-size: 2em;
        }}

        h2 {{
            font-size: 1.6em;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 0.5em;
        }}

        h3 {{
            font-size: 1.3em;
        }}

        h4 {{
            font-size: 1.1em;
        }}

        p {{
            margin: 1em 0;
        }}

        code {{
            background: #fcdfd9;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: #c7254e;
        }}

        pre {{
            background: #fcdfd9;
            color: #333;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            line-height: 1.4;
            margin: 1.5em 0;
        }}

        pre code {{
            background: none;
            padding: 0;
            color: #333;
        }}

        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 1em;
            margin-left: 0;
            color: #7f8c8d;
            font-style: italic;
        }}

        img {{
            max-width: 100%;
            height: auto;
            margin: 1.5em 0;
            border-radius: 5px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5em 0;
        }}

        table thead {{
            background: #ecf0f1;
        }}

        table th {{
            padding: 0.8em;
            text-align: left;
            font-weight: 600;
            color: #2c3e50;
        }}

        table td {{
            padding: 0.8em;
            border-bottom: 1px solid #ecf0f1;
        }}

        table tbody tr:hover {{
            background: #f9f9f9;
        }}

        a {{
            color: #3498db;
            text-decoration: none;
            transition: color 0.2s ease;
        }}

        a:hover {{
            color: #2980b9;
            text-decoration: underline;
        }}

        /* Table of Contents Sidebar */
        .toc-sidebar {{
            position: sticky;
            top: 20px;
            height: fit-content;
            max-height: calc(100vh - 40px);
            overflow-y: auto;
        }}

        .toc-content {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        }}

        .toc-title {{
            font-size: 1.1em;
            font-weight: 700;
            margin-bottom: 1em;
            color: #2c3e50;
            display: flex;
            align-items: center;
            gap: 0.5em;
        }}

        .toc-content ul {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}

        .toc-content li {{
            margin: 0.4em 0;
        }}

        .toc-content a {{
            display: block;
            padding: 0.4em 0.8em;
            border-radius: 3px;
            font-size: 0.8em;
            color: #7f8c8d;
            transition: all 0.2s ease;
        }}

        .toc-content a:hover {{
            background: #f0f0f0;
            color: #333;
        }}

        .toc-content ul ul {{
            margin-left: 1em;
            border-left: 2px solid #ecf0f1;
            padding-left: 0.5em;
        }}

        .toc-content ul ul a {{
            font-size: 0.75em;
            color: #7f8c8d;
        }}

        /* Canvas and interactive elements */
        canvas {{
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            background: white;
        }}

        input[type="range"] {{
            width: 100%;
            cursor: pointer;
        }}

        input[type="button"] {{
            padding: 0.6em 1.2em;
            background: #fcdfd9;
            color: #333;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 500;
            transition: background 0.2s ease;
        }}

        input[type="button"]:hover {{
            background: #f5b5a0;
        }}

        /* Footnotes styling */
        .footnote {{
            font-size: 0.9em;
            color: #7f8c8d;
        }}

        .footnotes {{
            border-top: 1px solid #ecf0f1;
            margin-top: 2em;
            padding-top: 1em;
            font-size: 0.9em;
            color: #7f8c8d;
        }}

        .footnotes ol {{
            margin: 0;
            padding-left: 1.5em;
        }}

        .footnotes li {{
            margin-bottom: 0.5em;
            line-height: 1.5;
        }}

        .footnotes p {{
            margin: 0;
            display: inline;
        }}

        sup a {{
            color: #3498db;
            margin: 0 2px;
            font-size: 0.85em;
        }}

        sup a:hover {{
            color: #2980b9;
        }}

        /* Sidenotes - positioned in right column */
        .footnote {{
            display: none;
        }}

        .sidenote {{
            position: absolute;
            width: 200px;
            font-size: 0.75em;
            color: #7f8c8d;
            line-height: 1.5;
            padding: 0.5em;
            margin-bottom: 1em;
            border-left: 2px solid #ecf0f1;
            padding-left: 0.8em;
        }}

        .sidenote-num {{
            font-weight: 700;
            color: #3498db;
            margin-right: 0.3em;
        }}

        @media (max-width: 1100px) {{
            .sidenote {{
                display: none;
            }}
        }}

        /* Giscus Comments Section */
        .giscus-container {{
            margin-top: 3em;
            padding-top: 2em;
            border-top: 2px solid #ecf0f1;
        }}
    </style>
    <!-- MathJax for LaTeX/Math notation -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const footnoteDiv = document.querySelector('.footnote');
            const sidenoteColumn = document.querySelector('.sidenote-column');
            const article = document.querySelector('article');
            if (!footnoteDiv || !sidenoteColumn || !article) return;

            const footnotes = footnoteDiv.querySelectorAll('li');
            const sidenotes = [];
            const articleTop = article.offsetTop;

            // First pass: create all sidenotes
            footnotes.forEach((fn, index) => {{
                const id = fn.id;
                const ref = document.querySelector('a[href="#' + id + '"]');

                if (ref) {{
                    // Create sidenote
                    const sidenote = document.createElement('div');
                    sidenote.className = 'sidenote';

                    // Get the number from the reference
                    const num = ref.textContent;

                    // Get footnote text (remove backref)
                    const textContent = fn.cloneNode(true);
                    const backref = textContent.querySelector('.footnote-backref');
                    if (backref) backref.remove();
                    const text = textContent.textContent.trim();

                    sidenote.innerHTML = '<span class="sidenote-num">' + num + '.</span> ' + text;

                    // Position sidenote based on reference location relative to article top
                    const refRect = ref.getBoundingClientRect();
                    const refPos = refRect.top + window.scrollY - articleTop;
                    sidenote.style.top = refPos + 'px';

                    // Insert into sidenote column
                    sidenoteColumn.appendChild(sidenote);

                    // Store sidenote info for overlap detection
                    sidenotes.push({{
                        element: sidenote,
                        refPos: refPos
                    }});
                }}
            }});

            // Second pass: adjust positions to avoid overlap
            sidenotes.forEach((sn, i) => {{
                const sidenote = sn.element;
                const sidenoteHeight = sidenote.offsetHeight || 100;
                let desiredTop = sn.refPos;

                // Check overlap with previous sidenotes
                for (let j = 0; j < i; j++) {{
                    const prevSn = sidenotes[j];
                    const prevTop = parseFloat(prevSn.element.style.top);
                    const prevHeight = prevSn.element.offsetHeight || 100;
                    const prevBottom = prevTop + prevHeight + 10; // 10px gap

                    // If this sidenote would overlap, move it down
                    if (desiredTop < prevBottom) {{
                        desiredTop = prevBottom;
                    }}
                }}

                sidenote.style.top = desiredTop + 'px';
            }});
        }});
    </script>
</head>
<body>
    <div class="blog-container">
        <div class="blog-wrapper">
            <article>
                <div class="post-header">
                    <h1 class="post-title">{title}</h1>
                    <div class="post-meta">
                        {meta_info}
                    </div>
                </div>
                {content}
                {tags_html}
            </article>

            <aside class="toc-sidebar">
                <div class="toc-content">
                    {toc_html}
                </div>
            </aside>

            <aside class="sidenote-column"></aside>
        </div>

        <div class="giscus-container">
            <script src="https://giscus.app/client.js"
                    data-repo="JaturongKongmanee/website"
                    data-repo-id="R_kgDOIuZQJg"
                    data-category="Announcements"
                    data-category-id="DIC_kwDOIuZQJs4DEniS"
                    data-mapping="pathname"
                    data-strict="0"
                    data-reactions-enabled="1"
                    data-emit-metadata="0"
                    data-input-position="bottom"
                    data-theme="preferred_color_scheme"
                    data-lang="en"
                    crossorigin="anonymous"
                    async>
            </script>
        </div>

        <div class="back-link">
            {back_link}
        </div>
    </div>
</body>
</html>'''


def parse_frontmatter(content):
    """Parse YAML-style frontmatter from markdown."""
    if not content.startswith('---'):
        return {}, content

    lines = content.split('\n')
    end_marker = -1

    for i in range(1, len(lines)):
        if lines[i].startswith('---'):
            end_marker = i
            break

    if end_marker == -1:
        return {}, content

    frontmatter = {}
    for line in lines[1:end_marker]:
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    body = '\n'.join(lines[end_marker + 1:])
    return frontmatter, body


def extract_headings(html):
    """Extract headings from HTML for table of contents."""
    heading_pattern = r'<h([2-6]) id="([^"]*)"[^>]*>([^<]+)</h\1>'
    headings = re.findall(heading_pattern, html)

    if not headings:
        return ""

    toc_html = '<ul>'
    current_level = 2

    for level, heading_id, heading_text in headings:
        level = int(level)

        if level > current_level:
            toc_html += '<ul>' * (level - current_level)
        elif level < current_level:
            toc_html += '</ul>' * (current_level - level)

        current_level = level
        toc_html += f'<li><a href="#{heading_id}">{heading_text}</a></li>'

    toc_html += '</ul>' * (current_level - 2) + '</ul>'
    return toc_html


def generate_toc_extension():
    """Generate table of contents with proper IDs."""
    return toc.TocExtension(
        permalink=False,
        title='Table of Contents',
        slugify=lambda value, separator: re.sub(r'[^\w\s-]', '', value).strip().lower().replace(' ', '-')
    )


if len(sys.argv) == 1:
    print('Usage: python md_coverter.py <filename>.md')
    print('Example: python md_coverter.py my_post.md')
    print('\nFrontmatter format (optional):')
    print('---')
    print('title: My Blog Post Title')
    print('date: 2026-08-30')
    print('tags: machine-learning, python, tutorial')
    print('author: Your Name')
    print('---')
    print('\nYour markdown content here...')
    sys.exit()

file_name, file_type = sys.argv[1].split(".")

if file_type != 'md':
    print('You have to provide a .md file')
    sys.exit()

with open(PATH + f'{file_name}.md', 'r') as f:
    raw_content = f.read()

# Parse frontmatter
frontmatter, markdown_content = parse_frontmatter(raw_content)

# Extract metadata
title = frontmatter.get('title', file_name.replace('_', ' ').title())
date_str = frontmatter.get('date', datetime.now().strftime('%Y-%m-%d'))
tags = frontmatter.get('tags', '').split(',') if frontmatter.get('tags') else []
author = frontmatter.get('author', 'Jaturong Kongmanee')

# Convert markdown to HTML with footnotes support
extensions = ['tables', 'fenced_code', 'footnotes', generate_toc_extension()]
html_content = markdown.markdown(markdown_content, extensions=extensions)

# Calculate reading time (assuming 200 words per minute)
word_count = len(markdown_content.split())
reading_time = max(1, round(word_count / 200))

# Format date (parse and reformat to "Month Day, Year")
try:
    parsed_date = datetime.strptime(date_str, '%Y-%m-%d')
    formatted_date = parsed_date.strftime('%B %d, %Y')
except:
    formatted_date = date_str

# Extract and generate table of contents
toc_html = extract_headings(html_content)
if not toc_html:
    toc_html = '<p style="color: #999; font-size: 0.8em;">No sections found</p>'

# Build metadata info in new format
meta_info = f'Date: {formatted_date}'
if reading_time:
    meta_info += f' | Estimated Reading Time: {reading_time} min'
if author:
    meta_info += f' | Author: {author}'

# Build tags HTML
tags_html = ''
if tags:
    tags_html = '<div class="post-tags">'
    for tag in tags:
        tag = tag.strip()
        if tag:
            tags_html += f'<span class="tag">{tag}</span>'
    tags_html += '</div>'

# Create full HTML
full_html = HTML_TEMPLATE.format(
    title=title,
    content=html_content,
    back_link=LINK_TO_MAIN_PAGE,
    meta_info=meta_info,
    tags_html=tags_html,
    toc_html=toc_html
)

with open(PATH + f'{file_name}.html', 'w') as f:
    f.write(full_html)

print(f'✓ Successfully converted {file_name}.md to {file_name}.html')
print(f'  Title: {title}')
print(f'  Date: {formatted_date}')
print(f'  Reading Time: {reading_time} min')
if tags:
    print(f'  Tags: {", ".join([t.strip() for t in tags])}')
