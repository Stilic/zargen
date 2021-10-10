import markdown
from glob import glob
from pathlib import Path
import os

CONTENT_PATH = "./docs"
DIST_PATH = "./_site"
if not os.path.isdir(DIST_PATH):
    os.mkdir(DIST_PATH)
os.chdir(CONTENT_PATH)

for file in glob("./**/*.md", recursive=True):
    with open(file, "r") as original:
        os.chdir(os.path.join("..", DIST_PATH))
        path = os.path.normpath(Path(file).with_suffix("")) + ".html"
        dirpath = os.path.split(path)[0]
        if dirpath != "":
            if not os.path.isdir(dirpath):
                os.mkdir(dirpath)
        open(path, "w").write(markdown.markdown(original.read()))
        os.chdir(os.path.join("..", CONTENT_PATH))
