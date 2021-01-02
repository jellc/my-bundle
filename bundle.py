import onlinejudge_bundle
import sys
import os
import subprocess
import glob
import pathlib
from logging import getLogger, INFO, basicConfig
logger = getLogger(__name__)


def main(args):
    if not len(args):
        logger.error('\033[31m' + " no source file specified.")
        sys.exit(1)

    workpath = os.path.expanduser('~')
    libs = ["-I", os.path.expanduser('~/Library'), "-I", os.path.expanduser('~/ac-library')]

    abspath = os.path.abspath(args[0])
    if abspath.startswith('/cygdrive/c/cygwin64/'):
        abspath = abspath[len('/cygdrive/c/cygwin64'):]

    cmd = ["oj-bundle", str(pathlib.Path(abspath).relative_to(pathlib.Path(workpath)))] + libs

    if len(args) > 1:
        stdout = args[1]
        with open(args[1], "w") as out:
            exit_stat = subprocess.call(cmd, cwd=workpath, stdout=out, stderr=subprocess.DEVNULL)
        logger.info(" {} -> {}".format(args[0], stdout))
    else:
        exit_stat = subprocess.call(cmd, cwd=workpath, stdout=None, stderr=subprocess.DEVNULL)

    return exit_stat
