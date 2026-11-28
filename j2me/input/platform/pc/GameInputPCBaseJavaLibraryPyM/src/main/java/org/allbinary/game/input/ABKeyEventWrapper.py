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

from java.lang.JavaRuntimeStatic import lazy_static


class ABKeyEventWrapper:
    instance: ABKeyEventWrapper = None

    def _init_fields(self) -> None:
        self.VK_ENTER: int = 10
        self.VK_BACK_SPACE: int = 8
        self.VK_TAB: int = 9
        self.VK_CANCEL: int = 3
        self.VK_CLEAR: int = 12
        self.VK_SHIFT: int = 16
        self.VK_CONTROL: int = 17
        self.VK_ALT: int = 18
        self.VK_PAUSE: int = 19
        self.VK_CAPS_LOCK: int = 20
        self.VK_ESCAPE: int = 27
        self.VK_SPACE: int = 32
        self.VK_PAGE_UP: int = 33
        self.VK_PAGE_DOWN: int = 34
        self.VK_END: int = 35
        self.VK_HOME: int = 36
        self.VK_LEFT: int = 37
        self.VK_UP: int = 38
        self.VK_RIGHT: int = 39
        self.VK_DOWN: int = 40
        self.VK_COMMA: int = 44
        self.VK_MINUS: int = 45
        self.VK_PERIOD: int = 46
        self.VK_SLASH: int = 47
        self.VK_0: int = 48
        self.VK_1: int = 49
        self.VK_2: int = 50
        self.VK_3: int = 51
        self.VK_4: int = 52
        self.VK_5: int = 53
        self.VK_6: int = 54
        self.VK_7: int = 55
        self.VK_8: int = 56
        self.VK_9: int = 57
        self.VK_SEMICOLON: int = 59
        self.VK_EQUALS: int = 61
        self.VK_A: int = 65
        self.VK_B: int = 66
        self.VK_C: int = 67
        self.VK_D: int = 68
        self.VK_E: int = 69
        self.VK_F: int = 70
        self.VK_G: int = 71
        self.VK_H: int = 72
        self.VK_I: int = 73
        self.VK_J: int = 74
        self.VK_K: int = 75
        self.VK_L: int = 76
        self.VK_M: int = 77
        self.VK_N: int = 78
        self.VK_O: int = 79
        self.VK_P: int = 80
        self.VK_Q: int = 81
        self.VK_R: int = 82
        self.VK_S: int = 83
        self.VK_T: int = 84
        self.VK_U: int = 85
        self.VK_V: int = 86
        self.VK_W: int = 87
        self.VK_X: int = 88
        self.VK_Y: int = 89
        self.VK_Z: int = 90
        self.VK_OPEN_BRACKET: int = 91
        self.VK_BACK_SLASH: int = 92
        self.VK_CLOSE_BRACKET: int = 93
        self.VK_NUMPAD0: int = 96
        self.VK_NUMPAD1: int = 97
        self.VK_NUMPAD2: int = 98
        self.VK_NUMPAD3: int = 99
        self.VK_NUMPAD4: int = 100
        self.VK_NUMPAD5: int = 101
        self.VK_NUMPAD6: int = 102
        self.VK_NUMPAD7: int = 103
        self.VK_NUMPAD8: int = 104
        self.VK_NUMPAD9: int = 105
        self.VK_MULTIPLY: int = 106
        self.VK_ADD: int = 107
        self.VK_SEPARATER: int = 108
        self.VK_SEPARATOR: int = 108
        self.VK_SUBTRACT: int = 109
        self.VK_DECIMAL: int = 110
        self.VK_DIVIDE: int = 111
        self.VK_DELETE: int = 127
        self.VK_NUM_LOCK: int = 144
        self.VK_SCROLL_LOCK: int = 145
        self.VK_F1: int = 112
        self.VK_F2: int = 113
        self.VK_F3: int = 114
        self.VK_F4: int = 115
        self.VK_F5: int = 116
        self.VK_F6: int = 117
        self.VK_F7: int = 118
        self.VK_F8: int = 119
        self.VK_F9: int = 120
        self.VK_F10: int = 121
        self.VK_F11: int = 122
        self.VK_F12: int = 123
        self.VK_F13: int = 61440
        self.VK_F14: int = 61441
        self.VK_F15: int = 61442
        self.VK_F16: int = 61443
        self.VK_F17: int = 61444
        self.VK_F18: int = 61445
        self.VK_F19: int = 61446
        self.VK_F20: int = 61447
        self.VK_F21: int = 61448
        self.VK_F22: int = 61449
        self.VK_F23: int = 61450
        self.VK_F24: int = 61451
        self.VK_PRINTSCREEN: int = 154
        self.VK_INSERT: int = 155
        self.VK_HELP: int = 156
        self.VK_META: int = 157
        self.VK_BACK_QUOTE: int = 192
        self.VK_QUOTE: int = 222
        self.VK_KP_UP: int = 224
        self.VK_KP_DOWN: int = 225
        self.VK_KP_LEFT: int = 226
        self.VK_KP_RIGHT: int = 227
        self.VK_DEAD_GRAVE: int = 128
        self.VK_DEAD_ACUTE: int = 129
        self.VK_DEAD_CIRCUMFLEX: int = 130
        self.VK_DEAD_TILDE: int = 131
        self.VK_DEAD_MACRON: int = 132
        self.VK_DEAD_BREVE: int = 133
        self.VK_DEAD_ABOVEDOT: int = 134
        self.VK_DEAD_DIAERESIS: int = 135
        self.VK_DEAD_ABOVERING: int = 136
        self.VK_DEAD_DOUBLEACUTE: int = 137
        self.VK_DEAD_CARON: int = 138
        self.VK_DEAD_CEDILLA: int = 139
        self.VK_DEAD_OGONEK: int = 140
        self.VK_DEAD_IOTA: int = 141
        self.VK_DEAD_VOICED_SOUND: int = 142
        self.VK_DEAD_SEMIVOICED_SOUND: int = 143
        self.VK_AMPERSAND: int = 150
        self.VK_ASTERISK: int = 151
        self.VK_QUOTEDBL: int = 152
        self.VK_LESS: int = 153
        self.VK_GREATER: int = 160
        self.VK_BRACELEFT: int = 161
        self.VK_BRACERIGHT: int = 162
        self.VK_AT: int = 512
        self.VK_COLON: int = 513
        self.VK_CIRCUMFLEX: int = 514
        self.VK_DOLLAR: int = 515
        self.VK_EURO_SIGN: int = 516
        self.VK_EXCLAMATION_MARK: int = 517
        self.VK_INVERTED_EXCLAMATION_MARK: int = 518
        self.VK_LEFT_PARENTHESIS: int = 519
        self.VK_NUMBER_SIGN: int = 520
        self.VK_PLUS: int = 521
        self.VK_RIGHT_PARENTHESIS: int = 522
        self.VK_UNDERSCORE: int = 523
        self.VK_WINDOWS: int = 524
        self.VK_CONTEXT_MENU: int = 525
        self.VK_FINAL: int = 24
        self.VK_CONVERT: int = 28
        self.VK_NONCONVERT: int = 29
        self.VK_ACCEPT: int = 30
        self.VK_MODECHANGE: int = 31
        self.VK_KANA: int = 21
        self.VK_KANJI: int = 25
        self.VK_ALPHANUMERIC: int = 240
        self.VK_KATAKANA: int = 241
        self.VK_HIRAGANA: int = 242
        self.VK_FULL_WIDTH: int = 243
        self.VK_HALF_WIDTH: int = 244
        self.VK_ROMAN_CHARACTERS: int = 245
        self.VK_ALL_CANDIDATES: int = 256
        self.VK_PREVIOUS_CANDIDATE: int = 257
        self.VK_CODE_INPUT: int = 258
        self.VK_JAPANESE_KATAKANA: int = 259
        self.VK_JAPANESE_HIRAGANA: int = 260
        self.VK_JAPANESE_ROMAN: int = 261
        self.VK_KANA_LOCK: int = 262
        self.VK_INPUT_METHOD_ON_OFF: int = 263
        self.VK_CUT: int = 65489
        self.VK_COPY: int = 65485
        self.VK_PASTE: int = 65487
        self.VK_UNDO: int = 65483
        self.VK_AGAIN: int = 65481
        self.VK_FIND: int = 65488
        self.VK_PROPS: int = 65482
        self.VK_STOP: int = 65480
        self.VK_COMPOSE: int = 65312
        self.VK_ALT_GRAPH: int = 65406
        self.VK_BEGIN: int = 65368
        self.VK_UNDEFINED: int = 0

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> ABKeyEventWrapper:
        return ABKeyEventWrapper.instance
# from java.awt.event.KeyEvent import KeyEvent
# from jsinterop.annotations.JsType import JsType


def _ABKeyEventWrapper_instance() -> object:
    return ABKeyEventWrapper()

lazy_static(ABKeyEventWrapper, "instance", _ABKeyEventWrapper_instance)

