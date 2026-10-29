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
# package org.allbinary.game.layer.identification

from __future__ import annotations

from org.allbinary.layer.event.LayerManagerEventListener import LayerManagerEventListener


class GroupLayerManagerListener(LayerManagerEventListener):
    SINGLETON: GroupLayerManagerListener = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.list_: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> GroupLayerManagerListener:
        return GroupLayerManagerListener.SINGLETON
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        LayerManagerEventHandler.getInstance().addListener(self)
    

    def clear(self) -> None:
        groupList: BasicArrayList = None
        size: int = self.list_.size()
        for index in range(size - 1, 0 - 1, -1):
            groupList = self.list_.objectArray[index]
            groupList.clear()
    

    def getGroupSizeFromInterface(self, groupInterfaceCompositeInterface: GroupInterfaceCompositeInterface) -> int:
        groupInterfaceArray: list[Group] = groupInterfaceCompositeInterface.getGroupInterface()
        return self.getGroupSize(groupInterfaceArray[0])
    

    def getGroupSize(self, groupInterface: Group) -> int:
        id: int = int(groupInterface.getGroupId())
        return self.getGroupSizeById(id)
    

    def getList(self, groupInterface: Group) -> BasicArrayList:
        id: int = int(groupInterface.getGroupId())
        return self.getListById(id)
    

    def getListById(self, groupId: int) -> BasicArrayList:
        groupList: BasicArrayList = self.list_.objectArray[groupId]
        return groupList
    

    def getGroupSizeById(self, groupId: int) -> int:
        groupList: BasicArrayList = self.list_.objectArray[groupId]
        size: int = groupList.size()
        return size
    

    def areAllOtherGroupsEmpty(self, groupInterface: Group) -> bool:
        id: int = int(groupInterface.getGroupId())
        size: int = self.list_.size()
        for index in range(size - 1, 0 - 1, -1):
            if id != index:
                groupSize: int = self.getGroupSizeById(index)
                if groupSize != 0:
                    self.logUtil.putF(str(StringMaker().append("Group Size: ").appendint(groupSize)), self, "areAllOtherGroupsEmpty")
                    return False
        return True
    

    def isIdInList(self, id: int, excludeGroupList: BasicArrayList) -> bool:
        size: int = excludeGroupList.size()
        groupInterfaceArray: list[Group] = None
        groupInterface: Group = None
        groupId: int = 0
        for index in range(size - 1, 0 - 1, -1):
            groupInterfaceArray = excludeGroupList.objectArray[index]
            size2: int = len(groupInterfaceArray)
            for index2 in range(0, size2):
                groupInterface = groupInterfaceArray[index2]
                groupId = int(groupInterface.getGroupId())
                if groupId == id:
                    return True
        return False
    

    def areAllOtherGroupsLessThan(self, excludeGroupList: BasicArrayList, maxSize: int) -> bool:
        size: int = self.list_.size()
        for index in range(size - 1, 0 - 1, -1):
            if not self.isIdInList(index, excludeGroupList):
                groupSize: int = self.getGroupSizeById(index)
                if groupSize >= maxSize:
                    return False
        return True
    

    def init(self, total: int) -> None:
        while self.list_.size() <= total + 1:
            self.list_.add(BasicArrayListD())
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    # throws Exception
    def onCreateLayerManagerEvent(self, layerManagerEvent: LayerManagerEvent) -> None:
        layerInterface: AllBinaryLayer = layerManagerEvent.getLayerInterface()
        groupInterfaceArray: list[Group] = layerInterface.getGroupInterface()
        size: int = len(groupInterfaceArray)
        id: int = 0
        groupList: BasicArrayList = None
        for index in range(0, size):
            id = int(groupInterfaceArray[index].getGroupId())
            groupList = self.list_.objectArray[id]
            if groupList is None:
                self.logUtil.putF(str(StringMaker().append("id: ").appendint(id)), self, "onCreateLayerManagerEvent")
            if not groupList.contains(layerInterface):
                groupList.add(layerInterface)
            else:
                pass
    

    # throws Exception
    def onDeleteLayerManagerEvent(self, layerManagerEvent: LayerManagerEvent) -> None:
        layerInterface: AllBinaryLayer = layerManagerEvent.getLayerInterface()
        groupInterfaceArray: list[Group] = layerInterface.getGroupInterface()
        size: int = len(groupInterfaceArray)
        id: int = 0
        groupList: BasicArrayList = None
        for index in range(0, size):
            id = int(groupInterfaceArray[index].getGroupId())
            groupList = self.list_.objectArray[id]
            groupList.remove(layerInterface)
    

    def log(self) -> None:
        stringBuffer: StringMaker = StringMaker()
        GROUP: str = "Group: "
        SPACE: str = CommonSeps.getInstance().SPACE
        TOTAL_LABEL: str = CommonLabels.getInstance().TOTAL_LABEL
        size: int = self.list_.size()
        for index in range(size - 1, 0 - 1, -1):
            groupList: BasicArrayList = self.list_.objectArray[index]
            stringBuffer.append(GROUP)
            stringBuffer.appendint(index)
            stringBuffer.append(SPACE)
            stringBuffer.append(TOTAL_LABEL)
            stringBuffer.appendint(groupList.size())
            stringBuffer.append(SPACE)
        self.logUtil.putF(str(stringBuffer), self, "log")
from org.allbinary.game.identification.Group import Group
from org.allbinary.game.identification.GroupInterfaceCompositeInterface import GroupInterfaceCompositeInterface
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.event.LayerManagerEvent import LayerManagerEvent
from org.allbinary.layer.event.LayerManagerEventHandler import LayerManagerEventHandler
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


GroupLayerManagerListener.SINGLETON = GroupLayerManagerListener()

