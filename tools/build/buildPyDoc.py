#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2011-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    buildPyDoc.py
# @author  Daniel Krajzewicz
# @author  Michael Behrisch
# @date    2011-10-20
# @version $Id$

"""
Generates pydoc files for all python libraries.
"""
from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import shutil
import pydoc
import types
from optparse import OptionParser
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import traci  # noqa
import sumolib  # noqa
from sumolib.miscutils import working_dir  # noqa


def pydoc_recursive(module):
    pydoc.writedoc(module)
    for submod in module.__dict__.values():
        if isinstance(submod, types.ModuleType) and submod.__name__.startswith(module.__name__):
            pydoc_recursive(submod)


optParser = OptionParser()
optParser.add_option("-p", "--pydoc-output", help="output folder for pydoc")
optParser.add_option("-c", "--clean", action="store_true", default=False, help="remove output dirs")
(options, args) = optParser.parse_args()

if options.pydoc_output:
    if options.clean:
        shutil.rmtree(options.pydoc_output, ignore_errors=True)
    os.mkdir(options.pydoc_output)
    with working_dir(options.pydoc_output):
        for module in (traci, sumolib):
            pydoc_recursive(module)