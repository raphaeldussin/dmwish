#!/usr/bin/env python

import pandas as pd
import subprocess as sp
import argparse
import os

user = os.environ.get("HOME")
wishfile = f"{user}/.dmget_wishlist"


def pydmwish(wishfiles):
    """ optimized dmget for a list of files

    PARAMETERS:
    -----------

    wishfiles: list of str
        files to retrieve

    """
    df = _create_database(wishfiles)
    _retrieve_files(df)
    return None


def _read_wishlist():
    """ read requested files from wishlist file """
    fid = open(wishfile, "r")
    wishfiles = fid.readlines()
    fid.close()
    return wishfiles


def _create_database(wishfiles):
    """ create a dataframe of all files and directories """
    data = []
    for f in wishfiles:
        f = f.replace("\n", "")
        fname = f.replace("/", " ").split()[-1]
        fdir = f.rstrip(fname)
        data.append([fdir, fname])
    # create dataframe
    df = pd.DataFrame(data, columns=["directory", "file"])
    return df


def _retrieve_files(df):
    """ run one dmget for each directory (optimized dmget) """
    alldirs = list(set(df["directory"]))
    for thisdir in alldirs:
        match = df.where(df["directory"] == thisdir)["file"].dropna(how="all")
        getfiles = list(match)
        check = _run_dmget(thisdir, getfiles)
    return None


def _list_files(df):
    """ list files in the wish list """
    alldirs = list(set(df["directory"]))
    for thisdir in alldirs:
        match = df.where(df["directory"] == thisdir)["file"].dropna(how="all")
        getfiles = list(match)
        print(">>> In directory:")
        print(f">>> {thisdir}")
        print(">>> get the files:")
        print(f">>> {getfiles}")
    return None


def _run_dmget(rep, files):
    """ get files from directory rep """
    cmd = ["nohup", "dmget", "-v", "-d", rep] + files + ["> /dev/null 2>&1 &"]
    cmd_str = " ".join(x for x in cmd)
    check = sp.check_call(cmd_str, shell=True)
    return None


def _clean_list():
    """ clean the wish list """
    check = sp.check_call(f"rm -f {wishfile}", shell=True)
    return None


def _add_to_wishlist(files):
    """ add files to wishlist """
    fid = open(f"{wishfile}", "a")
    for f in files:
        fid.write(f)
        fid.write("\n")
    fid.close()
    return None
