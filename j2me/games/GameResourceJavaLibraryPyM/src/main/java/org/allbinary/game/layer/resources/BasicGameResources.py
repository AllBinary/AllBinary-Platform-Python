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
# package org.allbinary.game.layer.resources

from __future__ import annotations

from org.allbinary.logic.string.StringMaker import StringMaker


class BasicGameResources:
    stringBuffer: StringMaker = StringMaker()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.RESOURCE: str = StringUtil.getInstance().EMPTY_STRING
        self.RESOURCE_DESTROY: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self, ROOT: str, SIZE: list[str]) -> None:
        from org.allbinary.game.layer.resources.SIZE import SIZE
        try:
            scale: int = int(GameConfigurationCentral.getInstance().SCALE.getValue())
            if scale > 1 and scale - 1 < len(SIZE):
                self.append(ROOT, SIZE[scale - 1])
            else:
                raise Exception(str(StringMaker().append("Invalid Value: ").appendint(scale)))
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.INIT, e)
    

    # throws Exception
    def append(self, ROOT: str, sizeString: str) -> None:
        DESTROY: str = "_destroy"
        string: str = self.getString()
        BasicGameResources.stringBuffer.delete(0, BasicGameResources.stringBuffer.length())
        BasicGameResources.stringBuffer.append(ROOT)
        BasicGameResources.stringBuffer.append(string)
        BasicGameResources.stringBuffer.append(sizeString)
        self.RESOURCE = str(BasicGameResources.stringBuffer)
        BasicGameResources.stringBuffer.delete(0, BasicGameResources.stringBuffer.length())
        BasicGameResources.stringBuffer.append(ROOT)
        BasicGameResources.stringBuffer.append(DESTROY)
        BasicGameResources.stringBuffer.append(string)
        BasicGameResources.stringBuffer.append(sizeString)
        self.RESOURCE_DESTROY = str(BasicGameResources.stringBuffer)
    

    # throws Exception
    def getString(self) -> str:
        from org.allbinary.game.layer.resources.GameGraphicsResourceUtil import GameGraphicsResourceUtil
        return GameGraphicsResourceUtil.getInstance().getName()
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


