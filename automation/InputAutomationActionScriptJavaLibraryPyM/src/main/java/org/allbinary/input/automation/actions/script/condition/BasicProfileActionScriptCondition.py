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
# package org.allbinary.input.automation.actions.script.condition

from __future__ import annotations

from org.allbinary.input.automation.actions.script.ProfileActionScriptItem import ProfileActionScriptItem
from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface


class BasicProfileActionScriptCondition(ProfileActionScriptItem, ProfileActionScriptConditionInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.profileActionProcessorInterfaceVector: BasicArrayList = None
        self.profileActionConditionInterfaceVector: BasicArrayList = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor2(self, label: str, node: Node) -> None:
        from org.allbinary.input.automation.actions.script.condition.GenericProfileActionScriptConditionData import GenericProfileActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionFactory import ProfileActionScriptConditionFactory
        super().__init__(label, node)
        self._init_fields()
        self.init()
        nodeList: NodeList = node.getChildNodes()
        for index in range(0, nodeList.getLength()):
            actionItemNode: Node = nodeList.item(index)
            if actionItemNode.getNodeType() == Node.ELEMENT_NODE:
                if actionItemNode.getNodeName().compareTo(GenericProfileActionScriptConditionData.NAME) == 0:
                    self.addCondition(ProfileActionScriptConditionFactory.getInstance(actionItemNode))
                elif actionItemNode.getNodeName().compareTo(GenericProfileActionScriptInputData.NAME) == 0:
                    self.addProcessor(ProfileActionScriptInputFactory.getInstance(actionItemNode))
                elif actionItemNode.getNodeName().compareTo(GenericProfileActionScriptOutputData.NAME) == 0:
                    self.addProcessor(ProfileActionScriptOutputFactory.getInstance(actionItemNode))
    

    # throws Exception
    def addProcessorNodes(self, node: Node) -> None:
        nodeList: NodeList = node.getChildNodes()
        for index in range(0, nodeList.getLength()):
            processorActionItemNode: Node = nodeList.item(index)
            if processorActionItemNode.getNodeName().compareTo(GenericProfileActionScriptInputData.NAME) == 0:
                self.addProcessor(ProfileActionScriptInputFactory.getInstance(processorActionItemNode))
            elif processorActionItemNode.getNodeName().compareTo(GenericProfileActionScriptOutputData.NAME) == 0:
                self.addProcessor(ProfileActionScriptOutputFactory.getInstance(processorActionItemNode))
    

    def _constructor1(self, label: str) -> None:
        super().__init__(label)
        self._init_fields()
        self.init()
    

    def init(self) -> None:
        self.setProfileActionProcessorInterfaceVector(BasicArrayListD())
        self.setProfileActionConditionInterfaceVector(BasicArrayListD())
        self.getJPopupMenu().add(self.getConditionJPopupMenu())
        self.getJPopupMenu().add(self.getInputJPopupMenu())
        self.getJPopupMenu().add(self.getOutputJPopupMenu())
    

    def getConditionJPopupMenu(self) -> JMenu:
        from org.allbinary.input.automation.actions.script.condition.JMenu import JMenu
        from org.allbinary.input.automation.actions.script.condition.JMenuItem import JMenuItem
        from org.allbinary.input.automation.actions.script.condition.JMenuItem import JMenuItem
        from org.allbinary.input.automation.actions.script.condition.JMenuItem import JMenuItem
        jMenu: JMenu = JMenu(self.NEW_CONDITION)
        jMenuItemColorAt: JMenuItem = JMenuItem(self.NEW_COLOR_AT)
        jMenuItemAlways: JMenuItem = JMenuItem(self.NEW_ALWAYS)
        jMenuItemTimeInterval: JMenuItem = JMenuItem(self.NEW_TIME_INTERVAL)
        jMenuItemColorAt.addActionListener(self)
        jMenuItemAlways.addActionListener(self)
        jMenuItemTimeInterval.addActionListener(self)
        jMenu.add(jMenuItemColorAt)
        jMenu.add(jMenuItemAlways)
        jMenu.add(jMenuItemTimeInterval)
        return jMenu
    

    def getInputJPopupMenu(self) -> JMenu:
        from org.allbinary.input.automation.actions.script.condition.JMenu import JMenu
        from org.allbinary.input.automation.actions.script.condition.JMenuItem import JMenuItem
        from org.allbinary.input.automation.actions.script.condition.JMenuItem import JMenuItem
        from org.allbinary.input.automation.actions.script.condition.JMenuItem import JMenuItem
        jMenu: JMenu = JMenu(self.NEW_INPUT)
        jMenuItemKey: JMenuItem = JMenuItem(self.NEW_KEY_INPUT)
        jMenuItemMouse: JMenuItem = JMenuItem(self.NEW_MOUSE_INPUT)
        jMenuItemJoystick: JMenuItem = JMenuItem(self.NEW_JOYSTICK_INPUT)
        jMenuItemKey.addActionListener(self)
        jMenuItemMouse.addActionListener(self)
        jMenuItemJoystick.addActionListener(self)
        jMenu.add(jMenuItemKey)
        jMenu.add(jMenuItemMouse)
        jMenu.add(jMenuItemJoystick)
        return jMenu
    

    def getOutputJPopupMenu(self) -> JMenu:
        from org.allbinary.input.automation.actions.script.condition.JMenu import JMenu
        from org.allbinary.input.automation.actions.script.condition.JMenuItem import JMenuItem
        jMenu: JMenu = JMenu(self.NEW_OUTPUT)
        jMenuItemImage: JMenuItem = JMenuItem(self.NEW_IMAGE_OUTPUT)
        jMenuItemImage.addActionListener(self)
        jMenu.add(jMenuItemImage)
        return jMenu
    

    def addProcessor(self, profileActionProcessorInterface: ProfileActionScriptProcessorInterface) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "addInput")
        self.getProfileActionProcessorInterfaceVector().add(profileActionProcessorInterface)
        self.add(profileActionProcessorInterface)
    

    def removeProcessor(self, profileActionProcessorInterface: ProfileActionScriptProcessorInterface) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "removeInput")
        self.getProfileActionProcessorInterfaceVector().remove(profileActionProcessorInterface)
        self.remove(profileActionProcessorInterface)
    

    def removeCondition(self, profileActionScriptNodeInterface: ProfileActionScriptNodeInterface) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "removeCondition")
        self.getProfileActionConditionInterfaceVector().remove(profileActionScriptNodeInterface)
        self.remove(profileActionScriptNodeInterface)
    

    def addCondition(self, profileActionScriptNodeInterface: ProfileActionScriptNodeInterface) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "addCondition")
        self.getProfileActionConditionInterfaceVector().add(profileActionScriptNodeInterface)
        self.add(profileActionScriptNodeInterface)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.actions.script.condition.GenericProfileActionScriptConditionData import GenericProfileActionScriptConditionData
        node: Node = document.createElement(GenericProfileActionScriptConditionData.NAME)
        profileActionConditionInterfaceVector: BasicArrayList = self.getProfileActionConditionInterfaceVector()
        size: int = profileActionConditionInterfaceVector.size()
        for index in range(0, size):
            profileActionConditionInterface: ProfileActionScriptConditionInterface = profileActionConditionInterfaceVector.get(index)
            node.appendChild(profileActionConditionInterface.toXmlNode(document))
        profileActionProcessorInterfaceVector: BasicArrayList = self.getProfileActionProcessorInterfaceVector()
        size2: int = profileActionProcessorInterfaceVector.size()
        for index in range(0, size2):
            profileActionProcessorInterface: ProfileActionScriptProcessorInterface = profileActionProcessorInterfaceVector.get(index)
            node.appendChild(profileActionProcessorInterface.toXmlNode(document))
        return node
    

    def getProfileActionConditionInterfaceVector(self) -> BasicArrayList:
        return self.profileActionConditionInterfaceVector
    

    def setProfileActionConditionInterfaceVector(self, profileActionConditionInterfaceVector: BasicArrayList) -> None:
        self.profileActionConditionInterfaceVector = profileActionConditionInterfaceVector
    

    def actionPerformed(self, actionEvent: ActionEvent) -> None:
        from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptCondition import TimeIntervalActionScriptCondition
        from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptCondition import AlwaysActionScriptCondition
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptCondition import ColorAtActionScriptCondition
        try:
            super().actionPerformed(actionEvent)
            if actionEvent.getActionCommand().compareTo(self.DELETE) == 0:
                if isinstance(self.getParent(), ProfileActionScriptNodeInterface):
                    profileActionScriptNodeInterface: ProfileActionScriptNodeInterface = self.getParent()
                    profileActionScriptNodeInterface.removeCondition(self)
                    JTreeInterfaceFactory.getInstance().getJTreeInterface().updateJTree()
            elif actionEvent.getActionCommand().compareTo(self.NEW_COLOR_AT) == 0:
                self.addCondition(ColorAtActionScriptCondition())
                self.updateTree()
            elif actionEvent.getActionCommand().compareTo(self.NEW_ALWAYS) == 0:
                self.addCondition(AlwaysActionScriptCondition())
                self.updateTree()
            elif actionEvent.getActionCommand().compareTo(self.NEW_TIME_INTERVAL) == 0:
                self.addCondition(TimeIntervalActionScriptCondition())
                self.updateTree()
            elif actionEvent.getActionCommand().compareTo(self.NEW_KEY_INPUT) == 0:
                self.addProcessor(KeyboardActionScriptInput())
                self.updateTree()
            elif actionEvent.getActionCommand().compareTo(self.NEW_MOUSE_INPUT) == 0:
                self.addProcessor(MouseActionScriptInput())
                self.updateTree()
            elif actionEvent.getActionCommand().compareTo(self.NEW_IMAGE_OUTPUT) == 0:
                self.addProcessor(ImageActionScriptOutput())
                self.updateTree()
        except Exception as e:
            self.logUtil.put("Error", self, "actionPerformed", e)
    

    def getProfileActionProcessorInterfaceVector(self) -> BasicArrayList:
        return self.profileActionProcessorInterfaceVector
    

    def setProfileActionProcessorInterfaceVector(self, profileActionProcessorInterfaceVector: BasicArrayList) -> None:
        self.profileActionProcessorInterfaceVector = profileActionProcessorInterfaceVector
    

    def updateTree(self) -> None:
        JTreeInterfaceFactory.getInstance().getJTreeInterface().updateJTree()
        treePath: TreePath = TreePath(self)
        JTreeInterfaceFactory.getInstance().getJTreeInterface().getActionScriptJTree().expandPath(treePath)
    

    # throws Exception
    def shouldProcess(self, frame: int) -> bool:
        profileActionConditionInterfaceVector: BasicArrayList = self.getProfileActionConditionInterfaceVector()
        size: int = profileActionConditionInterfaceVector.size()
        for index in range(0, size):
            profileActionScriptConditionInterface: ProfileActionScriptConditionInterface = profileActionConditionInterfaceVector.get(index)
            if not profileActionScriptConditionInterface.shouldProcess(frame):
                return False
        return True
    

    # throws Exception
    def process(self, frame: int) -> None:
        self.logUtil.putF(str(StringMaker().append("Start - Processing ").appendint(self.getProfileActionProcessorInterfaceVector().size()).append(" inputs")), self, self.commonStrings.PROCESS)
        profileActionProcessorInterfaceVector: BasicArrayList = self.getProfileActionProcessorInterfaceVector()
        size: int = profileActionProcessorInterfaceVector.size()
        for index in range(0, size):
            profileActionScriptProcessorInterface: ProfileActionScriptProcessorInterface = profileActionProcessorInterfaceVector.get(index)
            profileActionScriptProcessorInterface.process(frame)
# from java.awt.event.ActionEvent import ActionEvent
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.swing import *
# from javax.swing.tree.TreePath import TreePath
from org.allbinary.input.automation.actions.script.JTreeInterfaceFactory import JTreeInterfaceFactory
from org.allbinary.input.automation.actions.script.ProfileActionScriptNodeInterface import ProfileActionScriptNodeInterface
from org.allbinary.input.automation.actions.script.condition.processors.ProfileActionScriptProcessorInterface import ProfileActionScriptProcessorInterface
from org.allbinary.input.automation.actions.script.condition.processors.input.GenericProfileActionScriptInputData import GenericProfileActionScriptInputData
from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInput import KeyboardActionScriptInput
from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInput import MouseActionScriptInput
from org.allbinary.input.automation.actions.script.condition.processors.input.ProfileActionScriptInputFactory import ProfileActionScriptInputFactory
from org.allbinary.input.automation.module.actions.script.condition.processors.output.GenericProfileActionScriptOutputData import GenericProfileActionScriptOutputData
from org.allbinary.input.automation.module.actions.script.condition.processors.output.ImageActionScriptOutput import ImageActionScriptOutput
from org.allbinary.input.automation.module.actions.script.condition.processors.output.ProfileActionScriptOutputFactory import ProfileActionScriptOutputFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


