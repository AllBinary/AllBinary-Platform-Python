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
# package org.allbinary.input.automation.module.generic.configuration.profile.actions.script

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
# from javax.swing.tree.DefaultMutableTreeNode import DefaultMutableTreeNode
from org.allbinary.input.automation.actions.script.ProfileActionScriptNodeInterface import ProfileActionScriptNodeInterface


class GenericProfileActionScript(*java_bases(DefaultMutableTreeNode, ProfileActionScriptNodeInterface)):
    NAME: str = "Root"

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionJPanel import GenericProfileActionJPanel
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.genericProfileActionJPanel: GenericProfileActionJPanel = None
        self.profileActionConditionInterfaceVector: BasicArrayList = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor2(self, genericProfileActionJPanel: GenericProfileActionJPanel, node: Node) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionFactory import ProfileActionScriptConditionFactory
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionData import GenericProfileActionData
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionJPanel import GenericProfileActionJPanel
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        super().__init__(GenericProfileActionScript.NAME)
        self._init_fields()
        self.genericProfileActionJPanel = genericProfileActionJPanel
        self.setProfileActionConditionInterfaceVector(BasicArrayListD())
        actionScriptNode: Node = DomSearchHelper.getNode(GenericProfileActionData.SCRIPT, node.getChildNodes())
        if actionScriptNode is not None:
            nodeList: NodeList = actionScriptNode.getChildNodes()
            for index in range(0, nodeList.getLength()):
                actionConditionNode: Node = nodeList.item(index)
                if actionConditionNode.getNodeType() == Node.ELEMENT_NODE:
                    self.addCondition(ProfileActionScriptConditionFactory.getInstance(actionConditionNode))
        else:
            raise Exception("Profile Action Script Node Null")
    

    def _constructor1(self, genericProfileActionJPanel: GenericProfileActionJPanel) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionJPanel import GenericProfileActionJPanel
        super().__init__()
        self._init_fields()
        self.genericProfileActionJPanel = genericProfileActionJPanel
        self.setProfileActionConditionInterfaceVector(BasicArrayListD())
    

    def addCondition(self, profileActionScriptNodeInterface: ProfileActionScriptNodeInterface) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "addCondition")
        self.getProfileActionConditionInterfaceVector().add(profileActionScriptNodeInterface)
        self.add(profileActionScriptNodeInterface)
    

    def removeCondition(self, profileActionScriptNodeInterface: ProfileActionScriptNodeInterface) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "removeCondition")
        self.getProfileActionConditionInterfaceVector().remove(profileActionScriptNodeInterface)
        self.remove(profileActionScriptNodeInterface)
    

    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        self.logUtil.putF("HashMap: " + str(hashMap), self, "toHashMap()")
        return hashMap
    

    def getProfileActionConditionInterfaceVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.profileActionConditionInterfaceVector
    

    def setProfileActionConditionInterfaceVector(self, profileActionConditionInterfaceVector: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        self.profileActionConditionInterfaceVector = profileActionConditionInterfaceVector
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
        from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionData import GenericProfileActionData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(GenericProfileActionData.SCRIPT)
        vector: BasicArrayList = self.getProfileActionConditionInterfaceVector()
        size: int = vector.size()
        for index in range(0, size):
            profileActionConditionInterface: ProfileActionScriptConditionInterface = vector.get(index)
            node.appendChild(profileActionConditionInterface.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionFactory import ProfileActionScriptConditionFactory
# from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
# from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionData import GenericProfileActionData
# from org.allbinary.input.automation.module.generic.configuration.profile.actions.GenericProfileActionJPanel import GenericProfileActionJPanel
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


