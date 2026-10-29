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



class InputRobotFactory:
    inputRobotFactory: InputRobotFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        self.helpSetListenerInterface: HelpSetListener = None
    

    # throws Exception
    @staticmethod
    def getInstance() -> InputRobotFactory:
        return InputRobotFactory.inputRobotFactory
    

    def __init__(self) -> None:
        from org.allbinary.input.automation.robot.InputRobot import InputRobot
        self._init_fields()
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
        self.logUtil.putF("Adding InputRobotInterface: " + inputRobotInterface.getName(), self, "add")
        self.get().put(inputRobotInterface.getName(), inputRobotInterface)
        helpSet: HelpSet = inputRobotInterface.getHelpSet()
        if self.helpSetListenerInterface is not None:
            if helpSet is not None:
                if not JavaHelpSetNotifier.isNotified(helpSet):
                    helpSetEvent: HelpSetEvent = HelpSetEvent(self, helpSet, HelpSetEvent.HELPSET_ADDED)
                    self.helpSetListenerInterface.helpSetAdded(helpSetEvent)
            else:
                self.logUtil.putF("Null HelpSet For: " + inputRobotInterface.getName(), self, "add")
        else:
            self.logUtil.putF("No HelpSet Listener", self, "add")
    

    # throws Exception
    def loadLibraries(self) -> None:
        set: Set = self.get().keySet()
        self.logUtil.putF("Loading Libraries", self, "loadLibraries")
        nameArray: list[object] = set.toArray()
        size: int = len(nameArray)
        for index in range(0, size):
            inputRobotInterface: InputRobotInterface = InputRobotFactory.getInstance().get(nameArray[index])
            InputRobotFactory.loadLibrary(inputRobotInterface)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def loadLibraries(collection: Collection) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        logUtil.putF("Loading Libraries", "InputRobotFactory", "loadLibraries")
        iterator: Iterator = collection.iterator()
        while iterator.hasNext():
            InputRobotFactory.loadLibrary(iterator.next())
    

    # throws Exception
    @staticmethod
    def loadLibrary(inputRobotInterface: InputRobotInterface) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        if InterfaceUtil.isImplemented(SecuredNativeLibraryInterface, inputRobotInterface):
            logUtil.putF("Loading Library: " + inputRobotInterface.getName(), "InputRobotFactory", "loadLibraries")
            securedNativeLibraryInterface: SecuredNativeLibraryInterface = inputRobotInterface
            securedNativeLibraryInterface.load()
    

    # throws Exception
    def unloadLibraries(self) -> None:
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
    def get(self) -> ABHashtable[object, object]:
        return self.hashtable
    

    # Java overloaded method: Python keeps the last definition
    def get(self, name: str) -> InputRobotInterface:
        self.logUtil.putF("Getting Robot: " + name, self, "getRobots")
        return self.hashtable.get(name)
# from java.awt.GraphicsDevice import GraphicsDevice
# from java.awt.GraphicsEnvironment import GraphicsEnvironment
# from java.util.Collection import Collection
# from java.util.Iterator import Iterator
# from java.util.Set import Set
# from javax.help.HelpSet import HelpSet
# from javax.help.event.HelpSetEvent import HelpSetEvent
# from javax.help.event.HelpSetListener import HelpSetListener
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.help.JavaHelpSetNotifier import JavaHelpSetNotifier
from org.allbinary.logic.java.anyType.InterfaceUtil import InterfaceUtil
from org.allbinary.logic.system.loader.SecuredNativeLibraryInterface import SecuredNativeLibraryInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable


InputRobotFactory.inputRobotFactory = InputRobotFactory()

