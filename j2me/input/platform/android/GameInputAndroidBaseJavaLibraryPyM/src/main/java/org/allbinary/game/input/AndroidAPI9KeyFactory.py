# Generated Code Do Not Modify
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.game.input.AndroidKeyFactory import AndroidKeyFactory


class AndroidAPI9KeyFactory(AndroidKeyFactory):
    instance: object = NullUtil.getInstance().NULL_OBJECT
    

    @staticmethod
    def getInstance() -> AndroidAPI9KeyFactory:
        if AndroidAPI9KeyFactory.instance == NullUtil.getInstance().NULL_OBJECT:
            AndroidAPI9KeyFactory.instance = AndroidAPI9KeyFactory()
        return AndroidAPI9KeyFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        super().__init__()
        self.KEYCODE_BUTTON_L1 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_L1, "BUTTON L1")
        self.KEYCODE_BUTTON_R1 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_R1, "BUTTON R1")
        self.KEYCODE_BUTTON_THUMBR = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_THUMBR, "BUTTON THUMBR")
        self.KEYCODE_BUTTON_THUMBL = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_THUMBL, "BUTTON THUMBL")
        self.KEYCODE_BUTTON_START = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_START, "BUTTON START")
        self.KEYCODE_BUTTON_MODE = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_MODE, "BUTTON MODE")
        self.KEYCODE_BUTTON_B = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_B, "BUTTON B")
        self.KEYCODE_BUTTON_A = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_A, "BUTTON A")
        self.KEYCODE_BUTTON_X = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_X, "BUTTON X")
        self.KEYCODE_BUTTON_Y = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_Y, "BUTTON Y")
        self.KEYCODE_BUTTON_L2 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_L2, "BUTTON L2")
        self.KEYCODE_BUTTON_R2 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_R2, "BUTTON R2")
        self.KEYCODE_BUTTON_SELECT = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_SELECT, "BUTTON SELECT")
        self.KEYCODE_BUTTON_C = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_C, "BUTTON C")
        self.KEYCODE_BUTTON_Z = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_Z, "BUTTON Z")
from android.view.KeyEvent import KeyEvent


