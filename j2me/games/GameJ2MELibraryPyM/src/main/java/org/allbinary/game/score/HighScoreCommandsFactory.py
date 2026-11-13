#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.game.score

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.game.score.HighScoreCommandsBaseFactory import HighScoreCommandsBaseFactory


class HighScoreCommandsFactory(HighScoreCommandsBaseFactory):
    instance: HighScoreCommandsFactory = None
    

    @staticmethod
    def getInstance() -> HighScoreCommandsFactory:
        return HighScoreCommandsFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.game.score.HighScoreCommands import HighScoreCommands
        from org.allbinary.game.score.HighScoreCommands import HighScoreCommands
        from javax.microedition.lcdui.Command import Command
        super().__init__([HighScoreCommands.getInstance().PERSONAL, HighScoreCommands.getInstance().WORLD])
# from javax.microedition.lcdui.Command import Command


def _HighScoreCommandsFactory_instance() -> object:
    return HighScoreCommandsFactory()

lazy_static(HighScoreCommandsFactory, "instance", _HighScoreCommandsFactory_instance)

