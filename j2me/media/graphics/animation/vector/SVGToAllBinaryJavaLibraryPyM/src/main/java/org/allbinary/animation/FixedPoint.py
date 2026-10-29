# Generated Code Do Not Modify
# package org.allbinary.animation

from __future__ import annotations



class FixedPoint:
    instance: FixedPoint = None

    def _init_fields(self) -> None:
        self.ONE: int = 1 << 16

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> FixedPoint:
        return FixedPoint.instance
    

    def toFixed(self, val: float) -> int:
        return int((val * 65536.0))
    

    # Java overloaded method: Python keeps the last definition
    def toFixed(self, val: float) -> int:
        return int((val * 65536.0))
    

    def mul(self, a: int, b: int) -> int:
        return ((a * b) >> 16)
    

    def div(self, a: int, b: int) -> int:
        return (int(((a) << 16) / b))
    

    def toInt(self, fixed: int) -> int:
        return fixed >> 16


FixedPoint.instance = FixedPoint()

