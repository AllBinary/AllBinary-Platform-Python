# Generated Code Do Not Modify
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.game.input.AndroidAPI9KeyFactory import AndroidAPI9KeyFactory


class AndroidAPI12KeyFactory(AndroidAPI9KeyFactory):
    instance12: object = NullUtil.getInstance().NULL_OBJECT
    

    @staticmethod
    def getAPI12Instance() -> AndroidAPI12KeyFactory:
        if AndroidAPI12KeyFactory.instance12 == NullUtil.getInstance().NULL_OBJECT:
            AndroidAPI12KeyFactory.instance12 = AndroidAPI12KeyFactory()
        return AndroidAPI12KeyFactory.instance12
    

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
        from org.allbinary.game.input.AndroidGameKey import AndroidGameKey
        super().__init__()
        self.KEYCODE_BUTTON_1 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_1, "BUTTON 1")
        self.KEYCODE_BUTTON_10 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_10, "BUTTON 10")
        self.KEYCODE_BUTTON_11 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_11, "BUTTON 11")
        self.KEYCODE_BUTTON_12 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_12, "BUTTON 12")
        self.KEYCODE_BUTTON_13 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_13, "BUTTON 13")
        self.KEYCODE_BUTTON_14 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_14, "BUTTON 14")
        self.KEYCODE_BUTTON_15 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_15, "BUTTON 15")
        self.KEYCODE_BUTTON_16 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_16, "BUTTON 16")
        self.KEYCODE_BUTTON_2 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_2, "BUTTON 2")
        self.KEYCODE_BUTTON_3 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_3, "BUTTON 3")
        self.KEYCODE_BUTTON_4 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_4, "BUTTON 4")
        self.KEYCODE_BUTTON_5 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_5, "BUTTON 5")
        self.KEYCODE_BUTTON_6 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_6, "BUTTON 6")
        self.KEYCODE_BUTTON_7 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_7, "BUTTON 7")
        self.KEYCODE_BUTTON_8 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_8, "BUTTON 8")
        self.KEYCODE_BUTTON_9 = AndroidGameKey(KeyEvent.KEYCODE_BUTTON_9, "BUTTON 9")
from android.view.KeyEvent import KeyEvent


