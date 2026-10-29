# Generated Code Do Not Modify
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class PlatformKeyFactory:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.androidKeyFactory: AndroidKeyFactory = ActivityFractureControllerUtilFactory.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PlatformKeyFactory:
        if PlatformKeyFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            PlatformKeyFactory.instance = PlatformKeyFactory()
        return PlatformKeyFactory.instance
    

    def getString(self, keyCode: int) -> str:
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        return AndroidGameKey.getString(keyCode)
    

    def isSubmission(self, input: Input) -> bool:
        return self.androidKeyFactory.isSubmission(input)
    

    def isDelete(self, input: Input) -> bool:
        return self.androidKeyFactory.isDelete(input)
    

    def isBackSpace(self, input: Input) -> bool:
        return self.androidKeyFactory.isBackSpace(input)
    

    def isLeft(self, input: Input) -> bool:
        return self.androidKeyFactory.isLeft(input)
    

    def isRight(self, input: Input) -> bool:
        return self.androidKeyFactory.isRight(input)
    

    def isUp(self, input: Input) -> bool:
        return self.androidKeyFactory.isUp(input)
    

    def isDown(self, input: Input) -> bool:
        return self.androidKeyFactory.isDown(input)
    

    def isEnter(self, input: Input) -> bool:
        return self.androidKeyFactory.isEnter(input)
from org.allbinary.game.input.ActivityFractureControllerUtilFactory import ActivityFractureControllerUtilFactory


