#!/usr/bin/python3
"""This module contains a function that package the web_static folder"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """contains the shell script commands that generates
    a .tgz archive from the contents of the web_static folder."""

    if not local("mkdir -p versions").succeeded:
        return None

    dt = datetime.utcnow()
    dt = "{}{}{}{}{}{}".format(dt.year, dt.month, dt.day,
                               dt.hour, dt.minute, dt.second)
    target_path = "versions/web_static_{}.tgz".format(dt)
    if not local("tar -czvf {} web_static".format(target_path)).succeeded:
        return None

    return target_path
