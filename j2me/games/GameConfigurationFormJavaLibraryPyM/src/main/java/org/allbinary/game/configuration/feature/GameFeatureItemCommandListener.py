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
# package org.allbinary.game.configuration.feature

from __future__ import annotations

# from javax.microedition.lcdui.ItemCommandListener import ItemCommandListener


class GameFeatureItemCommandListener(ItemCommandListener):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.gameOptionsForm: GameOptionsForm = None
    

    def __init__(self, gameOptionsForm: GameOptionsForm) -> None:
        self._init_fields()
        self.gameOptionsForm = gameOptionsForm
    

    def commandAction(self, command: Command, item: Item) -> None:
        try:
            itemLabel: str = item.getLabel()
            self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().ITEM_LABEL).append(itemLabel)), self, MidletStrings.getInstance().COMMAND_ACTION)
            if isinstance(item, GameConfigurationGauge):
                GameConfigurationUtil.getInstance().change(self.gameOptionsForm, item)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, MidletStrings.getInstance().COMMAND_ACTION, e)
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.Item import Item
from org.allbinary.game.configuration.GameConfigurationGauge import GameConfigurationGauge
from org.allbinary.game.configuration.GameConfigurationUtil import GameConfigurationUtil
from org.allbinary.game.configuration.GameOptionsForm import GameOptionsForm
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.midlet.MidletStrings import MidletStrings
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings


