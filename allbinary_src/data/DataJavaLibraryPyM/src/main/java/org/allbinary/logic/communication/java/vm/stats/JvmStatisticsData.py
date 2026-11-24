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

from java.lang.JavaRuntimeStatic import lazy_static


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


def _JvmStatisticsData_NAME() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "NAME"

lazy_static(JvmStatisticsData, "NAME", _JvmStatisticsData_NAME)

def _JvmStatisticsData_TOTAL_MEMORY_BYTES() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "TOTAL_MEMORY_BYTES"

lazy_static(JvmStatisticsData, "TOTAL_MEMORY_BYTES", _JvmStatisticsData_TOTAL_MEMORY_BYTES)

def _JvmStatisticsData_TOTAL_MEMORY_KILOBYTES() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "TOTAL_MEMORY_KILOBYTES"

lazy_static(JvmStatisticsData, "TOTAL_MEMORY_KILOBYTES", _JvmStatisticsData_TOTAL_MEMORY_KILOBYTES)

def _JvmStatisticsData_TOTAL_MEMORY_MEGABYTES() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "TOTAL_MEMORY_MEGABYTES"

lazy_static(JvmStatisticsData, "TOTAL_MEMORY_MEGABYTES", _JvmStatisticsData_TOTAL_MEMORY_MEGABYTES)

def _JvmStatisticsData_FREE_MEMORY_BYTES() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "FREE_MEMORY_BYTES"

lazy_static(JvmStatisticsData, "FREE_MEMORY_BYTES", _JvmStatisticsData_FREE_MEMORY_BYTES)

def _JvmStatisticsData_FREE_MEMORY_KILOBYTES() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "FREE_MEMORY_KILOBYTES"

lazy_static(JvmStatisticsData, "FREE_MEMORY_KILOBYTES", _JvmStatisticsData_FREE_MEMORY_KILOBYTES)

def _JvmStatisticsData_FREE_MEMORY_MEGABYTES() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "FREE_MEMORY_MEGABYTES"

lazy_static(JvmStatisticsData, "FREE_MEMORY_MEGABYTES", _JvmStatisticsData_FREE_MEMORY_MEGABYTES)

def _JvmStatisticsData_MAX_MEMORY_BYTES() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "MAX_MEMORY_BYTES"

lazy_static(JvmStatisticsData, "MAX_MEMORY_BYTES", _JvmStatisticsData_MAX_MEMORY_BYTES)

def _JvmStatisticsData_MAX_MEMORY_KILOBYTES() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "MAX_MEMORY_KILOBYTES"

lazy_static(JvmStatisticsData, "MAX_MEMORY_KILOBYTES", _JvmStatisticsData_MAX_MEMORY_KILOBYTES)

def _JvmStatisticsData_MAX_MEMORY_MEGABYTES() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "MAX_MEMORY_MEGABYTES"

lazy_static(JvmStatisticsData, "MAX_MEMORY_MEGABYTES", _JvmStatisticsData_MAX_MEMORY_MEGABYTES)

def _JvmStatisticsData_NUMBER_OF_THREADS() -> object:
    return str(JvmStatisticsData.JVM_STATISTICS) + "NUMBER_OF_THREADS"

lazy_static(JvmStatisticsData, "NUMBER_OF_THREADS", _JvmStatisticsData_NUMBER_OF_THREADS)

