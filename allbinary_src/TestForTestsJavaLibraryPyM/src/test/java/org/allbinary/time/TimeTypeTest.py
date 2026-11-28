# Generated Code Do Not Modify
# package org.allbinary.time

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
import datetime
from org.allbinary.time.TimeTypeUtil import TimeTypeUtil


class TimeTypeTest:
    @java_inherited_overloads
    class TestableTimeTypeUtil(TimeTypeUtil):
        def _java_defaults(self):
            vars(self).setdefault("hour", 0)

        def _init_fields(self) -> None:
            if "hour" not in vars(self): self.hour: int = 0
        

        def __init__(self, hour: int) -> None:
            __class__._java_defaults(self)
            super().__init__()
            __class__._init_fields(self)
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
        from org.junit.jupiter.api.Assertions import Assertions
        from org.junit.jupiter.api.DisplayName import DisplayName
        from org.junit.jupiter.api.Test import Test
        """Otherwise - statement - ForEachStmt"""
    

    def isNight_returnsTrue_for_hours_greater_than_18(self) -> None:
        from org.junit.jupiter.api.Assertions import Assertions
        from org.junit.jupiter.api.DisplayName import DisplayName
        from org.junit.jupiter.api.Test import Test
        """Otherwise - statement - ForEachStmt"""
    

    def isNight_returnsFalse_for_boundary_hours_6_and_18(self) -> None:
        from org.junit.jupiter.api.Assertions import Assertions
        from org.junit.jupiter.api.DisplayName import DisplayName
        from org.junit.jupiter.api.Test import Test
        """Otherwise - statement - ForEachStmt"""
    

    def getNightOrDay_returns_expected_label(self) -> None:
        from org.junit.jupiter.api.Assertions import Assertions
        from org.junit.jupiter.api.DisplayName import DisplayName
        from org.junit.jupiter.api.Test import Test
        nightUtil: TimeTypeUtil = TimeTypeTest.TestableTimeTypeUtil(0)
        Assertions.assertEquals(nightUtil.NIGHT, nightUtil.getNightOrDay())
        dayUtil: TimeTypeUtil = TimeTypeTest.TestableTimeTypeUtil(12)
        Assertions.assertEquals(dayUtil.DAY, dayUtil.getNightOrDay())
    

    def getHourOfDay_long_converts_epoch_to_local_hour(self) -> None:
        from org.junit.jupiter.api.Assertions import Assertions
        from org.junit.jupiter.api.DisplayName import DisplayName
        from org.junit.jupiter.api.Test import Test
        util: TimeTypeUtil = TimeTypeUtil()
        """Otherwise - statement - ForEachStmt"""
    

    def isNight_long_expected_ranges(self) -> None:
        from org.junit.jupiter.api.Assertions import Assertions
        from org.junit.jupiter.api.DisplayName import DisplayName
        from org.junit.jupiter.api.Test import Test
        util: TimeTypeUtil = TimeTypeUtil()
        """Otherwise - statement - ForEachStmt"""
        """Otherwise - statement - ForEachStmt"""
    

    def getNightOrDay_long_consistency(self) -> None:
        from org.junit.jupiter.api.Assertions import Assertions
        from org.junit.jupiter.api.DisplayName import DisplayName
        from org.junit.jupiter.api.Test import Test
        util: TimeTypeUtil = TimeTypeUtil()
        nightMillis: int = TimeTypeTest.millisForHourLocal(0)
        dayMillis: int = TimeTypeTest.millisForHourLocal(12)
        Assertions.assertEquals(util.NIGHT, util.getNightOrDay(nightMillis))
        Assertions.assertEquals(util.DAY, util.getNightOrDay(dayMillis))
    

    def boundaries_day_for_long_based_api(self) -> None:
        from org.junit.jupiter.api.Assertions import Assertions
        from org.junit.jupiter.api.DisplayName import DisplayName
        from org.junit.jupiter.api.Test import Test
        util: TimeTypeUtil = TimeTypeUtil()
        """Otherwise - statement - ForEachStmt"""
    

    def constants_accessible_and_stable(self) -> None:
        from org.junit.jupiter.api.Assertions import Assertions
        from org.junit.jupiter.api.DisplayName import DisplayName
        from org.junit.jupiter.api.Test import Test
        util: TimeTypeUtil = TimeTypeUtil()
        Assertions.assertEquals("Night", util.NIGHT)
        Assertions.assertEquals("Day", util.DAY)
    

    def getInstance_returns_same_singleton(self) -> None:
        from org.junit.jupiter.api.Assertions import Assertions
        from org.junit.jupiter.api.DisplayName import DisplayName
        from org.junit.jupiter.api.Test import Test
        a: TimeTypeUtil = TimeTypeUtil.getInstance()
        b: TimeTypeUtil = TimeTypeUtil.getInstance()
        Assertions.assertSame(a, b)
# from java.util.Calendar import Calendar
# from org.junit.jupiter.api.Assertions import Assertions
# from org.junit.jupiter.api.DisplayName import DisplayName
# from org.junit.jupiter.api.Test import Test


