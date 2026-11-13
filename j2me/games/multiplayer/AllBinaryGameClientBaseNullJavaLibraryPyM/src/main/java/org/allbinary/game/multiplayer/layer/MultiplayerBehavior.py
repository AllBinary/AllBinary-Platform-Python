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
# package org.allbinary.game.multiplayer.layer

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class MultiplayerBehavior:
    NULL_MULTIPLAYER_BEHAVIOR: MultiplayerBehavior = None
    

    def __init__(self, username: str) -> None:
        pass
    

    def startTick(self) -> None:
        pass
    

    def endTick(self) -> None:
        pass
    

    def getApproximateElapsed(self) -> int:
        return 0
# from org.allbinary.logic.string.StringUtil import StringUtil


def _MultiplayerBehavior_NULL_MULTIPLAYER_BEHAVIOR() -> object:
    from org.allbinary.logic.string.StringUtil import StringUtil
    return MultiplayerBehavior(StringUtil.getInstance().EMPTY_STRING)

lazy_static(MultiplayerBehavior, "NULL_MULTIPLAYER_BEHAVIOR", _MultiplayerBehavior_NULL_MULTIPLAYER_BEHAVIOR)

