#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, os

changelog = "debian/changelog"
if os.path.exists(changelog):
    head = open(changelog).readline()
    try:
        version = head.split("(")[1].split(")")[0]
    except:
        print("debian/changelog format is wrong for get version")
        version = ""
    f = open("src/__version__", "w")
    f.write(version)
    f.close()

data_files = [
    ("/usr/share/applications", ["tr.org.daft-8.debpakir.desktop"]),
    ("/usr/share/locale/tr/LC_MESSAGES", ["po/tr/debpakir.mo"]),
    ("/usr/share/daft-8/debpakir/ui", ["ui/MainWindow.glade"]),
    ("/usr/share/daft-8/debpakir/src",
     ["src/Actions.py", "src/main.py", "src/MainWindow.py", "src/__version__"]),
    ("/usr/bin", ["debpakir"]),
    ("/usr/share/polkit-1/actions", ["tr.org.daft-8.pkexec.debpakir.policy"]),
    ("/usr/share/icons/hicolor/scalable/apps/", ["images/debpakir.svg"])
]

setup(
    name="DEBian PacKage InstalleR",
    version=version,
    packages=find_packages(),
    scripts=["debpakir"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Fatih Altun",
    author_email="",
    description="Manage and view .deb packages.",
    license="GPLv3",
    keywords="deb package installer",
    url="https://www.github.com/DAFT-8/debpakir",
)
