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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class PlatformKeyFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT
    

    @staticmethod
    def getInstance() -> PlatformKeyFactory:
        if PlatformKeyFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            PlatformKeyFactory.instance = PlatformKeyFactory()
        return PlatformKeyFactory.instance
    

    def getString(self, keyCode: int) -> str:
        from org.allbinary.game.input.J2MEGameKey import J2MEGameKey
        return J2MEGameKey.getString(keyCode)
    

    def isSubmission(self, input: Input) -> bool:
        from org.allbinary.game.input.J2MEKeyFactory import J2MEKeyFactory
        return J2MEKeyFactory.getInstance().isSubmission(input)
    

    def isDelete(self, input: Input) -> bool:
        from org.allbinary.game.input.J2MEKeyFactory import J2MEKeyFactory
        return J2MEKeyFactory.getInstance().isDelete(input)
    

    def isBackSpace(self, input: Input) -> bool:
        from org.allbinary.game.input.J2MEKeyFactory import J2MEKeyFactory
        return J2MEKeyFactory.getInstance().isBackSpace(input)
    

    def isLeft(self, input: Input) -> bool:
        from org.allbinary.game.input.J2MEKeyFactory import J2MEKeyFactory
        return J2MEKeyFactory.getInstance().isLeft(input)
    

    def isRight(self, input: Input) -> bool:
        from org.allbinary.game.input.J2MEKeyFactory import J2MEKeyFactory
        return J2MEKeyFactory.getInstance().isRight(input)
    

    def isUp(self, input: Input) -> bool:
        from org.allbinary.game.input.J2MEKeyFactory import J2MEKeyFactory
        return J2MEKeyFactory.getInstance().isUp(input)
    

    def isDown(self, input: Input) -> bool:
        from org.allbinary.game.input.J2MEKeyFactory import J2MEKeyFactory
        return J2MEKeyFactory.getInstance().isDown(input)
    

    def isEnter(self, input: Input) -> bool:
        from org.allbinary.game.input.J2MEKeyFactory import J2MEKeyFactory
        return J2MEKeyFactory.getInstance().isEnter(input)


