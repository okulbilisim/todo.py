# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('todocli/todocli.py').read(),re.M).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-todocli",
    packages = ["todocli"],
    entry_points = {
        "console_scripts": ['todocli = todocli.todocli:main']
        },
    version = version,
    description = "Python command line todo application",
    long_description = long_descr,
    author = "Okulbilisim",
    author_email = "info@okulbilisim.com",
    url = "https://github.com/okulbilisim/todo.py",
    )
