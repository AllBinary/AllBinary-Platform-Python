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



class JvmStatisticsData:
    JVM_STATISTICS: str = "JVM_STATISTICS_"
    NAME: str = None
    TOTAL_MEMORY_BYTES: str = None
    TOTAL_MEMORY_KILOBYTES: str = None
    TOTAL_MEMORY_MEGABYTES: str = None
    FREE_MEMORY_BYTES: str = None
    FREE_MEMORY_KILOBYTES: str = None
    FREE_MEMORY_MEGABYTES: str = None
    MAX_MEMORY_BYTES: str = None
    MAX_MEMORY_KILOBYTES: str = None
    MAX_MEMORY_MEGABYTES: str = None
    NUMBER_OF_THREADS: str = None
    

    def __init__(self) -> None:
        super().__init__()


JvmStatisticsData.NAME = str(JvmStatisticsData.JVM_STATISTICS) + "NAME"

JvmStatisticsData.TOTAL_MEMORY_BYTES = str(JvmStatisticsData.JVM_STATISTICS) + "TOTAL_MEMORY_BYTES"

JvmStatisticsData.TOTAL_MEMORY_KILOBYTES = str(JvmStatisticsData.JVM_STATISTICS) + "TOTAL_MEMORY_KILOBYTES"

JvmStatisticsData.TOTAL_MEMORY_MEGABYTES = str(JvmStatisticsData.JVM_STATISTICS) + "TOTAL_MEMORY_MEGABYTES"

JvmStatisticsData.FREE_MEMORY_BYTES = str(JvmStatisticsData.JVM_STATISTICS) + "FREE_MEMORY_BYTES"

JvmStatisticsData.FREE_MEMORY_KILOBYTES = str(JvmStatisticsData.JVM_STATISTICS) + "FREE_MEMORY_KILOBYTES"

JvmStatisticsData.FREE_MEMORY_MEGABYTES = str(JvmStatisticsData.JVM_STATISTICS) + "FREE_MEMORY_MEGABYTES"

JvmStatisticsData.MAX_MEMORY_BYTES = str(JvmStatisticsData.JVM_STATISTICS) + "MAX_MEMORY_BYTES"

JvmStatisticsData.MAX_MEMORY_KILOBYTES = str(JvmStatisticsData.JVM_STATISTICS) + "MAX_MEMORY_KILOBYTES"

JvmStatisticsData.MAX_MEMORY_MEGABYTES = str(JvmStatisticsData.JVM_STATISTICS) + "MAX_MEMORY_MEGABYTES"

JvmStatisticsData.NUMBER_OF_THREADS = str(JvmStatisticsData.JVM_STATISTICS) + "NUMBER_OF_THREADS"

