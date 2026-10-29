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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.init.Init import Init


class KeyFactoryInitializer(Init):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def init(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.INIT)
from org.allbinary.logic.communication.log.LogUtil import LogUtil


