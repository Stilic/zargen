import markdown
from glob import glob
from pathlib import Path
import os
from shutil import rmtree
import yaml

config = yaml.load(open("_config.yml", "r").read(), Loader=yaml.FullLoader) or {"content_path": "./docs", "out_path": "./_site"}
if os.path.isdir(config["out_path"]):
    rmtree(config["out_path"])
os.mkdir(config["out_path"])
os.chdir(config["content_path"])

for file in glob("./**/*.md", recursive=True):
    with open(file, "r") as original:
        os.chdir(os.path.join("..", config["out_path"]))
        path = os.path.normpath(Path(file).with_suffix("")) + ".html"
        dirpath = os.path.split(path)[0]
        if dirpath != "":
            if not os.path.isdir(dirpath):
                os.mkdir(dirpath)
        open(path, "w").write(markdown.markdown(original.read()))
        os.chdir(os.path.join("..", config["content_path"]))
