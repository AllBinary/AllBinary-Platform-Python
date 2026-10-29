# Generated Code Do Not Modify
# package org.allbinary.logic.math

from __future__ import annotations



class MathUtil:
    instance: MathUtil = None

    def _init_fields(self) -> None:
        self.ACCURACY: int = 100

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> MathUtil:
        return MathUtil.instance
    

    def getTotalDigits(self, digits: int) -> int:
        total: int = 0
        while digits > 0:
            digits = int(digits / 10)
            total += 1
        return total
    

    def sqrt(self, value: int) -> int:
        if value <= 1:
            return value
        accumulated: int = value >> 1
        result: int = (accumulated + (int(value / accumulated))) >> 1
        while True:
            accumulated = result
            result = (accumulated + (int(value / accumulated))) >> 1
            if not (accumulated > result):
                break
        return accumulated
    

    def sqrtd(self, x: int) -> float:
        if x == 0:
            return 0.0
        if x < 0:
            return -1.0
        result: float = float(x)
        for index in range(0, self.ACCURACY):
            result = (result + (float(x) / result)) / 2.0
        return result
    

    def abs(self, value: int) -> int:
        return (-value if (value < 0) else value)
    

    def abslong(self, value: int) -> int:
        return (-value if (value < 0) else value)
    

    def min(self, value: int, value2: int) -> int:
        return (value if (value <= value2) else value2)
    

    def max(self, value: int, value2: int) -> int:
        return (value if (value >= value2) else value2)
from jsinterop.annotations.JsType import JsType


MathUtil.instance = MathUtil()

