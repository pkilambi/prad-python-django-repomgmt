#!/usr/bin/env python
import os
import sys
import subprocess

SERVER_URL = "http://localhost/api/v1/"
USERNAME = "admin"
PASSWORD = "XXXX"
SOURCE = "./pkgsrc.txt"
REPO = "cisco"
SERIES = "grizzly"

def parse_datafiles(filename):
    with open(filename) as f:
        pkg_srcs = f.readlines()

    lines = [line.lstrip() for line in pkg_srcs]
    data = []
    for line in lines:
        data.append([line.strip() for line in line.split('|')[1:6]])
    return data


def run_command(command_args):
    """
    Execute system calls
    """
    proc = subprocess.Popen(command_args, shell=False)
    proc.communicate()


def create_package_source(name, code_url, pkg_url, flavor):
    run_command(["/home/prad/./repomgmt.py", "--username=%s" % USERNAME, "--password=%s" % PASSWORD, "--url=%s" % SERVER_URL,
                 "packagesource-create", name, code_url, pkg_url, flavor])


def add_subscription(repo=REPO, series=SERIES, pkgsrc_id=None):
    run_command(["/home/prad/./repomgmt.py", "--username=%s" % USERNAME, "--password=%s" % PASSWORD, "--url=%s" % SERVER_URL,
                 "subscription-create", repo, series, pkgsrc_id])


def remove_subscription(repo="cisco", series="grizzly", pkgsrc_id=None):
    run_command(["/home/prad/./repomgmt.py", "--username=%s" % USERNAME, "--password=%s" % PASSWORD, "--url=%s" % SERVER_URL,
                 "subscription-create", repo, series, pkgsrc_id])


def do_bulk(srcfile=SOURCE):
    if not os.path.exists(srcfile):
        print("Package Source output file [%s] missing" % srcfile)
        sys.exit(-1)
    sources = parse_datafiles(srcfile)
    for src in sources:
        create_package_source(src[1], src[2], src[3], src[4])
        print("Created pkg source %s" % src)
        add_subscription(pkgsrc_id=src[0])
        print "Subscribed Package Source", src

if __name__ == '__main__':
    do_bulk()
