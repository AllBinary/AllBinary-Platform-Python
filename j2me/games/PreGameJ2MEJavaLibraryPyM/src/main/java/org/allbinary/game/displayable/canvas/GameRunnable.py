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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

import time
import threading


class GameRunnable(object):

    def _init_fields(self) -> None:
        self.WAIT: int = 240
        self.FAST: int = 60
        self.waitInMillis: int = self.WAIT
    

    def __init__(self) -> None:
        self._init_fields()
    

    def run(self) -> None:
        DisplayInfoSingleton.getInstance().process()
    

    # throws Exception
    def processLoopSleep(self) -> None:
        time.sleep((self.waitInMillis) / 1000)
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton


