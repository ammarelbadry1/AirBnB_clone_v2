#!/usr/bin/python3
"""This module contains function that deploy our static files."""
import os
from fabric.api import *


env.user = 'ubuntu'
env.hosts = ['18.234.145.189', '34.229.66.147']


def deploy():
    """Deploys our static files using old functions"""

    do_pack = __import__('1-pack_web_static').do_pack
    do_deploy = __import__('2-do_deploy_web_static').do_deploy

    archive_path = do_pack()
    if (not archive_path):
        return False

    result = do_deploy(archive_path)
    return result
