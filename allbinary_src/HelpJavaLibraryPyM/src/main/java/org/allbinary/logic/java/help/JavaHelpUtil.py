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

from java.lang.JavaRuntimeStatic import lazy_static


class JavaHelpUtil:
    instance: JavaHelpUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.point: Point = Point(0, 0)
        self.dimension: Dimension = Dimension(640, 480)
        self.contextSensitiveHelpActionEvent: ActionEvent = ActionEvent(JLabel(), ActionEvent.ACTION_FIRST, None)
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    @staticmethod
    def getInstance() -> JavaHelpUtil:
        return JavaHelpUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getHelpSet_j1_1(self, filePath: str) -> HelpSet:
        from java.io.File import File
        from java.net.URL import URL
        try:
            helpSetURI: URI = File(filePath).toURI()
            helpSetURL: URL = helpSetURI.toURL()
            return self.getHelpSet(helpSetURL)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, JavaHelpUtil.getInstance(), "set", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getHelpSet_j1_2(self, url: URL) -> HelpSet:
        from java.net.URL import URL
        try:
            return HelpSet(None, url)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, JavaHelpUtil.getInstance(), "set", e)
            return None

    def getHelpSet(self, *args):
        if len(args) == 1 and True and (args[0] is None or isinstance(args[0], str)):
            return __class__.__dict__["getHelpSet_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["getHelpSet_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getHelpSet_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getHelpSet(*args)
    

    def show(self, helpSet: HelpSet) -> None:
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
# from java.awt.Point import Point
# from java.awt.Dimension import Dimension
# from java.awt.event.ActionEvent import ActionEvent
# from java.io.File import File
# from java.net.URI import URI
# from java.net.URL import URL
# from javax.help.CSH import CSH
# from javax.help.HelpBroker import HelpBroker
# from javax.help.HelpSet import HelpSet
# from javax.swing.JLabel import JLabel
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings


def _JavaHelpUtil_instance() -> object:
    return JavaHelpUtil()

lazy_static(JavaHelpUtil, "instance", _JavaHelpUtil_instance)

