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

    if (not os.path.exists(archive_path)):
        return False

    if not put(archive_path, "/tmp/").succeeded:
        return False

    # Extracting archive file name from the path
    archive_file = archive_path.split('/')[-1]

    # Get the new folder name that we will uncompress the archive to it
    static_content_folder = archive_file[:-4]

    folder_abs_path = "/data/web_static/releases/" + static_content_folder
    if not sudo("mkdir -p {}".format(folder_abs_path)).succeeded:
        return False

    with cd(folder_abs_path):
        if not sudo("tar -xzf /tmp/{}".format(archive_file)).succeeded:
            return False

        if not sudo("mv web_static/* .").succeeded:
            return False

        if not sudo("rm -r web_static/").succeeded:
            return False

    if not sudo("rm /tmp/{}".format(archive_file)).succeeded:
        return False

    if not sudo("rm -r /data/web_static/current").succeeded:
        return False

    if not sudo("ln -sf {} /data/web_static/current"
                .format(folder_abs_path)).succeeded:
        return False

    return True
