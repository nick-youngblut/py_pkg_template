#!/usr/bin/env python
from __future__ import print_function
# import
## batteries
import os
import sys
import glob
import logging
import argparse
## application
from TEMPLATE.__init__ import __version__
from TEMPLATE.Commands import command1 as command1_cmd
from TEMPLATE.Commands import command2 as command2_cmd

# logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

# function init
def main(args = None):
    #parser
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-v', '--version', action = 'version', version = __version__)
    ## parent parsers
    ### general
    parent1_p = argparse.ArgumentParser(add_help=False)
    parent1_p.add_argument('-c', '--cpus', type = int, default = 1,
                           help='CPUs used for parallel execution' + \
                           ' (default: %(default)s)')
    # Defining subparsers
    subparsers = parser.add_subparsers()
    ## example cmd1
    command1_cmd.ParseArgs(subparsers=subparsers, parents=[parent1_p])
    ## example cmd2
    command2_cmd.ParseArgs(subparsers=subparsers)

    # unit test args or command line?
    if args:
        args = parser.parse_args(args)
    else:
        args = parser.parse_args()

    # running subcommands
    if len(vars(args)) > 0:
        args.func(args)
    else:
        parser.parse_args(['--help'])
            
if __name__ == "__main__":
    main()
