# md_test.py
# tests the markdown module
# converts any markdown text into html

import markdown
# import os.sys

# f = open('README.md')
with open("README.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()
html = markdown.markdown(text)
print(html)