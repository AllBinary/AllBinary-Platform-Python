# Generated Code Do Not Modify
# package org.allbinary.logic.math.permutations

from __future__ import annotations

from org.allbinary.logic.util.visitor.Visitor import Visitor


class ObjectPermutationVisitor(Visitor):

    def _init_fields(self) -> None:
        self.data: list[object] = None
        self.stringBuilder: StringMaker = StringMaker()
    

    def __init__(self, data: list[object]) -> None:
        super().__init__()
        self._init_fields()
        self.data = data
    

    def visit(self, anyType: object) -> object:
        self.stringBuilder.delete(0, self.stringBuilder.length())
        self.print_(self.data, self.stringBuilder)
        return NullUtil.getInstance().NULL_OBJECT
    

    def print_(self, data: list[object]) -> None:
        stringBuilder: StringMaker = StringMaker()
        self.print_(data, stringBuilder)
    

    # Java overloaded method: Python keeps the last definition
    def print_(self, data: list[object], stringBuilder: StringMaker) -> None:
        tsUtil: TsUtil = TsUtil.getInstance()
        size: int = len(data)
        for i in range(0, size):
            stringBuilder.appendint(int(tsUtil.hashCode(data[i])))
            stringBuilder.append(CommonSeps.getInstance().SPACE)
        print(str(stringBuilder))
from org.allbinary.TsUtil import TsUtil
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


