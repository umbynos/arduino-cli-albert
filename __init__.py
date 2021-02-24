# -*- coding: utf-8 -*-

"""This is a wrapper for arduino-cli.

Arduino CLI is an all-in-one solution that provides builder, Boards/Library Manager, uploader, \
discovery and many other tools needed to use any Arduino compatible board and platforms.

Synopsis: <ino> [board] """

from albert import *
import os
import json
import subprocess
from time import sleep # TODO trash


__title__ = "Arduino CLI"
__version__ = "0.4.0"
__triggers__ = "ino "
__authors__ = "Umberto Baldi"
# __exec_deps__ = ["arduino-cli"] #TODO arduino-cli not found in PATH

iconPath = os.path.dirname(__file__) + "/arduino-cli-logo.bmp" # TODO cli logo svg


# Can be omitted
def initialize():
    pass


# Can be omitted
def finalize():
    pass

# Returns a list of connected boards (with metadata)
def getBoardList():
    proc = subprocess.run(["arduino-cli", "board", "list", "--format", "json"], stdout=subprocess.PIPE)

    items = []
    for board in json.loads(proc.stdout.decode()):
        if board.get("boards"):
            items.append(
                Item(
                    id = __title__,
                    icon = iconPath,
                    text = "%s (%s)" % (board["boards"][0]["name"], board["address"]),
                    subtext = "VID: %s PID: %s" % (board["boards"][0]["VID"], board["boards"][0]["PID"])
                    # actions = 
                )
            )
    return items

def handleQuery(query):
    if query.isTriggered:
        if query.string.startswith("board"):
            # if query.string.startswith("list"):
            boards = getBoardList()
            if not boards:
                return Item(
                    id = __title__,
                    icon = iconPath,
                    text = "No attached boards detected"
                )

            return boards
