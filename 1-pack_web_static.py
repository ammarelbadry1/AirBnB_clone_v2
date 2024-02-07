#!/usr/bin/python3
"""This module contains a function that package the web_static folder"""
from fabric.api import *


def do_pack():
    """contains the shell script commands that generates
    a .tgz archive from the contents of the web_static folder."""

    local("mkdir -p versions")
    result = local("tar -czvf versions/\
web_static_$(date '+%y%m%d%H%M%S').tgz web_static/")

    if (result.succeeded):
        with lcd("versions/"):
            realpath = local("realpath $(ls)")
            return realpath
    return None
