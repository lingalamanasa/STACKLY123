import os, glob, shutil

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('<script src="js/script.js"></script>', '')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

shutil.rmtree('js', ignore_errors=True)
