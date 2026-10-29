# Generated Code Do Not Modify

from __future__ import annotations



class AppTest:
    

    def testAddition(self) -> None:
        Assertions.assertEquals(2, 1 + 1)
    

    def testStringEquality(self) -> None:
        expected: str = "Hello World!"
        actual: str = "Hello World!"
        Assertions.assertEquals(expected, actual)
    

    def testBooleanAssertions(self) -> None:
        Assertions.assertTrue(True)
        Assertions.assertFalse(False)
from org.junit.jupiter.api.Assertions import Assertions
from org.junit.jupiter.api.DisplayName import DisplayName
from org.junit.jupiter.api.Test import Test


