# Generated Code Do Not Modify
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.android.ActivityFractureUtil import ActivityFractureUtil


class AndroidKeyFactory(ActivityFractureUtil):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.UNKNOWN: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_UNKNOWN, "UNKNOWN")
        self.KEYCODE_BUTTON_L1: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_R1: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_THUMBR: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_THUMBL: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_START: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_MODE: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_B: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_A: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_X: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_Y: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_L2: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_R2: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_SELECT: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_C: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_Z: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_1: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_10: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_11: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_12: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_13: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_14: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_15: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_16: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_2: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_3: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_4: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_5: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_6: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_7: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_8: AndroidGameKey = self.UNKNOWN
        self.KEYCODE_BUTTON_9: AndroidGameKey = self.UNKNOWN
        self.SOFT_LEFT: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_SOFT_LEFT, "SOFT_LEFT")
        self.SOFT_RIGHT: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_SOFT_RIGHT, "SOFT_RIGHT")
        self.HOME: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_HOME, "HOME")
        self.BACK: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_BACK, "BACK")
        self.CALL: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_CALL, "CALL")
        self.ENDCALL: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_ENDCALL, "ENDCALL")
        self.ZERO: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_0, CommonPhoneStrings.getInstance().ZERO)
        self.ONE: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_1, CommonPhoneStrings.getInstance().ONE)
        self.TWO: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_2, CommonPhoneStrings.getInstance().TWO)
        self.THREE: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_3, CommonPhoneStrings.getInstance().THREE)
        self.FOUR: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_4, CommonPhoneStrings.getInstance().FOUR)
        self.FIVE: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_5, CommonPhoneStrings.getInstance().FIVE)
        self.SIX: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_6, CommonPhoneStrings.getInstance().SIX)
        self.SEVEN: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_7, CommonPhoneStrings.getInstance().SEVEN)
        self.EIGHT: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_8, CommonPhoneStrings.getInstance().EIGHT)
        self.NINE: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_9, CommonPhoneStrings.getInstance().NINE)
        self.STAR: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_STAR, CommonPhoneStrings.getInstance().STAR)
        self.POUND: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_POUND, CommonPhoneStrings.getInstance().POUND)
        self.DPAD_UP: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_DPAD_UP, "UP")
        self.DPAD_DOWN: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_DPAD_DOWN, "DOWN")
        self.DPAD_LEFT: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_DPAD_LEFT, "LEFT")
        self.DPAD_RIGHT: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_DPAD_RIGHT, "RIGHT")
        self.DPAD_CENTER: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_DPAD_CENTER, "CENTER")
        self.VOLUME_UP: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_VOLUME_UP, "VOLUME_UP")
        self.VOLUME_DOWN: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_VOLUME_DOWN, "VOLUME_DOWN")
        self.POWER: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_POWER, "POWER")
        self.CAMERA: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_CAMERA, "CAMERA")
        self.CLEAR: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_CLEAR, "CLEAR")
        self.A: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_A, "A")
        self.B: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_B, "B")
        self.C: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_C, "C")
        self.D: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_D, "D")
        self.E: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_E, "E")
        self.F: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_F, "F")
        self.G: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_G, "G")
        self.H: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_H, "H")
        self.I: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_I, "I")
        self.J: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_J, "J")
        self.K: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_K, "K")
        self.L: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_L, "L")
        self.M: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_M, "M")
        self.N: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_N, "N")
        self.O: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_O, "O")
        self.P: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_P, "P")
        self.Q: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_Q, "Q")
        self.R: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_R, "R")
        self.S: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_S, "S")
        self.T: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_T, "T")
        self.U: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_U, "U")
        self.V: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_V, "V")
        self.W: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_W, "W")
        self.X: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_X, "X")
        self.Y: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_Y, "Y")
        self.Z: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_Z, "Z")
        self.COMMA: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_COMMA, "COMMA")
        self.PERIOD: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_PERIOD, AbPathData.getInstance().EXTENSION_SEP)
        self.ALT_LEFT: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_ALT_LEFT, "ALT_LEFT")
        self.ALT_RIGHT: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_ALT_RIGHT, "ALT_RIGHT")
        self.SHIFT_LEFT: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_SHIFT_LEFT, "SHIFT_LEFT")
        self.SHIFT_RIGHT: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_SHIFT_RIGHT, "SHIFT_RIGHT")
        self.TAB: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_TAB, "TAB")
        self.SPACE: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_SPACE, "SPACE")
        self.SYM: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_SYM, "SYM")
        self.EXPLORER: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_EXPLORER, "EXPLORER")
        self.ENVELOPE: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_ENVELOPE, "ENVELOPE")
        self.ENTER: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_ENTER, "ENTER")
        self.DEL: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_DEL, "DEL")
        self.GRAVE: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_GRAVE, "GRAVE")
        self.MINUS: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_MINUS, "MINUS")
        self.EQUALS: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_EQUALS, "EQUALS")
        self.LEFT_BRACKET: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_LEFT_BRACKET, "LEFT_BRACKET")
        self.RIGHT_BRACKET: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_RIGHT_BRACKET, "RIGHT_BRACKET")
        self.BACKSLASH: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_BACKSLASH, "BACKSLASH")
        self.SEMICOLON: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_SEMICOLON, "SEMICOLON")
        self.APOSTROPHE: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_APOSTROPHE, "APOSTROPHE")
        self.SLASH: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_SLASH, "SLASH")
        self.AT: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_AT, "AT")
        self.NUM: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_NUM, "NUM")
        self.HEADSETHOOK: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_HEADSETHOOK, "HEADSETHOOK")
        self.FOCUS: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_FOCUS, "FOCUS")
        self.PLUS: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_PLUS, "PLUS")
        self.MENU: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_MENU, "MENU")
        self.NOTIFICATION: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_NOTIFICATION, "NOTIFICATION")
        self.SEARCH: AndroidGameKey = AndroidGameKey(KeyEvent.KEYCODE_SEARCH, "SEARCH")

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def init(self) -> None:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF("Start/End", self, commonStrings.INIT)
    

    def isSubmission(self, input: Input) -> bool:
        if input == self.ENTER:
            return True
        elif input == self.DPAD_CENTER:
            return True
        return False
    

    def isDelete(self, input: Input) -> bool:
        return False
    

    def isBackSpace(self, input: Input) -> bool:
        if input == self.DEL:
            return True
        return False
    

    def isLeft(self, input: Input) -> bool:
        if input == self.DPAD_LEFT:
            return True
        return False
    

    def isRight(self, input: Input) -> bool:
        if input == self.DPAD_RIGHT:
            return True
        return False
    

    def isUp(self, input: Input) -> bool:
        if input == self.DPAD_UP:
            return True
        return False
    

    def isDown(self, input: Input) -> bool:
        if input == self.DPAD_DOWN:
            return True
        return False
    

    def isEnter(self, input: Input) -> bool:
        if input == self.DPAD_CENTER:
            return True
        elif input == self.ENTER:
            return True
        elif input == self.CALL:
            return True
        return False
from android.view.KeyEvent import KeyEvent
from org.allbinary.string.CommonPhoneStrings import CommonPhoneStrings
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.game.input.AndroidGameKey import AndroidGameKey


