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

    path_tkns = archive_path.split('/')
    our_folder = path_tkns[-1][:-4]
    put(archive_path, "/tmp/")
    abs_path = "/data/web_static/releases/" + our_folder
    create_dir = "mkdir -p " + abs_path
    change_dir = "cd " + abs_path
    sudo(create_dir)
    with cd(abs_path):
        abs_path2 = "/tmp/" + path_tkns[-1]
        uncompress = "tar -xvzf " + abs_path2
        sudo(uncompress)
        remove_archive = "rm /tmp/" + path_tkns[-1]
        sudo(remove_archive)
        sudo("rm -r /data/web_static/current")
        create_symlink = "ln -sf " + abs_path + " /data/web_static/current"
        sudo(create_symlink)
    return True
