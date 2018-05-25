﻿
# module list to test
modulelist = ['numpy', 'matplotlib', 'shutil', 'subprocess', 
              'pandas', 'platform', 'shapefile', 'flopy']

import os
import sys
import shutil
import importlib

dpth = 'temp'
if os.path.exists(dpth):
    shutil.rmtree(dpth)
os.makedirs(dpth)

def printmsg(msg):
    print(msg)
    return


def eval_module(m):
    try:
        msg = '  Module available for use: {}'.format(m)
        importlib.import_module(m)
        printmsg(msg)
    except Exception:
        msg = '  Error.  Could not import module: ' + m
        assert False, msg
    return

    
def test_anaconda():
    msg = '  Evaluating system information'
    printmsg(msg)
    sys_version = sys.version
    print('  Your python version: ', sys.version)
    if 'anaconda' not in sys_version.lower() and \
    'conda-forge' not in sys_version.lower() and \
    'miniconda' not in sys_version.lower():
        msg = '  Warning.  Your system version of python ' + \
              'is not Anaconda variant.'
        assert False, msg
    return
    
    
def test_modules():
    for m in modulelist:
        yield eval_module, m
    return


def test_matplotlib():    
    msg = '  Testing matplotlib installation'
    printmsg(msg)
    fpth = os.path.join('temp', 'randomfield.png')
    try:
        from matplotlib import pyplot as plt
        import numpy as np
        a = np.random.random(size=(100,100))
        plt.imshow(a, interpolation='nearest')
        plt.savefig(fpth)
    except:
        msg = '  Error.  Could not create a matplotlib plot.'
        assert False, msg
    
    msg = '  Error.  Could not create a matplotlib figure.'
    assert os.path.isfile(fpth), msg
    return
        

if __name__ == "__main__":
    
    # test that this is a version of Anaconda
    test_anaconda()
    
    # evaluate installed modules
    for m in modulelist:
        eval_module(m)
        
    # evaluate matplotlib
    test_matplotlib()
    
        
    
