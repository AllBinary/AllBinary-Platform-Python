# Generated Code Do Not Modify
# package org.allbinary.game.input

from __future__ import annotations



class AndroidNumberKeyToJ2MECanvasNumberKey:
    androidtoJavaMicroEditionKeyMap: list[int] = [0] * (17)
    

    @staticmethod
    def init() -> None:
        AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[KeyEvent.KEYCODE_0] = Canvas.KEY_NUM0
        AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[KeyEvent.KEYCODE_1] = Canvas.KEY_NUM1
        AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[KeyEvent.KEYCODE_2] = Canvas.KEY_NUM2
        AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[KeyEvent.KEYCODE_3] = Canvas.KEY_NUM3
        AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[KeyEvent.KEYCODE_4] = Canvas.KEY_NUM4
        AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[KeyEvent.KEYCODE_5] = Canvas.KEY_NUM5
        AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[KeyEvent.KEYCODE_6] = Canvas.KEY_NUM6
        AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[KeyEvent.KEYCODE_7] = Canvas.KEY_NUM7
        AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[KeyEvent.KEYCODE_8] = Canvas.KEY_NUM8
        AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[KeyEvent.KEYCODE_9] = Canvas.KEY_NUM9
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getKey(key: int) -> int:
        if key < len(AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap):
            value: int = AndroidNumberKeyToJ2MECanvasNumberKey.androidtoJavaMicroEditionKeyMap[key]
            if value != 0:
                return value
        return key
# from javax.microedition.lcdui.Canvas import Canvas
from android.view.KeyEvent import KeyEvent


