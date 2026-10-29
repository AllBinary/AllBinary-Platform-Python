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
        self.keyEventWrapper: ABKeyEventWrapper = ABKeyEventWrapper.getInstance()
        self.UNKNOWN: PCGameKey = PCGameKey(self.keyEventWrapper.VK_UNDEFINED, "UNKNOWN")
        self.ENTER: PCGameKey = PCGameKey(5, "Enter")
        self._A: PCGameKey = PCGameKey(self.keyEventWrapper.VK_A, "A")
        self._B: PCGameKey = PCGameKey(self.keyEventWrapper.VK_B, "B")
        self._C: PCGameKey = PCGameKey(self.keyEventWrapper.VK_C, "C")
        self._D: PCGameKey = PCGameKey(self.keyEventWrapper.VK_D, "D")
        self._E: PCGameKey = PCGameKey(self.keyEventWrapper.VK_E, "E")
        self._F: PCGameKey = PCGameKey(self.keyEventWrapper.VK_F, "F")
        self._G: PCGameKey = PCGameKey(self.keyEventWrapper.VK_G, "G")
        self._H: PCGameKey = PCGameKey(self.keyEventWrapper.VK_H, "H")
        self._I: PCGameKey = PCGameKey(self.keyEventWrapper.VK_I, "I")
        self._J: PCGameKey = PCGameKey(self.keyEventWrapper.VK_J, "J")
        self._K: PCGameKey = PCGameKey(self.keyEventWrapper.VK_K, "K")
        self._L: PCGameKey = PCGameKey(self.keyEventWrapper.VK_L, "L")
        self._M: PCGameKey = PCGameKey(self.keyEventWrapper.VK_M, "M")
        self._N: PCGameKey = PCGameKey(self.keyEventWrapper.VK_N, "N")
        self._O: PCGameKey = PCGameKey(self.keyEventWrapper.VK_O, "O")
        self._P: PCGameKey = PCGameKey(self.keyEventWrapper.VK_P, "P")
        self._Q: PCGameKey = PCGameKey(self.keyEventWrapper.VK_Q, "Q")
        self._R: PCGameKey = PCGameKey(self.keyEventWrapper.VK_R, "R")
        self._S: PCGameKey = PCGameKey(self.keyEventWrapper.VK_S, "S")
        self._T: PCGameKey = PCGameKey(self.keyEventWrapper.VK_T, "T")
        self._U: PCGameKey = PCGameKey(self.keyEventWrapper.VK_U, "U")
        self._V: PCGameKey = PCGameKey(self.keyEventWrapper.VK_V, "V")
        self._W: PCGameKey = PCGameKey(self.keyEventWrapper.VK_W, "W")
        self._X: PCGameKey = PCGameKey(self.keyEventWrapper.VK_X, "X")
        self._Y: PCGameKey = PCGameKey(self.keyEventWrapper.VK_Y, "Y")
        self._Z: PCGameKey = PCGameKey(self.keyEventWrapper.VK_Z, "Z")
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
        self.ZERO: PCGameKey = PCGameKey(self.keyEventWrapper.VK_0, CommonPhoneStrings.getInstance().ZERO)
        self.ONE: PCGameKey = PCGameKey(self.keyEventWrapper.VK_1, CommonPhoneStrings.getInstance().ONE)
        self.TWO: PCGameKey = PCGameKey(self.keyEventWrapper.VK_2, CommonPhoneStrings.getInstance().TWO)
        self.THREE: PCGameKey = PCGameKey(self.keyEventWrapper.VK_3, CommonPhoneStrings.getInstance().THREE)
        self.FOUR: PCGameKey = PCGameKey(self.keyEventWrapper.VK_4, CommonPhoneStrings.getInstance().FOUR)
        self.FIVE: PCGameKey = PCGameKey(self.keyEventWrapper.VK_5, CommonPhoneStrings.getInstance().FIVE)
        self.SIX: PCGameKey = PCGameKey(self.keyEventWrapper.VK_6, CommonPhoneStrings.getInstance().SIX)
        self.SEVEN: PCGameKey = PCGameKey(self.keyEventWrapper.VK_7, CommonPhoneStrings.getInstance().SEVEN)
        self.EIGHT: PCGameKey = PCGameKey(self.keyEventWrapper.VK_8, CommonPhoneStrings.getInstance().EIGHT)
        self.NINE: PCGameKey = PCGameKey(self.keyEventWrapper.VK_9, CommonPhoneStrings.getInstance().NINE)
        self.DPAD_UP: PCGameKey = PCGameKey(self.keyEventWrapper.VK_UP, CommonPhoneStrings.getInstance().UP)
        self.DPAD_DOWN: PCGameKey = PCGameKey(self.keyEventWrapper.VK_DOWN, CommonPhoneStrings.getInstance().DOWN)
        self.DPAD_LEFT: PCGameKey = PCGameKey(self.keyEventWrapper.VK_LEFT, CommonPhoneStrings.getInstance().LEFT)
        self.DPAD_RIGHT: PCGameKey = PCGameKey(self.keyEventWrapper.VK_RIGHT, CommonPhoneStrings.getInstance().RIGHT)
        self.DPAD_UP2: PCGameKey = self.DPAD_UP
        self.DPAD_DOWN2: PCGameKey = self.DPAD_DOWN
        self.DPAD_LEFT2: PCGameKey = self.DPAD_LEFT
        self.DPAD_RIGHT2: PCGameKey = self.DPAD_RIGHT
        self.COMMA: PCGameKey = PCGameKey(self.keyEventWrapper.VK_COMMA, "COMMA")
        self.SPACE: PCGameKey = PCGameKey(self.keyEventWrapper.VK_SPACE, "SPACE")
        self.DEL: PCGameKey = PCGameKey(self.keyEventWrapper.VK_DELETE, "DEL")
        self.STAR: PCGameKey = PCGameKey(42, CommonPhoneStrings.getInstance().STAR)
        self.QUESTION: PCGameKey = PCGameKey(47, "?")
        self.PERIOD: PCGameKey = PCGameKey(self.keyEventWrapper.VK_PERIOD, CommonSeps.getInstance().PERIOD)
        self.ESCAPE: PCGameKey = PCGameKey(self.keyEventWrapper.VK_ESCAPE, "Esc")
        self.BACK_SPACE: PCGameKey = PCGameKey(self.keyEventWrapper.VK_BACK_SPACE, "Backspace")

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
from org.allbinary.game.input.ABKeyEventWrapper import ABKeyEventWrapper
from org.allbinary.game.input.PCGameKey import PCGameKey


PCKeyFactory.SINGLETON = PCKeyFactory()

