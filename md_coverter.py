import markdown
import sys

LINK_TO_MAIN_PAGE = '<a class="link" href="https://jaturongkongmanee.github.io/website/"><input type="button" value="Back to the main page"></a>'
PATH = './blog/'


if len(sys.argv) == 1:
    print('You have to provide a markdown file you want to convert to HTML file!')
    sys.exit()

file_name, file_type = sys.argv[1].split(".")

if file_type == 'md':
    file_name
else:
    print('You have to provide .md file')
    sys.exit()


with open(PATH + f'{file_name}.md', 'r') as f:
    temp_md = f.read()

temp_html = markdown.markdown(temp_md)
temp_html = LINK_TO_MAIN_PAGE + temp_html

with open(PATH + f'{file_name}.html', 'w') as f:
    f.write(temp_html)



