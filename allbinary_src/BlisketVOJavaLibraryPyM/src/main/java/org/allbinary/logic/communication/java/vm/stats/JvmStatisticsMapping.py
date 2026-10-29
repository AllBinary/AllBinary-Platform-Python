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
# package org.allbinary.logic.communication.java.vm.stats

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
from org.allbinary.logic.communication.java.vm.stats.JvmStatistics import JvmStatistics


class JvmStatisticsMapping(JvmStatistics, TableMappingInterface):
    

    def __init__(self) -> None:
        super().__init__()
    

    def toHashMap(self) -> dict:
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(JvmStatisticsData.FREE_MEMORY_BYTES, self.getFreeMemoryBytesString())
        hashMap.put(JvmStatisticsData.FREE_MEMORY_KILOBYTES, self.getFreeMemoryKilobytesString())
        hashMap.put(JvmStatisticsData.FREE_MEMORY_MEGABYTES, self.getFreeMemoryMegabytesString())
        hashMap.put(JvmStatisticsData.MAX_MEMORY_BYTES, self.getMaxMemoryBytesString())
        hashMap.put(JvmStatisticsData.MAX_MEMORY_KILOBYTES, self.getMaxMemoryKilobytesString())
        hashMap.put(JvmStatisticsData.MAX_MEMORY_MEGABYTES, self.getMaxMemoryMegabytesString())
        hashMap.put(JvmStatisticsData.NUMBER_OF_THREADS, self.getNumberOfThreadsString())
        hashMap.put(JvmStatisticsData.TOTAL_MEMORY_BYTES, self.getTotalMemoryBytesString())
        hashMap.put(JvmStatisticsData.TOTAL_MEMORY_KILOBYTES, self.getTotalMemoryKilobytesString())
        hashMap.put(JvmStatisticsData.TOTAL_MEMORY_MEGABYTES, self.getTotalMemoryMegabytesString())
        return hashMap
    

    # throws Exception
    def getKey(self) -> object:
        from org.allbinary.logic.communication.java.vm.stats.JvmStatisticsData import JvmStatisticsData
        return JvmStatisticsData.NAME
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        vector: BasicArrayList = BasicArrayListD()
        vector.add(self.getFreeMemoryBytesString())
        vector.add(self.getFreeMemoryKilobytesString())
        vector.add(self.getFreeMemoryMegabytesString())
        vector.add(self.getMaxMemoryBytesString())
        vector.add(self.getMaxMemoryKilobytesString())
        vector.add(self.getMaxMemoryMegabytesString())
        vector.add(self.getNumberOfThreadsString())
        vector.add(self.getTotalMemoryBytesString())
        vector.add(self.getTotalMemoryKilobytesString())
        vector.add(self.getTotalMemoryMegabytesString())
        return vector
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil


