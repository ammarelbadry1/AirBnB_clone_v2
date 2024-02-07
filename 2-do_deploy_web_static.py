#!/usr/bin/python3
"""This script distributes web_static archive to web servers"""
import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['34.229.66.147', '18.234.145.189']


def do_deploy(archive_path):
    """Distributes web_static archive to web servers

    Args:
        archive_path (str): the path to the archived file
    """

    if not os.path.exists(archive_path):
        return False

    if not put(archive_path, "/tmp/").succeeded:
        return False

    # Extracting archive file name from the path
    archive_file = archive_path.split('/')[-1]

    # Get the new folder name that we will uncompress the archive to it
    static_content_folder = archive_file[:-4]

    folder_abs_path = "/data/web_static/releases/" + static_content_folder
    if not run("mkdir -p {}".format(folder_abs_path)).succeeded:
        return False

    if not run("tar -xzf /tmp/{} -C {}"
               .format(archive_file, folder_abs_path)).succeeded:
        return False

    if not run("mv {}/web_static/* {}"
               .format(folder_abs_path, folder_abs_path)).succeeded:
        return False

    if not run("rm -rf {}/web_static/".format(folder_abs_path)).succeeded:
        return False

    if not run("rm /tmp/{}".format(archive_file)).succeeded:
        return False

    if not run("rm -rf /data/web_static/current").succeeded:
        return False

    if not run("ln -sf {} /data/web_static/current"
               .format(folder_abs_path)).succeeded:
        return False

    return True
