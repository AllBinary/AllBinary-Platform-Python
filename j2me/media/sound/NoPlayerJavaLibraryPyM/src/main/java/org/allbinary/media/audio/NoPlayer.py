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
# package org.allbinary.media.audio

from __future__ import annotations

from org.allbinary.media.audio.BasicPlayer import BasicPlayer


class NoPlayer(BasicPlayer):
    NO_PLAYER: NoPlayer = None
    

    def __init__(self) -> None:
        super().__init__()
    

    def close(self) -> None:
        pass
    

    def getContentType(self) -> str:
        return StringUtil.getInstance().NULL_STRING
    

    def getControl(self, controlType: str) -> Control:
        from org.allbinary.media.audio.NullControl import NullControl
        return NullControl()
    

    def getControls(self) -> list[Control]:
        return [None] * (0)
# from javax.microedition.media.Control import Control
from org.allbinary.logic.string.StringUtil import StringUtil


NoPlayer.NO_PLAYER = NoPlayer()

