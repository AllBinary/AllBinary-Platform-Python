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
# package org.allbinary.midlet

from __future__ import annotations

# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.midlet.MIDlet import MIDlet
from org.allbinary.logic.NullUtil import NullUtil


class AllBinaryMidlet(MIDlet, CommandListener):
    NULL_ALLBINARY_MIDLET: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.SET_DISPLAY: str = "setDisplay"
        self.SETTING_: str = "Setting: "
        self._DISPLAY_: str = " Display: "
        self.SETTING_NO_TITLE: str = "Setting: No Title, Display: "
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        self.midletDestroyed: bool = False
    

    @staticmethod
    def getNullInstance() -> AllBinaryMidlet:
        if AllBinaryMidlet.NULL_ALLBINARY_MIDLET == NullUtil.getInstance().NULL_OBJECT:
            AllBinaryMidlet.NULL_ALLBINARY_MIDLET = AllBinaryMidlet()
        return AllBinaryMidlet.NULL_ALLBINARY_MIDLET
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.logUtil.putF(self.commonStrings.CONSTRUCTOR, self, "AllBinaryMidlet::AllBinaryMidlet")
    

    def setDisplay(self, newDisplay: Displayable) -> None:
        title: str = StringUtil.getInstance().EMPTY_STRING
        if newDisplay != NullCanvas.NULL_CANVAS:
            title = newDisplay.getTitle()
            if title is not None:
                self.logUtil.putF(str(StringMaker().append(self.SETTING_).append(title).append(self._DISPLAY_).append(StringUtil.getInstance().toString(newDisplay))), self, self.SET_DISPLAY)
            else:
                self.logUtil.putF(str(StringMaker().append(self.SETTING_NO_TITLE).append(StringUtil.getInstance().toString(newDisplay))), self, self.SET_DISPLAY)
        display: Display = self.getDisplay()
        display.setCurrent(newDisplay)
    

    def getDisplay(self) -> Display:
        return Display.getDisplay(self)
    

    def getCurrentDisplayable(self) -> Displayable:
        return Display.getDisplay(self).getCurrent()
    

    def setDestroyed(self, destroyed: bool) -> None:
        self.midletDestroyed = destroyed
    

    def isDestroyed(self) -> bool:
        return self.midletDestroyed
    

    # throws MIDletStateChangeException
    def startApp(self) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def pauseApp(self) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def destroyAppInRunnable(self, unconditional: bool, isProgress: bool) -> None:
        pass
    

    def destroyApp(self, unconditional: bool) -> None:
        METHOD_NAME: str = "AllBinaryMidlet::destroyApp"
        try:
            self.logUtil.putF(self.commonStrings.START, self, METHOD_NAME)
            PreLogUtil.put(Memory.getInfo(), self, METHOD_NAME)
            self.setDestroyed(True)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, METHOD_NAME, e)
    

    # throws Exception
    def setStartStateHashtable(self, hashtable: ABHashtable[object, object]) -> None:
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append(StringUtil.getInstance().toString(hashtable))), self, "setStartStateHashtable")
        self.hashtable = hashtable
    

    # throws Exception
    def getStartStateHashtable(self) -> ABHashtable[object, object]:
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append(StringUtil.getInstance().toString(self.hashtable))), self, "getStartStateHashtable")
        return self.hashtable
    

    # throws Exception
    def getCurrentStateHashtable(self) -> ABHashtable[object, object]:
        self.logUtil.putF(self.commonStrings.START, self, "getStateHashtable")
        return StdUtil.getInstance().NULL_TABLE
    

    def commandAction(self, command: Command, displayable: Displayable) -> None:
        pass
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.Display import Display
# from javax.microedition.lcdui.Displayable import Displayable
# from javax.microedition.lcdui.NullCanvas import NullCanvas
# from javax.microedition.midlet.MIDletStateChangeException import MIDletStateChangeException
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.system.Memory import Memory
from org.allbinary.util.ABHashtable import ABHashtable


