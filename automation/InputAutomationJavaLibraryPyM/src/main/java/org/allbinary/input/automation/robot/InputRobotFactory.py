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
# package org.allbinary.input.automation.robot

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import lazy_static


class InputRobotFactory:
    inputRobotFactory: InputRobotFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        if "helpSetListenerInterface" not in vars(self): self.helpSetListenerInterface: HelpSetListener = None
    

    # throws Exception
    @staticmethod
    def getInstance() -> InputRobotFactory:
        return InputRobotFactory.inputRobotFactory
    

    def __init__(self) -> None:
        from org.allbinary.input.automation.robot.InputRobot import InputRobot
        __class__._init_fields(self)
        try:
            graphenv: GraphicsEnvironment = GraphicsEnvironment.getLocalGraphicsEnvironment()
            screens: list[GraphicsDevice] = graphenv.getScreenDevices()
            inputRobotInterface: InputRobotInterface = None
            for i in range(0, len(screens)):
                inputRobotInterface = InputRobot(screens[i])
                self.logUtil.putF("Adding Robot: " + inputRobotInterface.getName(), self, "getRobots")
                self.get().put(inputRobotInterface.getName(), inputRobotInterface)
            self.logUtil.putF("Number Of Robots: " + str(self.hashtable.size()), self, "getRobots")
        except Exception as e:
            self.logUtil.putF(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR)
    

    def addListener(self, helpSetListenerInterface: HelpSetListener) -> None:
        self.helpSetListenerInterface = helpSetListenerInterface
    

    # throws Exception
    def add(self, inputRobotInterface: InputRobotInterface) -> None:
        from org.allbinary.logic.java.help.JavaHelpSetNotifier import JavaHelpSetNotifier
        self.logUtil.putF("Adding InputRobotInterface: " + inputRobotInterface.getName(), self, "add")
        self.get().put(inputRobotInterface.getName(), inputRobotInterface)
        helpSet: HelpSet = inputRobotInterface.getHelpSet()
        if self.helpSetListenerInterface is not None:
            if helpSet is not None:
                if not (JavaHelpSetNotifier.isNotified(helpSet)):
                    helpSetEvent: HelpSetEvent = HelpSetEvent(self, helpSet, HelpSetEvent.HELPSET_ADDED)
                    self.helpSetListenerInterface.helpSetAdded(helpSetEvent)
            else:
                self.logUtil.putF("Null HelpSet For: " + inputRobotInterface.getName(), self, "add")
        else:
            self.logUtil.putF("No HelpSet Listener", self, "add")
    

    # throws Exception
    def loadLibraries_j0(self) -> None:
        from java.util.Set import Set
        set: Set = self.get().keySet()
        self.logUtil.putF("Loading Libraries", self, "loadLibraries")
        nameArray: list[object] = set.toArray()
        size: int = len(nameArray)
        for index in range(0, size):
            inputRobotInterface: InputRobotInterface = InputRobotFactory.getInstance().get(nameArray[index])
            InputRobotFactory.loadLibrary(inputRobotInterface)
    

    # throws Exception
    @staticmethod
    def loadLibraries_j1(collection: Collection) -> None:
        from java.util.Collection import Collection
        from java.util.Iterator import Iterator
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        logUtil: LogUtil = LogUtil.getInstance()
        logUtil.putF("Loading Libraries", "InputRobotFactory", "loadLibraries")
        iterator: Iterator = collection.iterator()
        while java_predicate(iterator, "hasNext"):
            InputRobotFactory.loadLibrary(iterator.next())

    def loadLibraries(self, *args):
        implementation = __class__.__dict__.get("loadLibraries_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().loadLibraries(*args)
    

    # throws Exception
    @staticmethod
    def loadLibrary(inputRobotInterface: InputRobotInterface) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.java.anyType.InterfaceUtil import InterfaceUtil
        from org.allbinary.logic.system.loader.SecuredNativeLibraryInterface import SecuredNativeLibraryInterface
        logUtil: LogUtil = LogUtil.getInstance()
        if InterfaceUtil.isImplemented(SecuredNativeLibraryInterface, inputRobotInterface):
            logUtil.putF("Loading Library: " + inputRobotInterface.getName(), "InputRobotFactory", "loadLibraries")
            securedNativeLibraryInterface: SecuredNativeLibraryInterface = inputRobotInterface
            securedNativeLibraryInterface.load()
    

    # throws Exception
    def unloadLibraries(self) -> None:
        from java.util.Set import Set
        from org.allbinary.logic.java.anyType.InterfaceUtil import InterfaceUtil
        from org.allbinary.logic.system.loader.SecuredNativeLibraryInterface import SecuredNativeLibraryInterface
        self.logUtil.putF("Unloading Libraries", self, "unloadLibraries")
        set: Set = self.get().keySet()
        inputRobotInterface: InputRobotInterface = None
        inputRobotArray: list[object] = set.toArray()
        size: int = len(inputRobotArray)
        for index in range(0, size):
            inputRobotInterface = self.get(inputRobotArray[index])
            if InterfaceUtil.isImplemented(SecuredNativeLibraryInterface, inputRobotInterface):
                self.logUtil.putF("Unloading Library: " + inputRobotInterface.getName(), self, "unloadLibraries")
                securedNativeLibraryInterface: SecuredNativeLibraryInterface = inputRobotInterface
                securedNativeLibraryInterface.unload()
    

    # throws Exception
    def get_j0(self) -> ABHashtable[object, object]:
        from org.allbinary.util.ABHashtable import ABHashtable
        return self.hashtable
    

    def get_j1(self, name: str) -> InputRobotInterface:
        self.logUtil.putF("Getting Robot: " + name, self, "getRobots")
        return self.hashtable.get(name)

    def get(self, *args):
        implementation = __class__.__dict__.get("get_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().get(*args)
# from java.awt.GraphicsDevice import GraphicsDevice
# from java.awt.GraphicsEnvironment import GraphicsEnvironment
# from java.util.Collection import Collection
# from java.util.Iterator import Iterator
# from java.util.Set import Set
# from javax.help.HelpSet import HelpSet
# from javax.help.event.HelpSetEvent import HelpSetEvent
# from javax.help.event.HelpSetListener import HelpSetListener
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.help.JavaHelpSetNotifier import JavaHelpSetNotifier
# from org.allbinary.logic.java.anyType.InterfaceUtil import InterfaceUtil
# from org.allbinary.logic.system.loader.SecuredNativeLibraryInterface import SecuredNativeLibraryInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.ABHashtable import ABHashtable


def _InputRobotFactory_inputRobotFactory() -> object:
    return InputRobotFactory()

lazy_static(InputRobotFactory, "inputRobotFactory", _InputRobotFactory_inputRobotFactory)

