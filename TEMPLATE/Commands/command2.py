#!/usr/bin/env python
from __future__ import print_function
# import
## batteries
import os
import sys
import logging
import argparse
## application
from TEMPLATE.misc import misc_func

# init funcs
def ParseArgs(test_args=None, subparsers=None, parents=[]):
    desc = 'Example command 2'
    epi = """DESCRIPTION:
    """
    if subparsers:
        parser = subparsers.add_parser('command2', description=desc,
                                       epilog=epi, parents=parents,
                                       formatter_class=argparse.RawTextHelpFormatter)
    else:
        parser = argparse.ArgumentParser(description=desc, epilog=epi,
                                         formatter_class=argparse.RawTextHelpFormatter)
    ## args
    parser.add_argument('input_file',
                        help = 'input file path')
    parser.add_argument('-s', '--str',  default = 'string', 
                        help = 'Example string param (default: %(default)s)')
    parser.add_argument('-b', '--bool',  action = 'store_true',
                        help = 'Example bool param (default: %(default)s)')

    # test args
    if test_args:
        args = parser.parse_args(test_args)
        return args

    return parser
