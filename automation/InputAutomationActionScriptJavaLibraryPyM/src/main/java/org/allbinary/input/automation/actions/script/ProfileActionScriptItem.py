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
# package org.allbinary.input.automation.actions.script

from __future__ import annotations

# from java.awt.event.ActionListener import ActionListener
# from javax.swing.tree.DefaultMutableTreeNode import DefaultMutableTreeNode
from org.allbinary.input.automation.actions.script.ProfileActionScriptItemInterface import ProfileActionScriptItemInterface


class ProfileActionScriptItem(DefaultMutableTreeNode, ProfileActionScriptItemInterface, ActionListener):
    EDIT: str = "Edit"
    DELETE: str = "Delete"
    NEW_CONDITION: str = "New Condition"
    NEW_INPUT: str = "New Input"
    NEW_OUTPUT: str = "New Output"
    NEW_COLOR_AT: str = "Color At"
    NEW_TIME_INTERVAL: str = "Time Interval"
    NEW_ALWAYS: str = "Always On/Off"
    NEW_KEY_INPUT: str = "Key"
    NEW_MOUSE_INPUT: str = "Mouse"
    NEW_JOYSTICK_INPUT: str = "Joystick"
    NEW_IMAGE_OUTPUT: str = "Image"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.jPopupMenu: JPopupMenu = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor2(self, label: str, node: Node) -> None:
        super().__init__(label)
        self._init_fields()
        self.init()
        self.logUtil.putF("Label: " + label, self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor1(self, label: str) -> None:
        super().__init__(label)
        self._init_fields()
        self.init()
        self.logUtil.putF("Label: " + label, self, self.commonStrings.CONSTRUCTOR)
    

    def init(self) -> None:
        from org.allbinary.input.automation.actions.script.JPopupMenu import JPopupMenu
        from org.allbinary.input.automation.actions.script.JMenuItem import JMenuItem
        from org.allbinary.input.automation.actions.script.JMenuItem import JMenuItem
        self.setJPopupMenu(JPopupMenu())
        jMenuItemEdit: JMenuItem = JMenuItem(ProfileActionScriptItem.EDIT)
        jMenuItemDelete: JMenuItem = JMenuItem(ProfileActionScriptItem.DELETE)
        jMenuItemEdit.addActionListener(self)
        jMenuItemDelete.addActionListener(self)
        self.getJPopupMenu().add(jMenuItemEdit)
        self.getJPopupMenu().add(jMenuItemDelete)
    

    # throws Exception
    def process(self, frame: int) -> None:
        raise RuntimeError()
    

    def getJPopupMenu(self) -> JPopupMenu:
        return self.jPopupMenu
    

    def showDialog(self) -> None:
        raise RuntimeError()
    

    def actionPerformed(self, actionEvent: ActionEvent) -> None:
        if actionEvent.getActionCommand().compareTo(ProfileActionScriptItem.EDIT) == 0:
            self.showDialog()
    

    def setJPopupMenu(self, jPopupMenu: JPopupMenu) -> None:
        self.jPopupMenu = jPopupMenu
# from java.awt.event.ActionEvent import ActionEvent
# from javax.swing import *
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Node import Node


