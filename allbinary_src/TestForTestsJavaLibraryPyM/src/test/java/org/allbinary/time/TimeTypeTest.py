# Generated Code Do Not Modify
# package org.allbinary.time

from __future__ import annotations

import datetime


class TimeTypeTest:
    class TestableTimeTypeUtil(TimeTypeUtil):

        def _init_fields(self) -> None:
            self.hour: int = None
        

        def __init__(self, hour: int) -> None:
            super().__init__()
            self._init_fields()
            self.hour = hour
        

        def getHourOfDay(self) -> int:
            return self.hour
    

    @staticmethod
    def millisForHourLocal(hour: int) -> int:
        cal: datetime.datetime = datetime.datetime.now()
        cal.set(Calendar.HOUR_OF_DAY, hour)
        cal.set(Calendar.MINUTE, 0)
        cal.set(Calendar.SECOND, 0)
        cal.set(Calendar.MILLISECOND, 0)
        return cal.getTimeInMillis()
    

    def isNight_returnsTrue_for_hours_less_than_6(self) -> None:
        from org.allbinary.time.TestableTimeTypeUtil import TestableTimeTypeUtil
        """Otherwise - statement - ForEachStmt"""
    

    def isNight_returnsTrue_for_hours_greater_than_18(self) -> None:
        from org.allbinary.time.TestableTimeTypeUtil import TestableTimeTypeUtil
        """Otherwise - statement - ForEachStmt"""
    

    def isNight_returnsFalse_for_boundary_hours_6_and_18(self) -> None:
        from org.allbinary.time.TestableTimeTypeUtil import TestableTimeTypeUtil
        """Otherwise - statement - ForEachStmt"""
    

    def getNightOrDay_returns_expected_label(self) -> None:
        from org.allbinary.time.TestableTimeTypeUtil import TestableTimeTypeUtil
        from org.allbinary.time.TestableTimeTypeUtil import TestableTimeTypeUtil
        nightUtil: TimeTypeUtil = TestableTimeTypeUtil(0)
        Assertions.assertEquals(nightUtil.NIGHT, nightUtil.getNightOrDay())
        dayUtil: TimeTypeUtil = TestableTimeTypeUtil(12)
        Assertions.assertEquals(dayUtil.DAY, dayUtil.getNightOrDay())
    

    def getHourOfDay_long_converts_epoch_to_local_hour(self) -> None:
        from org.allbinary.time.TimeTypeUtil import TimeTypeUtil
        util: TimeTypeUtil = TimeTypeUtil()
        """Otherwise - statement - ForEachStmt"""
    

    def isNight_long_expected_ranges(self) -> None:
        from org.allbinary.time.TimeTypeUtil import TimeTypeUtil
        util: TimeTypeUtil = TimeTypeUtil()
        """Otherwise - statement - ForEachStmt"""
        """Otherwise - statement - ForEachStmt"""
    

    def getNightOrDay_long_consistency(self) -> None:
        from org.allbinary.time.TimeTypeUtil import TimeTypeUtil
        util: TimeTypeUtil = TimeTypeUtil()
        nightMillis: int = TimeTypeTest.millisForHourLocal(0)
        dayMillis: int = TimeTypeTest.millisForHourLocal(12)
        Assertions.assertEquals(util.NIGHT, util.getNightOrDay(nightMillis))
        Assertions.assertEquals(util.DAY, util.getNightOrDay(dayMillis))
    

    def boundaries_day_for_long_based_api(self) -> None:
        from org.allbinary.time.TimeTypeUtil import TimeTypeUtil
        util: TimeTypeUtil = TimeTypeUtil()
        """Otherwise - statement - ForEachStmt"""
    

    def constants_accessible_and_stable(self) -> None:
        from org.allbinary.time.TimeTypeUtil import TimeTypeUtil
        util: TimeTypeUtil = TimeTypeUtil()
        Assertions.assertEquals("Night", util.NIGHT)
        Assertions.assertEquals("Day", util.DAY)
    

    def getInstance_returns_same_singleton(self) -> None:
        from org.allbinary.time.TimeTypeUtil import TimeTypeUtil
        from org.allbinary.time.TimeTypeUtil import TimeTypeUtil
        a: TimeTypeUtil = TimeTypeUtil.getInstance()
        b: TimeTypeUtil = TimeTypeUtil.getInstance()
        Assertions.assertSame(a, b)
# from java.util.Calendar import Calendar
from org.junit.jupiter.api.Assertions import Assertions
from org.junit.jupiter.api.DisplayName import DisplayName
from org.junit.jupiter.api.Test import Test


