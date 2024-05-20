#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-SP-5"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["NGC_4038S"] = [ 112223, 112225, 112227, 112231, 112251, 112253, 112255,
                    112261, 112263, 112265, 112506, 112508, 112510, 112512,
                    112833, 112835, 112837, 112936, 112938, 112940, 112942,
                    112944, 112946, 112948, 112950, 112952, 113071, 113073,
                    113075, 113105, 113107, 113109,
                    113289, 113291, 113293, 113327,
                    113428, 113430, 113432, 113434,
                    116982, 116986, 116988, 116990, 116992, 116996, 116998,
                    117000, 119365, 119367, 119370,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["NGC_4038S"] = "extent=200 pix_list=-13,14,15 qagrade=1"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["NGC_4038S"] = "bank=0 pix_list=-13 qagrade=2"

#
pars3 = {}
pars3["NGC_4038S"] = "bank=1 pix_list=-13,14,15 qagrade=3"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
