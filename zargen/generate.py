from glob import glob
from pathlib import Path
import os
from time import time

startTime = time()
from shutil import rmtree, copyfile

import markdown
import yaml
from .utils import BadConfigurationError


def generate():
    """Generates the content for the final site."""
    print("Generating the content...")
    try:
        config = yaml.load(open("_config.yml", "r").read(), Loader=yaml.FullLoader)
    except:
        config = {
            "content_path": "./docs",
            "out_path": "./_site",
        }
    if not os.path.isdir(config["content_path"]):
        raise BadConfigurationError(
            "The content directory '{0}' doesn't exist.".format(config["content_path"])
        )
    if os.path.isdir(config["out_path"]):
        rmtree(config["out_path"])
    os.mkdir(config["out_path"])
    os.chdir(config["content_path"])

    files_counter = 0
    for file in glob("./**/*", recursive=True):
        files_counter += 1
        path = os.path.normpath(Path(file).with_suffix("")) + ".html"
        if not os.path.isdir(file):
            with open(file, "r") as original:
                os.chdir(os.path.join("..", config["out_path"]))
                dirpath = os.path.split(path)[0]
                if dirpath != "":
                    if not os.path.isdir(dirpath):
                        os.mkdir(dirpath)
                print(path)
                if os.path.splitext(file)[1] == ".md":
                    print("yes")
                    open(path, "w").write(markdown.markdown(original.read()))
                else:
                    copyfile(os.path.join("..", config["content_path"], file), path)
                os.chdir(os.path.join("..", config["content_path"]))
        else:
            files_counter -= 1

    print(
        """
    Finished!
    Number of files processed: {0}
    Time for finish: {1}""".format(
            files_counter, time() - startTime
        )
    )
