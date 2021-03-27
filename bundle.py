import sys
import os
import subprocess
import pathlib
from logging import getLogger
logger = getLogger(__name__)

logf = '.bundlelog'


def main(args):
    if not len(args):
        logger.error('\033[31m' + " No source file specified.")
        sys.exit(1)

    workpath = os.path.expanduser('~')
    libs = ["-I", os.path.expanduser('~/Library'), "-I", os.path.expanduser('~/ac-library')]

    abspath = os.path.abspath(args[0])
    if abspath.startswith('/cygdrive/c/cygwin64/'):
        abspath = abspath[len('/cygdrive/c/cygwin64'):]

    cmd = ["oj-bundle", str(pathlib.Path(abspath).relative_to(pathlib.Path(workpath)))] + libs

    if len(args) > 1:
        stdout = args[1]
        with open(args[1], 'w') as out, open(logf, 'w') as err:
            exit_stat = subprocess.call(cmd, cwd=workpath, stdout=out, stderr=err)
        if exit_stat:
            with open(logf, 'r') as err:
                for msg in err.readlines():
                    logger.info(msg)
        else:
            logger.info(" {} -> {}".format(args[0], stdout))

    else:
        with open(logf, 'w') as err:
            exit_stat = subprocess.call(cmd, cwd=workpath, stdout=None, stderr=err)
        if exit_stat:
            with open(logf, 'r') as err:
                for msg in err.readlines():
                    logger.info(msg)

    os.remove(logf)

    return exit_stat
