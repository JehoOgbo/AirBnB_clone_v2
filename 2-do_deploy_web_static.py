#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
import time


def do_deploy(archive_path):
    """function that distributes the archive""" 
    try:
        # get the filename
        # split using '/' and the last item is the filename
        filename = archive_path.split("/")[-1]

        # get the filename without the extension
        no_ext = filename.split(".")[0]

        # path is name of folder to uncompress the archive to
        path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run("mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp{} -C {}{}/".format(filename, path, no_ext))
        run("rm /tmp/{}".format(archive_path))
        run("rm /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current".format(no_ext)
    except Exception:
        return False
