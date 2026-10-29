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
        from org.allbinary.game.input.PCGameKey import PCGameKey
        return PCGameKey.getString(keyCode)
    

    def isSubmission(self, input: Input) -> bool:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        return PCKeyFactory.getInstance().isSubmission(input)
    

    def isDelete(self, input: Input) -> bool:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        return PCKeyFactory.getInstance().isDelete(input)
    

    def isBackSpace(self, input: Input) -> bool:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        return PCKeyFactory.getInstance().isBackSpace(input)
    

    def isUp(self, input: Input) -> bool:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        return PCKeyFactory.getInstance().isUp(input)
    

    def isDown(self, input: Input) -> bool:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        return PCKeyFactory.getInstance().isDown(input)
    

    def isEnter(self, input: Input) -> bool:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        return PCKeyFactory.getInstance().isEnter(input)
    

    def isLeft(self, input: Input) -> bool:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        return PCKeyFactory.getInstance().isLeft(input)
    

    def isRight(self, input: Input) -> bool:
        from org.allbinary.game.input.PCKeyFactory import PCKeyFactory
        return PCKeyFactory.getInstance().isRight(input)


