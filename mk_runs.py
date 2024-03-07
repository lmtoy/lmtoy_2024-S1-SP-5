#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-SP-5"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["NGC_4038S"] = [ 112223, 112225, 112227, 112231, 112251, 112253, 112255,
                    112261, 112263, 112265,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["NGC_4038S"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["NGC_4038S"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
