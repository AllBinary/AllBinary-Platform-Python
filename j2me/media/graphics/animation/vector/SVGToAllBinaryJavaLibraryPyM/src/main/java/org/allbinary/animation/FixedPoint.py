# Generated Code Do Not Modify
# package org.allbinary.animation

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class FixedPoint:
    instance: FixedPoint = None

    def _init_fields(self) -> None:
        self.ONE: int = 1 << 16

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> FixedPoint:
        return FixedPoint.instance
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def toFixed_j1_1(self, val: float) -> int:
        return int((val * 65536.0))
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def toFixed_j1_2(self, val: float) -> int:
        return int((val * 65536.0))

    def toFixed(self, *args):
        if len(args) == 1 and True and isinstance(args[0], (int, float)) and not isinstance(args[0], bool):
            return self.toFixed_j1_1(*args)
        if len(args) == 1:
            return self.toFixed_j1_2(*args)
        return getattr(self, "toFixed_j" + str(len(args)))(*args)
    

    def mul(self, a: int, b: int) -> int:
        return ((a * b) >> 16)
    

    def div(self, a: int, b: int) -> int:
        return (int(((a) << 16) / b))
    

    def toInt(self, fixed: int) -> int:
        return fixed >> 16


def _FixedPoint_instance() -> object:
    return FixedPoint()

lazy_static(FixedPoint, "instance", _FixedPoint_instance)

