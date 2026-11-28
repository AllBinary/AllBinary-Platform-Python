# Generated Code Do Not Modify
# package org.allbinary.logic.math.permutations

from __future__ import annotations

from java.lang.System import System
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.util.visitor.Visitor import Visitor


@java_inherited_overloads
class IntPermutationVisitor(Visitor):
    def _java_defaults(self):
        vars(self).setdefault("data", None)
        vars(self).setdefault("stringBuilder", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        if "data" not in vars(self): self.data: list[int] = None
        self.stringBuilder: StringMaker = StringMaker()
    

    def __init__(self, data: list[int]) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.data = data
    

    def visit(self, anyType: object) -> object:
        from org.allbinary.logic.NullUtil import NullUtil
        self.stringBuilder.delete(0, self.stringBuilder.length())
        self.print_(self.data, self.stringBuilder)
        return NullUtil.getInstance().NULL_OBJECT
    

    def print__j1(self, data: list[int]) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuilder: StringMaker = StringMaker()
        self.print_(data, stringBuilder)
    

    def print__j2(self, data: list[int], stringBuilder: StringMaker) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        commonSeps: CommonSeps = CommonSeps.getInstance()
        size: int = len(data)
        for i in range(0, size):
            stringBuilder.appendint(data[i])
            stringBuilder.append(commonSeps.SPACE)
        print(str(stringBuilder))

    def print_(self, *args):
        implementation = __class__.__dict__.get("print__j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().print_(*args)
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps


