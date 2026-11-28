# Generated Code Do Not Modify
# package org.allbinary.animation

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import lazy_static


class FixedPoint:
    instance: FixedPoint = None

    def _init_fields(self) -> None:
        self.ONE: int = ((((1) << ((16) & 31)) + 0x80000000) % 0x100000000 - 0x80000000)

    def __init__(self) -> None:
        __class__._init_fields(self)
    

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
            return __class__.__dict__["toFixed_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["toFixed_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("toFixed_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().toFixed(*args)
    

    def mul(self, a: int, b: int) -> int:
        return (int((a * b)) >> (int(16) & 63))
    

    def div(self, a: int, b: int) -> int:
        return (int(((a) << 16) / b))
    

    def toInt(self, fixed: int) -> int:
        return int(fixed) >> (int(16) & 31)


def _FixedPoint_instance() -> object:
    return FixedPoint()

lazy_static(FixedPoint, "instance", _FixedPoint_instance)

