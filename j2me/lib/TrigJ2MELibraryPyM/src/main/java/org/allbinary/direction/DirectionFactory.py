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
# package org.allbinary.direction

from __future__ import annotations



class DirectionFactory:
    instance: DirectionFactory = None

    def _init_fields(self) -> None:
        self.NAME: str = "DIRECTION"
        self.LEFT: Direction = Direction(CommonPhoneStrings.getInstance().LEFT, "WEST", 0, 1)
        self.RIGHT: Direction = Direction(CommonPhoneStrings.getInstance().RIGHT, "EAST", 1, 0)
        self.DOWN: Direction = Direction(CommonPhoneStrings.getInstance().DOWN, "SOUTH", 2, 0)
        self.UP: Direction = Direction(CommonPhoneStrings.getInstance().UP, "NORTH", 3, 0)
        self.UP_LEFT: Direction = None
        self.UP_RIGHT: Direction = None
        self.DOWN_LEFT: Direction = None
        self.DOWN_RIGHT: Direction = None
        self.NOT_BORDERED_WITH: Direction = Direction("NOT_BORDERED_WITH", "NOT_BORDERED_WITH", 8, 0)
        self.NO_DIRECTION: Direction = Direction("NO_DIRECTION", "NO_DIRECTION", 9, 0)
        self.TOP: Direction = Direction("TOP", "TOP", 10, 0)
        self.BOTTOM: Direction = Direction("BOTTOM", "BOTTOM", 11, 0)
        self.ALL_DIRECTION: Direction = Direction("ALL_DIRECTION", "ALL_DIRECTION", 12, 0)
    

    @staticmethod
    def getInstance() -> DirectionFactory:
        return DirectionFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.direction.Direction import Direction
        from org.allbinary.direction.Direction import Direction
        from org.allbinary.direction.Direction import Direction
        from org.allbinary.direction.Direction import Direction
        self._init_fields()
        stringBuffer: StringMaker = StringMaker()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        self.UP_LEFT = Direction("UP LEFT", str(stringBuffer.append(self.UP.getOtherName()).append(commonSeps.SPACE).append(self.LEFT.getOtherName())), 4, 0)
        stringBuffer.delete(0, stringBuffer.length())
        self.UP_RIGHT = Direction("UP RIGHT", str(stringBuffer.append(self.UP.getOtherName()).append(commonSeps.SPACE).append(self.RIGHT.getOtherName())), 5, 0)
        stringBuffer.delete(0, stringBuffer.length())
        self.DOWN_LEFT = Direction("DOWN LEFT", str(stringBuffer.append(self.DOWN.getOtherName()).append(commonSeps.SPACE).append(self.LEFT.getOtherName())), 6, 0)
        stringBuffer.delete(0, stringBuffer.length())
        self.DOWN_RIGHT = Direction("DOWN RIGHT", str(stringBuffer.append(self.DOWN.getOtherName()).append(commonSeps.SPACE).append(self.RIGHT.getOtherName())), 7, 0)
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.direction.Direction import Direction


DirectionFactory.instance = DirectionFactory()

