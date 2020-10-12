#!/usr/bin/env python3.8
import bundle
import sys
from logging import getLogger, basicConfig, INFO
basicConfig(level=INFO)
bundle.main(sys.argv[1:])
