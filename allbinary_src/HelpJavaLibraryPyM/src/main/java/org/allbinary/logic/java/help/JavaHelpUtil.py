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
# package org.allbinary.logic.java.help

from __future__ import annotations



class JavaHelpUtil:
    instance: JavaHelpUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.point: Point = Point(0, 0)
        self.dimension: Dimension = Dimension(640, 480)
        self.contextSensitiveHelpActionEvent: ActionEvent = ActionEvent(JLabel(), ActionEvent.ACTION_FIRST, None)
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    @staticmethod
    def getInstance() -> JavaHelpUtil:
        return JavaHelpUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getHelpSet(self, filePath: str) -> HelpSet:
        try:
            helpSetURI: URI = File(filePath).toURI()
            helpSetURL: URL = helpSetURI.toURL()
            return self.getHelpSet(helpSetURL)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, JavaHelpUtil.getInstance(), "set", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getHelpSet(self, url: URL) -> HelpSet:
        try:
            return HelpSet(None, url)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, JavaHelpUtil.getInstance(), "set", e)
            return None
    

    def show(self, helpSet: HelpSet) -> None:
        from org.allbinary.logic.java.help.DisplayHelpFromSource import DisplayHelpFromSource
        try:
            helpBroker: HelpBroker = helpSet.createHelpBroker()
            helpBroker.setLocation(self.point)
            helpBroker.setSize(self.dimension)
            DisplayHelpFromSource(helpBroker).actionPerformed(self.contextSensitiveHelpActionEvent)
            self.logUtil.putF("CSH Action", JavaHelpUtil.getInstance(), "show")
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, JavaHelpUtil.getInstance(), "show", e)
    

    @staticmethod
    def main(args: list[str]) -> None:
        try:
            javaHelpUtil: JavaHelpUtil = JavaHelpUtil.getInstance()
            javaHelpUtil.show(javaHelpUtil.getHelpSet("G:/mnt/bc/mydev/working/automation/InputAutomationJavaApplication/AllBinaryInputAutomationHelp/AllBinaryInputAutomation.hs"))
        except Exception as e:
            pass
# from java.awt import *
# from java.awt.event.ActionEvent import ActionEvent
# from java.io.File import File
# from java.net.URI import URI
# from java.net.URL import URL
# from javax.help.CSH import CSH
# from javax.help.HelpBroker import HelpBroker
# from javax.help.HelpSet import HelpSet
# from javax.swing import *
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.java.help.Point import Point
from org.allbinary.logic.java.help.Dimension import Dimension
from org.allbinary.logic.java.help.JLabel import JLabel


JavaHelpUtil.instance = JavaHelpUtil()

