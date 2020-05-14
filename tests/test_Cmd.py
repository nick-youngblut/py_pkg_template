# import
## batteries
import os
import sys
import pytest

# test/data dir
test_dir = os.path.join(os.path.dirname(__file__))
data_dir = os.path.join(test_dir, 'data')

def test_cmd1_help(script_runner):
    ret = script_runner.run('TEMPLATE', 'command1', '-h')
    assert ret.success

def test_cmd2_help(script_runner):
    ret = script_runner.run('TEMPLATE', 'command2', '-h')
    assert ret.success
