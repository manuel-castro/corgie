from copy import deepcopy

COMMAND_LIST = []

from corgie.cli.downsample import downsample
COMMAND_LIST.append(downsample)
from corgie.cli.upsample import upsample
COMMAND_LIST.append(upsample)
from corgie.cli.compute_field import compute_field
COMMAND_LIST.append(compute_field)
from corgie.cli.compute_stats import compute_stats
COMMAND_LIST.append(compute_stats)
from corgie.cli.normalize import normalize
COMMAND_LIST.append(normalize)
from corgie.cli.align_block import align_block
COMMAND_LIST.append(align_block)
from corgie.cli.render import render
COMMAND_LIST.append(render)
from corgie.cli.copy import copy
COMMAND_LIST.append(copy)
from corgie.cli.apply_processor import apply_processor
COMMAND_LIST.append(apply_processor)

# To add new commands, create a file in this folder implementing a command,
# import the command here and add it to the list:


def get_command_list():
    return COMMAND_LIST
