# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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



class ABKeyEventWrapper:
    instance: ABKeyEventWrapper = None

    def _init_fields(self) -> None:
        self.VK_ENTER: int = KeyEvent.VK_ENTER
        self.VK_BACK_SPACE: int = KeyEvent.VK_BACK_SPACE
        self.VK_TAB: int = KeyEvent.VK_TAB
        self.VK_CANCEL: int = KeyEvent.VK_CANCEL
        self.VK_CLEAR: int = KeyEvent.VK_CLEAR
        self.VK_SHIFT: int = KeyEvent.VK_SHIFT
        self.VK_CONTROL: int = KeyEvent.VK_CONTROL
        self.VK_ALT: int = KeyEvent.VK_ALT
        self.VK_PAUSE: int = KeyEvent.VK_PAUSE
        self.VK_CAPS_LOCK: int = KeyEvent.VK_CAPS_LOCK
        self.VK_ESCAPE: int = KeyEvent.VK_ESCAPE
        self.VK_SPACE: int = KeyEvent.VK_SPACE
        self.VK_PAGE_UP: int = KeyEvent.VK_PAGE_UP
        self.VK_PAGE_DOWN: int = KeyEvent.VK_PAGE_DOWN
        self.VK_END: int = KeyEvent.VK_END
        self.VK_HOME: int = KeyEvent.VK_HOME
        self.VK_LEFT: int = KeyEvent.VK_LEFT
        self.VK_UP: int = KeyEvent.VK_UP
        self.VK_RIGHT: int = KeyEvent.VK_RIGHT
        self.VK_DOWN: int = KeyEvent.VK_DOWN
        self.VK_COMMA: int = KeyEvent.VK_COMMA
        self.VK_MINUS: int = KeyEvent.VK_MINUS
        self.VK_PERIOD: int = KeyEvent.VK_PERIOD
        self.VK_SLASH: int = KeyEvent.VK_SLASH
        self.VK_0: int = KeyEvent.VK_0
        self.VK_1: int = KeyEvent.VK_1
        self.VK_2: int = KeyEvent.VK_2
        self.VK_3: int = KeyEvent.VK_3
        self.VK_4: int = KeyEvent.VK_4
        self.VK_5: int = KeyEvent.VK_5
        self.VK_6: int = KeyEvent.VK_6
        self.VK_7: int = KeyEvent.VK_7
        self.VK_8: int = KeyEvent.VK_8
        self.VK_9: int = KeyEvent.VK_9
        self.VK_SEMICOLON: int = KeyEvent.VK_SEMICOLON
        self.VK_EQUALS: int = KeyEvent.VK_EQUALS
        self.VK_A: int = KeyEvent.VK_A
        self.VK_B: int = KeyEvent.VK_B
        self.VK_C: int = KeyEvent.VK_C
        self.VK_D: int = KeyEvent.VK_D
        self.VK_E: int = KeyEvent.VK_E
        self.VK_F: int = KeyEvent.VK_F
        self.VK_G: int = KeyEvent.VK_G
        self.VK_H: int = KeyEvent.VK_H
        self.VK_I: int = KeyEvent.VK_I
        self.VK_J: int = KeyEvent.VK_J
        self.VK_K: int = KeyEvent.VK_K
        self.VK_L: int = KeyEvent.VK_L
        self.VK_M: int = KeyEvent.VK_M
        self.VK_N: int = KeyEvent.VK_N
        self.VK_O: int = KeyEvent.VK_O
        self.VK_P: int = KeyEvent.VK_P
        self.VK_Q: int = KeyEvent.VK_Q
        self.VK_R: int = KeyEvent.VK_R
        self.VK_S: int = KeyEvent.VK_S
        self.VK_T: int = KeyEvent.VK_T
        self.VK_U: int = KeyEvent.VK_U
        self.VK_V: int = KeyEvent.VK_V
        self.VK_W: int = KeyEvent.VK_W
        self.VK_X: int = KeyEvent.VK_X
        self.VK_Y: int = KeyEvent.VK_Y
        self.VK_Z: int = KeyEvent.VK_Z
        self.VK_OPEN_BRACKET: int = KeyEvent.VK_OPEN_BRACKET
        self.VK_BACK_SLASH: int = KeyEvent.VK_BACK_SLASH
        self.VK_CLOSE_BRACKET: int = KeyEvent.VK_CLOSE_BRACKET
        self.VK_NUMPAD0: int = KeyEvent.VK_NUMPAD0
        self.VK_NUMPAD1: int = KeyEvent.VK_NUMPAD1
        self.VK_NUMPAD2: int = KeyEvent.VK_NUMPAD2
        self.VK_NUMPAD3: int = KeyEvent.VK_NUMPAD3
        self.VK_NUMPAD4: int = KeyEvent.VK_NUMPAD4
        self.VK_NUMPAD5: int = KeyEvent.VK_NUMPAD5
        self.VK_NUMPAD6: int = KeyEvent.VK_NUMPAD6
        self.VK_NUMPAD7: int = KeyEvent.VK_NUMPAD7
        self.VK_NUMPAD8: int = KeyEvent.VK_NUMPAD8
        self.VK_NUMPAD9: int = KeyEvent.VK_NUMPAD9
        self.VK_MULTIPLY: int = KeyEvent.VK_MULTIPLY
        self.VK_ADD: int = KeyEvent.VK_ADD
        self.VK_SEPARATER: int = KeyEvent.VK_SEPARATER
        self.VK_SEPARATOR: int = KeyEvent.VK_SEPARATOR
        self.VK_SUBTRACT: int = KeyEvent.VK_SUBTRACT
        self.VK_DECIMAL: int = KeyEvent.VK_DECIMAL
        self.VK_DIVIDE: int = KeyEvent.VK_DIVIDE
        self.VK_DELETE: int = KeyEvent.VK_DELETE
        self.VK_NUM_LOCK: int = KeyEvent.VK_NUM_LOCK
        self.VK_SCROLL_LOCK: int = KeyEvent.VK_SCROLL_LOCK
        self.VK_F1: int = KeyEvent.VK_F1
        self.VK_F2: int = KeyEvent.VK_F2
        self.VK_F3: int = KeyEvent.VK_F3
        self.VK_F4: int = KeyEvent.VK_F4
        self.VK_F5: int = KeyEvent.VK_F5
        self.VK_F6: int = KeyEvent.VK_F6
        self.VK_F7: int = KeyEvent.VK_F7
        self.VK_F8: int = KeyEvent.VK_F8
        self.VK_F9: int = KeyEvent.VK_F9
        self.VK_F10: int = KeyEvent.VK_F10
        self.VK_F11: int = KeyEvent.VK_F11
        self.VK_F12: int = KeyEvent.VK_F12
        self.VK_F13: int = KeyEvent.VK_F13
        self.VK_F14: int = KeyEvent.VK_F14
        self.VK_F15: int = KeyEvent.VK_F15
        self.VK_F16: int = KeyEvent.VK_F16
        self.VK_F17: int = KeyEvent.VK_F17
        self.VK_F18: int = KeyEvent.VK_F18
        self.VK_F19: int = KeyEvent.VK_F19
        self.VK_F20: int = KeyEvent.VK_F20
        self.VK_F21: int = KeyEvent.VK_F21
        self.VK_F22: int = KeyEvent.VK_F22
        self.VK_F23: int = KeyEvent.VK_F23
        self.VK_F24: int = KeyEvent.VK_F24
        self.VK_PRINTSCREEN: int = KeyEvent.VK_PRINTSCREEN
        self.VK_INSERT: int = KeyEvent.VK_INSERT
        self.VK_HELP: int = KeyEvent.VK_HELP
        self.VK_META: int = KeyEvent.VK_META
        self.VK_BACK_QUOTE: int = KeyEvent.VK_BACK_QUOTE
        self.VK_QUOTE: int = KeyEvent.VK_QUOTE
        self.VK_KP_UP: int = KeyEvent.VK_KP_UP
        self.VK_KP_DOWN: int = KeyEvent.VK_KP_DOWN
        self.VK_KP_LEFT: int = KeyEvent.VK_KP_LEFT
        self.VK_KP_RIGHT: int = KeyEvent.VK_KP_RIGHT
        self.VK_DEAD_GRAVE: int = KeyEvent.VK_DEAD_GRAVE
        self.VK_DEAD_ACUTE: int = KeyEvent.VK_DEAD_ACUTE
        self.VK_DEAD_CIRCUMFLEX: int = KeyEvent.VK_DEAD_CIRCUMFLEX
        self.VK_DEAD_TILDE: int = KeyEvent.VK_DEAD_TILDE
        self.VK_DEAD_MACRON: int = KeyEvent.VK_DEAD_MACRON
        self.VK_DEAD_BREVE: int = KeyEvent.VK_DEAD_BREVE
        self.VK_DEAD_ABOVEDOT: int = KeyEvent.VK_DEAD_ABOVEDOT
        self.VK_DEAD_DIAERESIS: int = KeyEvent.VK_DEAD_DIAERESIS
        self.VK_DEAD_ABOVERING: int = KeyEvent.VK_DEAD_ABOVERING
        self.VK_DEAD_DOUBLEACUTE: int = KeyEvent.VK_DEAD_DOUBLEACUTE
        self.VK_DEAD_CARON: int = KeyEvent.VK_DEAD_CARON
        self.VK_DEAD_CEDILLA: int = KeyEvent.VK_DEAD_CEDILLA
        self.VK_DEAD_OGONEK: int = KeyEvent.VK_DEAD_OGONEK
        self.VK_DEAD_IOTA: int = KeyEvent.VK_DEAD_IOTA
        self.VK_DEAD_VOICED_SOUND: int = KeyEvent.VK_DEAD_VOICED_SOUND
        self.VK_DEAD_SEMIVOICED_SOUND: int = KeyEvent.VK_DEAD_SEMIVOICED_SOUND
        self.VK_AMPERSAND: int = KeyEvent.VK_AMPERSAND
        self.VK_ASTERISK: int = KeyEvent.VK_ASTERISK
        self.VK_QUOTEDBL: int = KeyEvent.VK_QUOTEDBL
        self.VK_LESS: int = KeyEvent.VK_LESS
        self.VK_GREATER: int = KeyEvent.VK_GREATER
        self.VK_BRACELEFT: int = KeyEvent.VK_BRACELEFT
        self.VK_BRACERIGHT: int = KeyEvent.VK_BRACERIGHT
        self.VK_AT: int = KeyEvent.VK_AT
        self.VK_COLON: int = KeyEvent.VK_COLON
        self.VK_CIRCUMFLEX: int = KeyEvent.VK_CIRCUMFLEX
        self.VK_DOLLAR: int = KeyEvent.VK_DOLLAR
        self.VK_EURO_SIGN: int = KeyEvent.VK_EURO_SIGN
        self.VK_EXCLAMATION_MARK: int = KeyEvent.VK_EXCLAMATION_MARK
        self.VK_INVERTED_EXCLAMATION_MARK: int = KeyEvent.VK_INVERTED_EXCLAMATION_MARK
        self.VK_LEFT_PARENTHESIS: int = KeyEvent.VK_LEFT_PARENTHESIS
        self.VK_NUMBER_SIGN: int = KeyEvent.VK_NUMBER_SIGN
        self.VK_PLUS: int = KeyEvent.VK_PLUS
        self.VK_RIGHT_PARENTHESIS: int = KeyEvent.VK_RIGHT_PARENTHESIS
        self.VK_UNDERSCORE: int = KeyEvent.VK_UNDERSCORE
        self.VK_WINDOWS: int = KeyEvent.VK_WINDOWS
        self.VK_CONTEXT_MENU: int = KeyEvent.VK_CONTEXT_MENU
        self.VK_FINAL: int = KeyEvent.VK_FINAL
        self.VK_CONVERT: int = KeyEvent.VK_CONVERT
        self.VK_NONCONVERT: int = KeyEvent.VK_NONCONVERT
        self.VK_ACCEPT: int = KeyEvent.VK_ACCEPT
        self.VK_MODECHANGE: int = KeyEvent.VK_MODECHANGE
        self.VK_KANA: int = KeyEvent.VK_KANA
        self.VK_KANJI: int = KeyEvent.VK_KANJI
        self.VK_ALPHANUMERIC: int = KeyEvent.VK_ALPHANUMERIC
        self.VK_KATAKANA: int = KeyEvent.VK_KATAKANA
        self.VK_HIRAGANA: int = KeyEvent.VK_HIRAGANA
        self.VK_FULL_WIDTH: int = KeyEvent.VK_FULL_WIDTH
        self.VK_HALF_WIDTH: int = KeyEvent.VK_HALF_WIDTH
        self.VK_ROMAN_CHARACTERS: int = KeyEvent.VK_ROMAN_CHARACTERS
        self.VK_ALL_CANDIDATES: int = KeyEvent.VK_ALL_CANDIDATES
        self.VK_PREVIOUS_CANDIDATE: int = KeyEvent.VK_PREVIOUS_CANDIDATE
        self.VK_CODE_INPUT: int = KeyEvent.VK_CODE_INPUT
        self.VK_JAPANESE_KATAKANA: int = KeyEvent.VK_JAPANESE_KATAKANA
        self.VK_JAPANESE_HIRAGANA: int = KeyEvent.VK_JAPANESE_HIRAGANA
        self.VK_JAPANESE_ROMAN: int = KeyEvent.VK_JAPANESE_ROMAN
        self.VK_KANA_LOCK: int = KeyEvent.VK_KANA_LOCK
        self.VK_INPUT_METHOD_ON_OFF: int = KeyEvent.VK_INPUT_METHOD_ON_OFF
        self.VK_CUT: int = KeyEvent.VK_CUT
        self.VK_COPY: int = KeyEvent.VK_COPY
        self.VK_PASTE: int = KeyEvent.VK_PASTE
        self.VK_UNDO: int = KeyEvent.VK_UNDO
        self.VK_AGAIN: int = KeyEvent.VK_AGAIN
        self.VK_FIND: int = KeyEvent.VK_FIND
        self.VK_PROPS: int = KeyEvent.VK_PROPS
        self.VK_STOP: int = KeyEvent.VK_STOP
        self.VK_COMPOSE: int = KeyEvent.VK_COMPOSE
        self.VK_ALT_GRAPH: int = KeyEvent.VK_ALT_GRAPH
        self.VK_BEGIN: int = KeyEvent.VK_BEGIN
        self.VK_UNDEFINED: int = KeyEvent.VK_UNDEFINED

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ABKeyEventWrapper:
        return ABKeyEventWrapper.instance
# from java.awt.event.KeyEvent import KeyEvent
from jsinterop.annotations.JsType import JsType


ABKeyEventWrapper.instance = ABKeyEventWrapper()

