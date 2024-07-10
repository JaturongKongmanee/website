import markdown

MD_FILE_NAME = 'hypo'

PATH = './blog/'

with open(PATH + f'{MD_FILE_NAME}.md', 'r') as f:
    temp_md = f.read()

temp_html = markdown.markdown(temp_md)

with open(PATH + f'{MD_FILE_NAME}.html', 'w') as f:
    f.write(temp_html)
