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



class PCKeyFactory:
    SINGLETON: PCKeyFactory = None

    def _init_fields(self) -> None:
        self.UNKNOWN: PCGameKey = PCGameKey(254, "UNKNOWN")
        self.ENTER: PCGameKey = PCGameKey(13, "Enter")
        self._A: PCGameKey = PCGameKey(65, "A")
        self._B: PCGameKey = PCGameKey(66, "B")
        self._C: PCGameKey = PCGameKey(67, "C")
        self._D: PCGameKey = PCGameKey(68, "D")
        self._E: PCGameKey = PCGameKey(69, "E")
        self._F: PCGameKey = PCGameKey(70, "F")
        self._G: PCGameKey = PCGameKey(71, "G")
        self._H: PCGameKey = PCGameKey(72, "H")
        self._I: PCGameKey = PCGameKey(73, "I")
        self._J: PCGameKey = PCGameKey(74, "J")
        self._K: PCGameKey = PCGameKey(75, "K")
        self._L: PCGameKey = PCGameKey(76, "L")
        self._M: PCGameKey = PCGameKey(77, "M")
        self._N: PCGameKey = PCGameKey(78, "N")
        self._O: PCGameKey = PCGameKey(79, "O")
        self._P: PCGameKey = PCGameKey(80, "P")
        self._Q: PCGameKey = PCGameKey(81, "Q")
        self._R: PCGameKey = PCGameKey(82, "R")
        self._S: PCGameKey = PCGameKey(83, "S")
        self._T: PCGameKey = PCGameKey(84, "T")
        self._U: PCGameKey = PCGameKey(85, "U")
        self._V: PCGameKey = PCGameKey(86, "V")
        self._W: PCGameKey = PCGameKey(87, "W")
        self._X: PCGameKey = PCGameKey(88, "X")
        self._Y: PCGameKey = PCGameKey(89, "Y")
        self._Z: PCGameKey = PCGameKey(90, "Z")
        self.a: PCGameKey = PCGameKey(97, "a")
        self.b: PCGameKey = PCGameKey(98, "b")
        self.c: PCGameKey = PCGameKey(99, "c")
        self.d: PCGameKey = PCGameKey(100, "d")
        self.e: PCGameKey = PCGameKey(101, "e")
        self.f: PCGameKey = PCGameKey(102, "f")
        self.g: PCGameKey = PCGameKey(103, "g")
        self.h: PCGameKey = PCGameKey(104, "h")
        self.i: PCGameKey = PCGameKey(105, "i")
        self.j: PCGameKey = PCGameKey(106, "j")
        self.k: PCGameKey = PCGameKey(107, "k")
        self.l: PCGameKey = PCGameKey(108, "l")
        self.m: PCGameKey = PCGameKey(109, "m")
        self.n: PCGameKey = PCGameKey(110, "n")
        self.o: PCGameKey = PCGameKey(111, "o")
        self.p: PCGameKey = PCGameKey(112, "p")
        self.q: PCGameKey = PCGameKey(113, "q")
        self.r: PCGameKey = PCGameKey(114, "r")
        self.s: PCGameKey = PCGameKey(115, "s")
        self.t: PCGameKey = PCGameKey(116, "t")
        self.u: PCGameKey = PCGameKey(117, "u")
        self.v: PCGameKey = PCGameKey(118, "v")
        self.w: PCGameKey = PCGameKey(119, "w")
        self.x: PCGameKey = PCGameKey(120, PositionStrings.getInstance().X)
        self.y: PCGameKey = PCGameKey(121, PositionStrings.getInstance().Y)
        self.z: PCGameKey = PCGameKey(122, "z")
        self.ZERO: PCGameKey = PCGameKey(48, CommonPhoneStrings.getInstance().ZERO)
        self.ONE: PCGameKey = PCGameKey(49, CommonPhoneStrings.getInstance().ONE)
        self.TWO: PCGameKey = PCGameKey(50, CommonPhoneStrings.getInstance().TWO)
        self.THREE: PCGameKey = PCGameKey(51, CommonPhoneStrings.getInstance().THREE)
        self.FOUR: PCGameKey = PCGameKey(52, CommonPhoneStrings.getInstance().FOUR)
        self.FIVE: PCGameKey = PCGameKey(53, CommonPhoneStrings.getInstance().FIVE)
        self.SIX: PCGameKey = PCGameKey(54, CommonPhoneStrings.getInstance().SIX)
        self.SEVEN: PCGameKey = PCGameKey(55, CommonPhoneStrings.getInstance().SEVEN)
        self.EIGHT: PCGameKey = PCGameKey(56, CommonPhoneStrings.getInstance().EIGHT)
        self.NINE: PCGameKey = PCGameKey(57, CommonPhoneStrings.getInstance().NINE)
        self.DPAD_UP: PCGameKey = PCGameKey(38, CommonPhoneStrings.getInstance().UP)
        self.DPAD_DOWN: PCGameKey = PCGameKey(40, CommonPhoneStrings.getInstance().DOWN)
        self.DPAD_LEFT: PCGameKey = PCGameKey(37, CommonPhoneStrings.getInstance().LEFT)
        self.DPAD_RIGHT: PCGameKey = PCGameKey(39, CommonPhoneStrings.getInstance().RIGHT)
        self.DPAD_UP2: PCGameKey = self.DPAD_UP
        self.DPAD_DOWN2: PCGameKey = self.DPAD_DOWN
        self.DPAD_LEFT2: PCGameKey = self.DPAD_LEFT
        self.DPAD_RIGHT2: PCGameKey = self.DPAD_RIGHT
        self.COMMA: PCGameKey = PCGameKey(44, "COMMA")
        self.SPACE: PCGameKey = PCGameKey(32, "SPACE")
        self.DEL: PCGameKey = PCGameKey(46, "DEL")
        self.STAR: PCGameKey = PCGameKey(42, CommonPhoneStrings.getInstance().STAR)
        self.QUESTION: PCGameKey = PCGameKey(47, "?")
        self.PERIOD: PCGameKey = PCGameKey(46, CommonSeps.getInstance().PERIOD)
        self.ESCAPE: PCGameKey = PCGameKey(27, "Esc")
        self.BACK_SPACE: PCGameKey = PCGameKey(8, "Backspace")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PCKeyFactory:
        return PCKeyFactory.SINGLETON
    

    def isSubmission(self, input: Input) -> bool:
        if input == self.ENTER:
            return True
        return False
    

    def isDelete(self, input: Input) -> bool:
        if input == self.DEL:
            return True
        return False
    

    def isBackSpace(self, input: Input) -> bool:
        if input == self.BACK_SPACE:
            return True
        return False
    

    def isUp(self, input: Input) -> bool:
        if input == self.DPAD_UP or input == self.DPAD_UP2:
            return True
        return False
    

    def isDown(self, input: Input) -> bool:
        if input == self.DPAD_DOWN or input == self.DPAD_DOWN2:
            return True
        return False
    

    def isLeft(self, input: Input) -> bool:
        if input == self.DPAD_LEFT or input == self.DPAD_LEFT2:
            return True
        return False
    

    def isRight(self, input: Input) -> bool:
        if input == self.DPAD_RIGHT or input == self.DPAD_RIGHT2:
            return True
        return False
    

    def isEnter(self, input: Input) -> bool:
        if input == self.ENTER:
            return True
        return False
from org.allbinary.math.PositionStrings import PositionStrings
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.game.input.PCGameKey import PCGameKey


PCKeyFactory.SINGLETON = PCKeyFactory()

